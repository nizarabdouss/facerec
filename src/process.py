import verification as v
import collect
import cv2


class Queue:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def worker(self, frame) -> None:
        if not self.isEmpty():
            currHash = self.dequeue()
            x1, y1, x2, y2 = currHash[0], currHash[1], currHash[2]+currHash[0], currHash[3]+currHash[1]
            currFace = frame[y1:y1 + x2-x1, x1:x1 + y2-y1]
            if not v.Verify(currFace).get_existance():
                temp = collect.Person(currFace)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)
            else:
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 200, 0), 4)
    



