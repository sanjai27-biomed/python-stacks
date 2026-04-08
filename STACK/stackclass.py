class Stack:
    def __init__(self,size):
        self.size=size
        self.stack=[]
    
    def push(self,value):
        if len(self.stack)==self.size:
            print("Stack overflow")
        else:
            self.stack.append(value)
            print(value,"pushed")
            
    def pop(self):
        if len(self.stack)==0:
            print("Stack underflow")
        else:
            print(self.stack.pop(),"popped")
    
    def peek(self):
        if len(self.stack)==0:
            print("Stack is empty")
        else:
            print("Top:",self.stack[-1])

    def isEmpty(self):
        return len(self.stack)==self.size
    
    def isFull(self):
        return len(self.stack)==self.size
    
    def display(self):
        print("Stack:",self.stack)

s=Stack(3)

s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(40)

s.display()
s.pop()
s.peek()
print("empty?",s.isEmpty())
print("Full?",s.isFull())