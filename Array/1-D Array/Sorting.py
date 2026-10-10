def insertionSort(arr, n):
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
def bubbleSort(arr, n):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
def selectionSort(arr, n):
    for i in range(n - 1):
        minIndex = i
        for j in range(i + 1, n):
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
def quickSort(arr, low, high):
    if low < high:
        pivotIndex = partition(arr, low, high)
        quickSort(arr, low, pivotIndex - 1)
        quickSort(arr, pivotIndex + 1, high)
def merge(arr, low, mid, high):
    temp = []
    i = low
    j = mid + 1
    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
    while i <= mid:
        temp.append(arr[i])
        i += 1

    while j <= high:
        temp.append(arr[j])
        j += 1

    for k in range(len(temp)):
        arr[low + k] = temp[k]
def mergeSort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        mergeSort(arr, low, mid)
        mergeSort(arr, mid + 1, high)
        merge(arr, low, mid, high)
def display(arr):
    print("Sorted Array:")
    for x in arr:
        print(x, end=" ")
    print()
n = int(input("Enter the size of array:"))
print(f"Enter {n} elements:")
arr = list(map(int, input().split()))
while True:
    print("\n1. Insertion Sort")
    print("2. Bubble Sort")
    print("3. Selection Sort")
    print("4. Quick Sort")
    print("5. Merge Sort")
    print("6. Exit")
    choice = int(input("Enter choice: "))
    temp = arr.copy()
    if choice == 1:
        insertionSort(temp, n)
        display(temp)
    elif choice == 2:
        bubbleSort(temp, n)
        display(temp)
    elif choice == 3:
        selectionSort(temp, n)
        display(temp)
    elif choice == 4:
        quickSort(temp, 0, n - 1)
        display(temp)
    elif choice == 5:
        mergeSort(temp, 0, n - 1)
        display(temp)
    elif choice == 6:
        break
    else:
        print("Invalid choice")