# minimum stack
class MinStack():
    def __init__(self) -> None:
        self.main = []
        self.min = []


    def push(self, n):
        if len(self.main) == 0:
            self.min.append(n)
        elif n <= self.min[-1]:
            self.min.append(n)
        else:
            self.min.append(self.min[-1])
        self.main.append(n)
    

    def pop(self):
        self.min.pop()
        return self.main.pop()
    

    def get_min(self):
        return self.min[-1]
    


# example:
if __name__ =="__main__":
    min_stack = MinStack()
    min_stack.push(10)
    print(min_stack.main)
    print(min_stack.min)