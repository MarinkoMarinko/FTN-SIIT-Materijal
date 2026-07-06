class CircularQueue():
    def __init__(self, capacity):
        self._values = [None] * capacity
        self._capacity = capacity
        self._current_size = 0
        self._first = 0
        self._rear = 0

    def is_empty(self):
        return self._current_size == 0
    
    def is_full(self):
        return self._current_size == self._capacity
    
    def enqueue(self, val):
        if self.is_full():
            raise Exception("Queue is full!")
        self._values[self._rear] = val
        self._rear = (self._rear + 1) % self._capacity
        self._current_size = self._current_size + 1
    
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty!")
        self._values[self._first] = None
        self._first = (self._first + 1 ) % self._capacity
        self._current_size = self._current_size - 1

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty!")
        return self._values[self._first]
    
    def __str__(self):
        result = []

        for i in range(self._current_size):
            index = (self._first + i) % self._capacity
            result.append(str(self._values[index]))

        return " ".join(result)
    
if __name__ == "__main__":
    try:
        cq = CircularQueue(5)
        cq.enqueue(1)
        cq.enqueue(2)
        cq.enqueue(3)
        print(cq)
        cq.dequeue()
        print(cq)
        print(cq.peek())
        
    except Exception as e:
        print(e)