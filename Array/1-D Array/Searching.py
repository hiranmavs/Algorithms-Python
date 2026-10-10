# Searching Algorithms
def linearSearch(arr, n, key):
    for i in range(n):
        if arr[i] == key:
            return i
    return -1
def binarySearch(arr, n, key):
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif key < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1
n = int(input("Enter the size of array:"))
print(f"Enter {n} elements:")
arr = list(map(int, input().split()))
while True:
    print("\n1. Linear Search")
    print("2. Binary Search")
    print("3. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        key = int(input("Enter element to search: "))
        pos = linearSearch(arr, n, key)

        if pos == -1:
            print("Element not found.")
        else:
            print(f"Element found at position {pos + 1}.")

    elif choice == 2:
        key = int(input("Enter element to search: "))
        pos = binarySearch(arr, n, key)

        if pos == -1:
            print("Element not found.")
        else:
            print(f"Element found at position {pos + 1}.")

    elif choice == 3:
        break

    else:
        print("Invalid choice")