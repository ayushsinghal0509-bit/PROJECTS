# multi object tracking: yolov8 + simple iou tracker (bytetrack style)
import os
import numpy as np
import cv2
from scipy.optimize import linear_sum_assignment
from ultralytics import YOLO

TEST_DIR = r"D:/yolo"
OUT_DIR = "output"
HIGH_CONF = 0.4    # confident detections
LOW_CONF = 0.1     # weak detections, only used to keep existing tracks alive
NEW_CONF = 0.5     # min confidence to start a new track
MAX_LOST = 40      # frames a track survives without a match
MIN_IOU = 0.2

model = YOLO("yolov8x.pt")


class Track:
    count = 0

    def __init__(self, box, frame):
        Track.count += 1
        self.id = Track.count
        self.box = box
        self.vel = np.zeros(4)
        self.lost = 0
        self.seen = frame

    def predict(self):
        return self.box + self.vel

    def update(self, box, frame):
        self.vel = 0.7 * self.vel + 0.3 * (box - self.box)
        self.box = box
        self.lost = 0
        self.seen = frame


def iou(a, b):
    x1 = np.maximum(a[:, None, 0], b[None, :, 0])
    y1 = np.maximum(a[:, None, 1], b[None, :, 1])
    x2 = np.minimum(a[:, None, 2], b[None, :, 2])
    y2 = np.minimum(a[:, None, 3], b[None, :, 3])
    inter = np.clip(x2 - x1, 0, None) * np.clip(y2 - y1, 0, None)
    area_a = (a[:, 2] - a[:, 0]) * (a[:, 3] - a[:, 1])
    area_b = (b[:, 2] - b[:, 0]) * (b[:, 3] - b[:, 1])
    return inter / (area_a[:, None] + area_b[None, :] - inter + 1e-6)


def match(tracks, boxes):
    # hungarian matching on iou, returns (track, det) pairs + leftovers
    if len(tracks) == 0 or len(boxes) == 0:
        return [], list(range(len(tracks))), list(range(len(boxes)))
    sim = iou(np.array([t.predict() for t in tracks]), boxes)
    rows, cols = linear_sum_assignment(-sim)
    pairs = [(r, c) for r, c in zip(rows, cols) if sim[r, c] >= MIN_IOU]
    left_t = [i for i in range(len(tracks)) if i not in {p[0] for p in pairs}]
    left_d = [j for j in range(len(boxes)) if j not in {p[1] for p in pairs}]
    return pairs, left_t, left_d


def track_sequence(frames):
    Track.count = 0
    tracks, results = [], []
    for f, path in enumerate(frames, start=1):
        r = model(path, imgsz=1280, conf=LOW_CONF, iou=0.7, classes=[0], max_det=500, verbose=False)[0]
        boxes = r.boxes.xyxy.cpu().numpy()
        confs = r.boxes.conf.cpu().numpy()
        high, high_conf = boxes[confs >= HIGH_CONF], confs[confs >= HIGH_CONF]
        low = boxes[confs < HIGH_CONF]

        # round 1: every track (even lost ones) vs confident boxes
        pairs, left_t, left_d = match(tracks, high)
        for t, d in pairs:
            tracks[t].update(high[d], f)

        # round 2: tracks that were visible last frame vs weak boxes (occluded people)
        rest = [tracks[i] for i in left_t if tracks[i].lost == 0]
        pairs2, _, _ = match(rest, low)
        for t, d in pairs2:
            rest[t].update(low[d], f)

        # nobody matched -> start new track if the detection is confident enough
        for d in left_d:
            if high_conf[d] >= NEW_CONF:
                tracks.append(Track(high[d], f))

        for t in tracks:
            if t.seen != f:            # not matched this frame, keep moving it
                t.box = t.predict()
                t.vel *= 0.9
                t.lost += 1
            else:
                results.append((f, t.id, *t.box))
        tracks = [t for t in tracks if t.lost <= MAX_LOST]
    return results


def save(results, path, w, h):
    with open(path, "w") as fh:
        for f, tid, x1, y1, x2, y2 in results:
            x1, y1, x2, y2 = max(x1, 0), max(y1, 0), min(x2, w), min(y2, h)
            if x2 - x1 < 1 or y2 - y1 < 1:
                continue
            fh.write(f"{f},{tid},{x1:.2f},{y1:.2f},{x2 - x1:.2f},{y2 - y1:.2f},-1,-1,-1,-1\n")


if __name__ == "__main__":
    os.makedirs(OUT_DIR, exist_ok=True)
    seqs = sorted(os.listdir(TEST_DIR))
    for i, name in enumerate(seqs, start=1):
        folder = os.path.join(TEST_DIR, name, "img1")
        frames = sorted(os.path.join(folder, f) for f in os.listdir(folder) if f.endswith((".jpg", ".png")))
        h, w = cv2.imread(frames[0]).shape[:2]
        res = track_sequence(frames)
        save(res, os.path.join(OUT_DIR, f"{i:02d}.txt"), w, h)
        print(name, "->", f"{i:02d}.txt", "| ids:", Track.count)