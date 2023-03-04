def binary_search(arr, low, high, x):
	if high >= low:
		mid = (high + low) // 2
		if arr[mid] == x:
			return mid
		elif arr[mid] > x:
			return binary_search(arr, low, mid - 1, x)
		else:
			return binary_search(arr, mid + 1, high, x)
	else:
		return -1

s=input("Enter elements of array: ")
arr = [int(i) for i in s.split(' ')]
x=int(input("Enter element to search for: "))

result = binary_search(arr, 0, len(arr)-1, x)

if result == -1:
	print("Element not found")
else:
	print("Element found at index: "+ str(result))
