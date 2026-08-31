class Stack:
    def __init__(self) -> None:
        #YOU CAN (AND SHOULD!) MODIFY THIS FUNCTION
        # pass
        self.l=[]
        return
    def push(self,ele):
        self.l.append(ele)
    def pop(self):
        return self.l.pop()
    def length(self):
        return len(self.l)
    def top(self): #changed
        return self.l[-1]
    def print(self):
        print(*self.l)
    def __str__(self):
        s=""
        for i in range(len(self.l)):
            s+=str(self.l[i])+" "
        return s
    # You can implement this class however you like