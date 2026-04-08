queue=[]

while True:
    print("\nQueue operation menu")
    print("1.Enqueue")
    print("2.Dequeue")
    print("3.Front")
    print("4.Rear")
    print("5.isEmpty")
    print("6.Display")
    print("7.Exit")

    choice=int(input("Enter choice:"))
    if choice==1:
        val = int(input("enter a value:"))
        queue.append(val)
        print("Enqueued:",val)
    elif choice==2:
        if len(queue)==0:
            print("Queue underflow")
        else:
            print("Dequeued:",queue.pop(0))
    elif choice==3:
        if len(queue)==0:
            print("Queue is empty")
        else:
            print("Front elements:", queue[0])
    elif choice==4:
        if len(queue)==0:
            print("Queue is empty")
        else:
            print("Rear element:", queue[-1])
    elif choice==5:
        print("Is queue empty?",len(queue)==0)
    elif choice==6:
        print("Queue:",queue)
    elif choice==7:
        break
    else:
        print("Invalid choice")