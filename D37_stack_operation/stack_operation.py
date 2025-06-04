class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty!"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty!"

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        return self.stack[::-1]  # Top to bottom
s = Stack()
s.push(10)
s.push(20)
s.push(30)
