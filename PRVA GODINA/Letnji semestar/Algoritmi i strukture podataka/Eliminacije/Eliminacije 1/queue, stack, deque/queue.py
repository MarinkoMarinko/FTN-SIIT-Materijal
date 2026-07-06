class Queue:
    def __init__(self):
        self._values = []

    def is_empty(self):
        return len(self._values) == 0
    
    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty!")  
        else:
            return self._values[0]
    
    def enqueue(self, val):
        self._values.append(val)      
    
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty!")
        else:
            del self._values[0]
    
    def __str__(self):
        return " ".join(str(val) for val in self._values)

if __name__ == "__main__":
    try:
        q = Queue()
        q.dequeue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        print(q)
        q.dequeue()
        print(q.peek())
    except Exception as e:
        print(e)         