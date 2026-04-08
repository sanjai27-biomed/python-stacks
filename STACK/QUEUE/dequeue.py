queue=[10,20,30]
if len(queue)==0:
    print("Queue Underflow! cannot dequeue")
else:
    removed=queue.pop(0)
    print("Dequeued Element:",removed)

print("Queue after dequeue:", queue)