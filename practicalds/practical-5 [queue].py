#Queue

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue)<1:
            return None
        return self.queue.pop(0)

    def display(self):
        print(self.queue)

    def size(self):
        print(len(self.queue))

q = Queue()
q.enqueue(34)
q.enqueue(45)
q.enqueue(69)
q.enqueue(34)
q.enqueue(25)
q.size()
q.display()
q.dequeue()
print("After removing an element")
q.display()

