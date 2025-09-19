class Queue:
    def __init__(self):
        self.queue = []
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1 or self.front > self.rear

    def enqueue(self, val):
        if self.is_empty():
            self.front = 0
            self.rear = 0
            self.queue = [val]
        else:
            self.rear += 1
            self.queue.append(val)
        print(f"{val} added to the queue")

    def dequeue(self):
        if self.is_empty():
            print("Queue is EMPTY! Deletion not possible")
            return
        print(f"{self.queue[self.front]} removed from the queue")
        self.front += 1
        if self.front > self.rear:
            # Reset queue
            self.front = -1
            self.rear = -1
            self.queue = []

    def show(self):
        if self.is_empty():
            print("Queue is EMPTY!!!")
        else:
            print("Queue elements are:", end=" ")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()


def main():
    q = Queue()
    while True:
        print("\n1. Enqueue (Add Car)")
        print("2. Dequeue (Remove Car)")
        print("3. Show Queue")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            val = input("Enter car name to insert: ")
            q.enqueue(val)
        elif choice == 2:
            q.dequeue()
        elif choice == 3:
            q.show()
        elif choice == 4:
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
