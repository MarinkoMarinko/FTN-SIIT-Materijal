class EmptyQueueError(Exception):
    pass

class Queue(): 
    def __init__(self):
        self._values = []
    def __len__(self):
        return len(self._values)
    def enqueue(self, num):
        self._values.append(num)
    def dequeue(self):
        if len(self._values) == 0:
            raise EmptyQueueError("Queue is already empty!")
        return self._values.pop(0)
    def top(self):
        if len(self._values) == 0:
            raise EmptyQueueError("Queue is empty!")
        return self._values[-1]
    def __str__(self):
        return str(self._values)
if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(3)
    queue.enqueue(2)
    queue.enqueue(1)
    print(queue.top())
    print(queue)
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()