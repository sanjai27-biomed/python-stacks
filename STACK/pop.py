stack = [10,20,30,40,50,60,70,20]
if len(stack)==0:
    print("Stack Underflow")
else:
    removed=stack.pop()
    print("Popped element:",removed)
print("Stack After Pop:",stack)
