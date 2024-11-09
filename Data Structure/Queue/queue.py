class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next

    

class Queue:
    def __init__(self) -> None:
        self.front = None
        self.rear = None
        self._size = 0


    def enqueue(self, item):
        self._size += 1
        node = Node(item)

        if self.rear is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node
        

    def dequeue(self):
        if self.front is None:
            raise IndexError('pop from empty queue')
        
        self._size -= 1
        temp = self.front
        self.front = self.front.next

        if self.front is None:
            self.rear = None
        return temp.data
    

    def size(self):
        return self._size
    
# example
if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.size())
    for i in range(3):
        print(queue.dequeue())