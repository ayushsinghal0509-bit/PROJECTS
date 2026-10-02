import cv2
import math
from ultralytics import YOLO

class SimpleTracker:
    def __init__(self):
        self.center_points = {}
        self.id_count = 0
    def update(self, objects_rect):
        box_ids = []
        for rect in objects_rect:
            x, y, w, h, cls_id = rect
            cx = (x + x + w)//2
            cy = (y + y + h)//2
            duplicate = False
            
            for obj_id, pt in self.center_points.items():
                old_cx, old_cy, old_cls_id = pt
                dist = math.hypot(cx - old_cx, cy - old_cy)

                if dist < 50 and cls_id == old_cls_id:
                    self.center_points[obj_id] = (cx, cy, cls_id)
                    box_ids.append([x, y, w, h, obj_id, cls_id])
                    duplicate = True
                    break

            if not duplicate:
                self.center_points[self.id_count] = (cx, cy, cls_id)
                box_ids.append([x, y, w, h, self.id_count, cls_id])
                self.id_count += 1

        new_center_points = {}
        for box_id in box_ids:
            object_id = box_id[4]
            new_center_points[object_id] = self.center_points[object_id]

        self.center_points = new_center_points.copy()
        return box_ids

if __name__ == "__main__":
    cap = cv2.VideoCapture(0) 

    model = YOLO("yolov8n.pt") 
    tracker = SimpleTracker()
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        results = model(frame, stream=True, verbose=False)
        objects = []
        for r in results:
            boxes = r.boxes
            for box in boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                w = x2 - x1
                h = y2 - y1
                cls_id = int(box.cls[0]) 
                objects.append([x1, y1, w, h, cls_id])
        boxes_ids = tracker.update(objects)

        for box_id in boxes_ids:
            x, y, w, h, obj_id, cls_id = box_id
            class_name = model.names[cls_id]
            label = f"{class_name} ID: {obj_id}"
            cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imshow("Simple Tracker", frame)
        if cv2.waitKey(1) & 0xFF == 27: 
            break
    cap.release()
    cv2.destroyAllWindows() 
