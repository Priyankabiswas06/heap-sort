def heapify(arr, n, i, max_heap=True):
    if max_heap:
        # Max heapify
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[i] < arr[left]:
            largest = left

        if right < n and arr[largest] < arr[right]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest, max_heap)
    else:
        # Min heapify
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[i] > arr[left]:
            smallest = left

        if right < n and arr[smallest] > arr[right]:
            smallest = right

        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            heapify(arr, n, smallest, max_heap)

def heap_sort(arr, max_heap=True):
    n = len(arr)

    # Build heap (rearrange array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, max_heap)

    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0, max_heap)

arr = [12, 11, 13, 5, 6, 7]

# Sort using max heap
heap_sort(arr, max_heap=True)
print("Sorted array using max heap is:", arr)

# Sort using min heap
heap_sort(arr, max_heap=False)
print("Sorted array using min heap is:", arr)
