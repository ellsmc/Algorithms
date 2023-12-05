# Array representation
class Queue:
    def __init__(self, capacity):
        self.front = 0
        self.size = 0
        self.capacity = capacity
        self.rear = capacity - 1
        self.Qarray = [None]*capacity
        
    # Queue is full when size equals capacity
    def isFull(self):
        return self.size == self.capacity
 
    # Queue is empty when size is 0
    def isEmpty(self):
        return self.size == 0
 
    # Function to add an item to the queue.
    def Enqueue(self, item):
        """
        adds an element to the end of the queue
        """
        # Check if the queue is full
        if self.isFull():
            print("Full")
            return
        # increment the rear pointer to point to the next empty space
        self.rear = (self.rear + 1) % (self.capacity)
        # Add the data element to the queue location, where the rear is pointing
        self.Q[self.rear] = item
        self.size = self.size + 1
        print("% s enqueued to queue" % str(item))
 
    # Function to remove an item from queue.
    def Dequeue(self):
        if self.isEmpty():
            print("Empty")
            return
 
        print("% s dequeued from queue" % str(self.Q[self.front]))
        self.front = (self.front + 1) % (self.capacity)
        self.size = self.size - 1
 
    # get front of queue
    def que_front(self):
        if self.isEmpty():
            print("Queue is empty")
 
        print("Front item is", self.Q[self.front])
 
    # get rear of queue
    def que_rear(self):
        if self.isEmpty():
            print("Queue is empty")
        print("Rear item is",  self.Q[self.rear])
 

if __name__ == '__main__':
 
    queue = Queue(30)
    queue.EnQueue(10)
    queue.EnQueue(20)
    queue.EnQueue(30)
    queue.EnQueue(40)
    queue.DeQueue()
    queue.que_front()
    queue.que_rear()


# Linked List Representation
# class QNode:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# class Queue:
#     def __init__(self) -> None:
#         self.front = None
#         self.rear = None

