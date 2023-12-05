# Array representation
class Queue:
    def __init__(self, cap):
        self.cap = cap
        self.front = 0
        self.size = 0
        self.rear = cap - 1
        self.arr = [0] * cap

    def createQueue(self):
        return Queue(self.cap)
    
# Linked List Representation
class QNode:
    def __init__(self, data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self) -> None:
        self.front = None
        self.rear = None
        ``
