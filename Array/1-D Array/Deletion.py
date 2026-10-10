# All About Deleting an Array
def deleteBeginning(arr, n):
    for i in range(n - 1):
        arr[i] = arr[i + 1]
    return n - 1
def deletePosition(arr, n, pos):
    for i in range(pos - 1, n - 1):
        arr[i] = arr[i + 1]
    return n - 1
def deleteEnd(n):
    return n - 1
def display(arr, n):
    print("After Array:")
    for i in range(n):
        print(arr[i], end=" ")
    print()
arr = [0] * 100
n = int(input("Enter number of elements:"))
print("Enter elements:")
elements = list(map(int, input().split()))
for i in range(n):
    arr[i] = elements[i]

print("Before Array:")
for i in range(n):
    print(arr[i], end=" ")
print()

while True:
    print("\nMENU")
    print("1. Delete from Beginning")
    print("2. Delete from Position")
    print("3. Delete from End")
    print("4. Display Array")
    print("5. Exit")
    choice = int(input("Enter choice:"))
    if choice == 1:
        n = deleteBeginning(arr, n)
    elif choice == 2:
        pos = int(input("Enter position:"))
        n = deletePosition(arr, n, pos)
    elif choice == 3:
        n = deleteEnd(n)
    elif choice == 4:
        display(arr, n)
    elif choice == 5:
        break
    else:
        print("Invalid choice")