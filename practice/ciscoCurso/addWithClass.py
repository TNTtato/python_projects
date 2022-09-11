class add2N:
    first = 0
    second = 0
    result = 0

    def __init__(self, f, s):
        self.first = f
        self.second = s

    def display(self):
        print('the first number: ', self.first)
        print('the second number: ', self.second)
        print('the result: ', self.result)

    def operation(self):
        self.result = self.first + self.second

obj1 = add2N(1000, 2000)
obj1.operation()
obj1.display()
