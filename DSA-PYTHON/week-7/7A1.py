# Queue implementation using Array

queue = []
MAX = 5

def enqueue():
    if len(queue) == MAX:
        print("Queue Overflow")
    else:
        value = int(input("Enter element: "))
        queue.append(value)
        print("Element inserted")


def dequeue():
    if len(queue) == 0:
        print("Queue Underflow")
    else:
        print("Deleted element:", queue.pop(0))


def peek():
    if len(queue) == 0:
        print("Queue is empty")
    else:
        print("Front element:", queue[0])


def display():
    if len(queue) == 0:
        print("Queue is empty")
    else:
        print("Queue elements:")
        for element in queue:
            print(element, end=" ")
        print()


while True:
    print("\n----- QUEUE MENU -----")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        peek()
    elif choice == 4:
        display()
    elif choice == 5:
        print("Program terminated")
        break
    else:
        print("Invalid choice")
