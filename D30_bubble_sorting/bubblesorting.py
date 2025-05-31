def bubble_sorting(arr):
    n = len(arr)
    for i in range (n):
        for j in range (n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

arr = [12,3,44,55,7,9,0]
print(bubble_sorting(arr))