class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            print("Queue is Empty")
            return
        temp = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        print("Dequeued:", temp.data)

    def display(self):
        if self.front is None:
            print("Queue is Empty")
            return
        temp = self.front
        while temp is not None:
            print(temp.data, end=" --> ")
            temp = temp.next
        print("NULL")

q = Queue()
while True:
    print("\n1. Enqueue (Add Car)")
    print("2. Dequeue (Remove Car)")
    print("3. Display Queue")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        val = input("Enter car name: ")  
        q.enqueue(val)
    elif choice == 2:
        q.dequeue()
    elif choice == 3:
        q.display()
    elif choice == 4:
        print("Exiting program...")
        break
    else:
        print("Invalid choice")
