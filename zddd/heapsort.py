import datetime
import random

# heap sort
# techno-384@techno384-Latitude-3410:~/Documents/git/assesmentRepo/zddd$ python3 heapsort.py
# 2025-12-27 21:39:53.644001
# 2025-12-27 21:39:57.513645
# 0:00:03.869644
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        print("n = ",n, "i = ",i, "n//2-1 = ", n//2-1)
        heapify(arr, n, i)

    #Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)


# Example usage
#arr = [random.randint(1, 100) for _ in range(1000000)]
arr = [3, 2, 6, 5, 1, 9, 6, 7]
bt=datetime.datetime.now()
print(bt)
heap_sort(arr)
at=datetime.datetime.now()
print(at)
print(at-bt)
print(arr)
