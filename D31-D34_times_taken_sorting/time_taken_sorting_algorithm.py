import csv
import time
import random
import logging

logging.basicConfig(filename="sorting_error.log", level=logging.ERROR)

def read_names_from_csv(file_path):

    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        return [row[0] for row in reader]

# Sorted
def sort(arr):
    arr.sort()
    return arr

# Bubble Sort
def bubble_sort(arr):

    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

# Selection Sort
def selection_sort(arr):

    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

# Insertion Sort
def insertion_sort(arr):

    n = len(arr)
    for i in range (1,n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    return arr

# Merge Sort
def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    middle_element = len(arr) // 2
    left_sort = arr[:middle_element]
    right_sort = arr[middle_element:]

    sorted_left = merge_sort(left_sort)
    sorted_right = merge_sort(right_sort)

    return mg_sorting(sorted_left,sorted_right)


def mg_sorting(left,right):

    final_arr = []
    i = j = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            final_arr.append(left[i])
            i += 1

        else:
            final_arr.append(right[j])
            j += 1

    final_arr.extend(left[i:])
    final_arr.extend(right[j:])

    return  final_arr
"========================================================================="
# Quick Sort

def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = random.choice(arr)

    left = [i for i in arr if i < pivot]
    right = [i for i in arr if i > pivot]
    middle = [i for i in arr if i == pivot]

    return quick_sort(left) + middle + quick_sort(right)


"""
def separate(arr,low,high):
    pivot = arr[high]
    i = low - 1
    for j in range (low,high):
        if arr[j] <= pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1

def quick_sort(arr,low = 0,high = None):
    if high is None:
        high = len(arr)-1

    if low < high:
        pivot_ind = separate(arr, low, high )
        quick_sort(arr,low,pivot_ind-1)
        quick_sort(arr,pivot_ind+1,high)

    return arr
"""

def main():
    #file_path = '5k_name_list.csv'
    file_path = '10_million_name_list.csv'

    names = read_names_from_csv(file_path)

    names_bubble = names.copy()
    names_selection = names.copy()
    names_insertion = names.copy()
    names_sort = names.copy()
    names_merge = names.copy()
    names_quick = names.copy()

    while True:

        print("Choose Your Option")
        print("1. Bubble Sorting\n2. Selection Sorting\n3. Insertion Sorting\n4. Sort\n5. Merge Sorting\n6. Quick Sorting\n7. Exit")

        choose = int(input("Enter the number: "))

        if choose == 1:

            start_time = time.time()
            bubble_sort(names_bubble)
            end_time = time.time()

            """print("All names sorted using Bubble Sort:")
            for name in names_bubble:
                print(name)"""

            time_diff = end_time - start_time

            if time_diff < 60:
                print(f"\nTime taken {len(names)} datas by Bubble Sort: {time_diff:.4f} seconds")
            else:
                time_min = time_diff / 60
                print(f"\nTime taken {len(names)} datas  by Bubble Sort: {time_min:.4f} minutes")

        elif choose == 2:

            start_time = time.time()
            selection_sort(names_selection)
            end_time = time.time()

            """print("\nAll names sorted using Selection Sort:")
            for name in names_selection:
                print(name)"""

            time_diff = end_time - start_time

            if time_diff < 60:
                print(f"\nTime taken {len(names)} datas by Selection Sort: {time_diff:.4f} seconds")
            else:
                time_min = time_diff / 60
                print(f"\nTime taken {len(names)} datas  by Selection Sort: {time_min:.4f} minutes")

        elif choose == 3:

            start_time = time.time()
            insertion_sort(names_insertion)
            end_time = time.time()

            print("\nAll names sorted using Insertion Sort:")
            for name in names_insertion:
                print(name)

            time_diff = end_time - start_time

            if time_diff < 60:
                print(f"\nTime taken {len(names)} datas  by Insertion Sort: {time_diff:.4f} seconds")
            else:
                time_min = time_diff / 60
                print(f"\nTime taken {len(names)} datas  by Insertion Sort: {time_min:.4f} minutes")

        elif choose == 4:

            start_time = time.time()
            sort(names_sort)
            end_time = time.time()

            """print("\nAll names sorted using Sort:")
            for name in names_sort:
                print(name)"""

            time_diff = end_time - start_time

            if time_diff < 60:
                print(f"\nTime taken {len(names)} datas  by Sort: {time_diff:.4f} seconds")
            else:
                time_min = time_diff / 60
                print(f"\nTime taken {len(names)} datas  by Sort: {time_min:.4f} minutes")


        elif choose == 5:

            start_time = time.time()
            names_merge = merge_sort(names_merge)
            end_time = time.time()

            """print("\nAll names sorted using Merge Sort:")
            for name in names_merge:
                print(name)"""

            time_diff = end_time - start_time

            if time_diff < 60:
                print(f"\nTime taken {len(names)} datas  by Merge Sort: {time_diff:.4f} seconds")
            else:
                time_min = time_diff / 60
                print(f"\nTime taken {len(names)} datas  by Merge Sort: {time_min:.4f} minutes")


        elif choose == 6:

            try:
                start_time = time.time()
                names_quick = quick_sort(names_quick)
                end_time = time.time()

                """print("\nAll names sorted using Quick Sort:")
                for name in names_quick:
                    print(name)"""

                time_diff = end_time - start_time

                if time_diff < 60:
                    print(f"\nTime taken {len(names)} datas by Quick Sort: {time_diff:.4f} seconds")
                else:
                    time_min = time_diff / 60
                    print(f"\nTime taken {len(names)} datas  by Quick Sort: {time_min:.4f} minutes")

            except RecursionError as e:
                logging.error(f"Error: {e}")
                print("error")


        elif choose == 7:
            print("Exiting...")
            return

        else:
            print("Please, enter a valid option")

if __name__ == '__main__':
    main()
