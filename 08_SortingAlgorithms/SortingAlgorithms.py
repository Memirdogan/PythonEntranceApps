
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        idx_min = i
        for j in range(i+1, n):
            if arr[j] < arr[idx_min]:
                idx_min = j
        arr[i], arr[idx_min] = arr[idx_min], arr[i]
    return arr

