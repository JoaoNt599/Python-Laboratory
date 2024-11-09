# linked list
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None 


    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        
        current = self.head

        while current.next:
            current = current.next
        current.next = None(data)


    def __str__(self):
        node = self.head

        while node is not None:
            print(node.data)
            node = node.next

    
    # linked list search
    def search(self, target):
        current = self.head

        while current.next:
            if current.data == target:
                return True
            else:
                current = current.next
            return False
        
    
    # remove linked list node
    def remove(self, target):
        if self.head == target:
            self.head = self.head.next
            return
        
        current = self.head
        previous = None

        while current:
            if current.data == target:
                previous.next = current.next
            previous = current
            current = current.next

    
    # reverse linked list
    def reverse_list(self):
        current = self.head
        previous = None

        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous


# example:
if __name__ =="__main__":
    a_list = LinkedList()
    a_list.append("Tuesday")
    a_list.append("Wednesday")
    print(a_list)



