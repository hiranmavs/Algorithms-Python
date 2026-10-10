# Creating an Array Without Uisng in-Built Data Structures like
# Tuple,List,Set & Dictionary

# Initiatize The Array
n = 0
arr = [0] * 100
def createArray(): # Using Create Array Function
    global n
    n = int(input("Enter size of array:"))
    print("Enter elements:")
    elements = list(map(int, input().split()))
    for i in range(n):
        arr[i] = elements[i]
def displayArray(): # Display The Array
    print("Array Elements:", end=" ")
    for i in range(n):
        print(arr[i], end=" ")
    print()
def insertElement(): # Inserting an element inside the Array
    global n
    pos, value = map(int, input("Enter position and value:").split())
    for i in range(n - 1, pos - 2, -1):
        arr[i + 1] = arr[i]
    arr[pos - 1] = value
    n += 1
    displayArray()
def deleteElement(): # Deleting an element from the existing Array
    global n
    pos = int(input("Enter position to delete:"))
    for i in range(pos - 1, n - 1):
        arr[i] = arr[i + 1]
    n -= 1
    displayArray()
def linearSearch(): # Searching The Array one-by-one
    key = int(input("Enter element to search:"))
    for i in range(n):
        if arr[i] == key:
            print(f"Element found at position {i + 1}")
            return
    print("Element not found")
def binarySearch(): # Searching the Array using a Equation
    key = int(input("Enter element to search:"))
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            print(f"Element found at position {mid + 1}")
            return
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    print("Element not found")
# Sorting an array 
def bubbleSort(): 
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    displayArray()
def selectionSort():
    for i in range(n - 1):
        minimum = i
        for j in range(i + 1, n):
            if arr[j] < arr[minimum]:
                minimum = j
        arr[i], arr[minimum] = arr[minimum], arr[i]
    displayArray()
def insertionSort():
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    displayArray()
# Sorting Ended
def reverseArray(): # Recverse The Array
    for i in range(n // 2):
        arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
    displayArray()
def largestSmallest(): # Largest & Smallest Element in the Array
    largest = arr[0]
    smallest = arr[0]
    for i in range(1, n):
        if arr[i] > largest:
            largest = arr[i]
        if arr[i] < smallest:
            smallest = arr[i]
    print("Largest =", largest)
    print("Smallest =", smallest)
def countEvenOdd(): # Counting Even & Odd
    even = 0
    odd = 0
    for i in range(n):
        if arr[i] % 2 == 0:
            even += 1
        else:
            odd += 1
    print("Even =", even)
    print("Odd =", odd)
def frequencyCount(): # Counting The Frequency of How Many Times The Array Occured
    for i in range(n):
        count = 1
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                count += 1
        print(arr[i], "occurs", count, "times")
# Rotating The Array LEft & Right 
def leftRotate():
    first = arr[0]
    for i in range(n - 1):
        arr[i] = arr[i + 1]
    arr[n - 1] = first
    displayArray()
def rightRotate():
    last = arr[n - 1]
    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]
    arr[0] = last
    displayArray()
def mergeArrays(): # Merging Two Arrays
    m = int(input("Enter size of second array:"))
    print("Enter elements:")
    b = list(map(int, input().split()))
    c = []
    for i in range(n):
        c.append(arr[i])
    for i in range(m):
        c.append(b[i])
    print("Merged Array:")
    for x in c:
        print(x, end=" ")
    print()
def removeDuplicates(): # Removing Duplicate Elements
    global n
    i = 0
    while i < n:
        j = i + 1
        while j < n:
            if arr[i] == arr[j]:
                for k in range(j, n - 1):
                    arr[k] = arr[k + 1]
                n -= 1
            else:
                j += 1
        i += 1
    displayArray()
createArray()
while True:
    print("1. Display Array")
    print("2. Insert Element")
    print("3. Delete Element")
    print("4. Linear Search")
    print("5. Binary Search")
    print("6. Bubble Sort")
    print("7. Selection Sort")
    print("8. Insertion Sort")
    print("9. Reverse Array")
    print("10. Largest & Smallest")
    print("11. Count Even/Odd")
    print("12. Frequency Count")
    print("13. Left Rotation")
    print("14. Right Rotation")
    print("15. Merge Two Arrays")
    print("16. Remove Duplicates")
    print("17. Exit")
    choice = int(input("Enter choice:"))
    if choice == 1:
        displayArray()
    elif choice == 2:
        insertElement()
    elif choice == 3:
        deleteElement()
    elif choice == 4:
        linearSearch()
    elif choice == 5:
        binarySearch()
    elif choice == 6:
        bubbleSort()
    elif choice == 7:
        selectionSort()
    elif choice == 8:
        insertionSort()
    elif choice == 9:
        reverseArray()
    elif choice == 10:
        largestSmallest()
    elif choice == 11:
        countEvenOdd()
    elif choice == 12:
        frequencyCount()
    elif choice == 13:
        leftRotate()
    elif choice == 14:
        rightRotate()
    elif choice == 15:
        mergeArrays()
    elif choice == 16:
        removeDuplicates()
    elif choice == 17:
        print("Program Ended")
        break
    else:
        print("Invalid Choice")