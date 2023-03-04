def bubbleSort(arr):
    n = len(arr)
    check = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                check = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not check:
            return
s=input("Enter elements:")
arr = [int(i) for i in s.split(' ')]
bubbleSort(arr)
print("Sorted")
print(arr)