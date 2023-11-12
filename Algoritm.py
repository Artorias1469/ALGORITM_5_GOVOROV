import random
import time
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
def reverse_bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
sizes = [1000, 2000, 3000, 4000, 5000]
print("Arr size\ttime (average)\t        time (worst)")
for size in sizes:
    arr = [random.randint(0, 999) for _ in range(size)]
    for _ in range(30):
        start = time.time()
        for _ in range(1):
            bubble_sort(arr.copy())
        end = time.time()
        time_average = end - start
        start = time.time()
        for _ in range(1):
            reverse_bubble_sort(arr.copy())
        end = time.time()
        time_worst = end - start
        print(f"{size}\t\t{time_average:.6f} sec\t\t{time_worst:.6f} sec")