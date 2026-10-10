# All About Insertion an Array
def insertBeginning(arr, n, value):
    for i in range(n):
        for i in range(n - 1, -1, -1):
            arr[i + 1] = arr[i]
    arr[0] = value
    return n + 1
def insertPosition(arr, n, pos, value):
    for i in range(n, pos - 1, -1):
        arr[i] = arr[i - 1]
    arr[pos - 1] = value
    return n + 1
def insertEnd(arr, n, value):
    arr[n] = value
    return n + 1
def display(arr, n):
    print("After Array:")
    for i in range(n):
        print(arr[i], end=" ")
    print()
arr = [0] * 100
n = int(input("Enter number of elements:"))
print("Enter", n, "elements:")
for i in range(n):
    arr[i] = int(input())
print("Before Array:")
for i in range(n):
    print(arr[i], end=" ")
print()
while True:
    print("\nMENU")
    print("1. Insert at Beginning")
    print("2. Insert at Position")
    print("3. Insert at End")
    print("4. Display Array")
    print("5. Exit")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        value = int(input("Enter value:"))
        n = insertBeginning(arr, n, value)
    elif choice == 2:
        pos = int(input("Enter position:"))
        value = int(input("Enter value:"))
        n = insertPosition(arr, n, pos, value)
    elif choice == 3:
        value = int(input("Enter value:"))
        n = insertEnd(arr, n, value)
    elif choice == 4:
        display(arr, n)
    elif choice == 5:
        break
    else:
        print("Invalid choice")