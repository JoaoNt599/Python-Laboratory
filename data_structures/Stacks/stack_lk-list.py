#   simple stack using linked list
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    
class Stack:
    def __init__(self) -> None:
        self.head = None

        
    def push(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

        
    def pop(self):
        if self.head is None:
            raise IndexError('pop from empty stack')
        poppednode = self.head
        self.head = self.head.next
        return poppednode.data
    
        

# example:
if __name__ =="__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    for i in range(3):
        print(stack.pop())


