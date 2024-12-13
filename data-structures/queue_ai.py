class Queue:
    def __init__(self, *data):
        self.data = list(data) if data else []
        
    def enqueue(self, item):
        self.data.append(item)
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue operation failed: the queue is empty.")
        return self.data.pop()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek operation failed: the queue is empty.")
        return self.data[-1]
    
    def reverse(self):
        self.data.reverse()
    
    def is_empty(self):
        return self.size() == 0
    
    def size(self):
        return len(self.data)
    
    def __repr__(self):
        queue_in_string = map(str, self.data)
        return f"Queue({', '.join(queue_in_string)})"