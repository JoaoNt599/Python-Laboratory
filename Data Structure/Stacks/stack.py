# simple stack
class Stack:
    def __init__(self):
        self.items = []


    def push(self, data):
        self.items.append(data)


    def pop(self):
        return self.items.pop()
    

    def size(self):
        return len(self.items)
    

    def is_empty(self):
        return len(self.items) == 0
    

    def peek(self):
        return self.items[-1]