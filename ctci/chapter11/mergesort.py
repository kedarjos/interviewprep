def mergeSort(arr):
    if(len(arr) > 1):
        mid = len(arr)//2

        leftarr = arr[:mid]
        rightarr = arr[mid:]

        mergeSort(leftarr)
        mergeSort(rightarr)

        i = j = k = 0

        while i < len(leftarr) and j < len(rightarr):
            if leftarr[i] <= rightarr[j]:
                arr[k] = leftarr[i]
                i += 1
            else:
                arr[k] = rightarr[j]
                j += 1
            k += 1

        while i < len(leftarr):
            arr[k] = leftarr[i]
            i += 1
            k += 1

        while j < len(rightarr):
            arr[k] = rightarr[j]
            j += 1
            k += 1

def printList(arr):
    i = 0
    length = len(arr)
    while i < length:
        print(arr[i], end=" ")
        i += 1

if __name__ == "__main__":
    arr = [4, 5, 3, 1, 16, 10]
    print("Before sort: ")
    printList(arr)
    mergeSort(arr)
    print()
    print("After sort: ")
    printList(arr)
