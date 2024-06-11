class Queue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return len(self.elements) == 0
    
    def insert(self, new_element):
        self.elements.append(new_element)

    def pop(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        
        return self.elements.pop(0)

q = Queue()
q.insert(23)
q.insert(765)
q.insert(3)

print(q.pop())
print("Left in Queue:", q.elements)
