#Stack

class Stack:
    def __init__(self):
        self.elements=[]

    def push(self,data):
        self.elements.append(data)
        return data

    def pop(self):
        if self.is_empty():
            print('Stack is Empty.')
        else:
            print('Popped Value: ',self.elements[-1])
            self.elements.pop()

    def peek(self):
        return self.elements[len(self.elements)-1]

    def is_empty(self):
        return len(self.elements) == 0

stack = Stack()
print(stack.is_empty())
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
print(stack.is_empty())
print(stack.peek())
print(stack.peek())
stack.pop()
stack.pop() 
stack.pop() 
stack.pop() 
stack.pop() 
stack.pop() 
print(stack.is_empty())
