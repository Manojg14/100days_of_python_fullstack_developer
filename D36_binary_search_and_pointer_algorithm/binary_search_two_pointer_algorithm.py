import time

def binary_search(arr, left, right, target):
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def find_pair_with_binary_search(arr, target):
    for i in range(len(arr)):
        complement = target - arr[i]
        j = binary_search(arr, i + 1, len(arr) - 1, complement)
        if j != -1:
            return (i, j) 
    return None


arr = [1, 2, 4, 5, 7, 11, 15]
target = 17

start_time = time.time()

result = find_pair_with_binary_search(arr, target)

end_time = time.time()

if result:
    print(f"Index {result}, values: {arr[result[0]]}, {arr[result[1]]}")
else:
    print("No valid pair found.")

print(f"Time : {end_time - start_time} ")