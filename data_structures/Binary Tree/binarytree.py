class BinaryTree:

    def __init__(self, value):
        self.key = value
        self.left_child = None
        self.right_child = None


    def insert_left(self, value):
        if self.left_child == None:
            self.left_child = BinaryTree(value)
        else:
            bin_tree = BinaryTree(value)
            bin_tree.left_child = self.left_child
            self.left_child = bin_tree
    

    def insert_right(self, value):
        if self.right_child == None:
            self.right_child = BinaryTree(value)
        else:
            bin_tree = BinaryTree(value)
            bin_tree.right_child = self.right_child
            self.right_child = bin_tree
    

    def breadth_first_search(self, n):
        current = [self]
        next = []
        while current:
            for node in current:
                if node.key == n:
                    return True
                if node.left_child:
                    next.append(node.left_child)
                if node.right_child:
                    next.append(node.right_child)
            current = next
            next = []
        return False


    def preorder(self):
        if self:
            print(self.key)
            if self.left_child:
                self.left_child.preorder()
            if self.right_child:
                self.right_child.preorder()
    

    def postorder(self):
        if self:
            if self.left_child:
                self.left_child.postorder()
            if self.right_child:
                self.right_child.postorder()
            print(self.key)
    

    def inorder(self):
        if self:
            if self.left_child:
                self.left_child.inorder()
            print(self.key)
            if self.right_child:
                self.right_child.inorder()
      

    def invert(self):
        current = [self]
        next = []
        while current:
            for node in current:
                if node.left_child:
                    next.append(node.left_child)
                if node.right_child:
                    next.append(node.right_child)
                tmp = node.left_child
                node.left_child = node.right_child
                node.right_child = node.left_child
            current = next
            next = []



if __name__ == "__main__":
    tree = BinaryTree(1)
    tree.insert_left(2)
    tree.insert_right(3)
    tree.insert_left(4)
    tree.left_child.insert_right(6)
    tree.insert_right(5)


    print("Pre-order:")
    tree.preorder()


    print("Post-order:")
    tree.postorder()


    print("In-order:")
    tree.inorder()


    print("Before inversion:")
    tree.inorder()
    tree.invert()
    print("After inversion:")
    tree.inorder()


    result = tree.breadth_first_search(5)
    if result:
        print("Value 5 found in the tree.")
    else:
        print("Value 5 not found in tree.")

    
