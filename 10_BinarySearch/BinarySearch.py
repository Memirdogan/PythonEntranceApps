def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == target:
            return mid
        elif guess < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# tests

arr = [2, 4, 7, 10, 13, 18, 22, 27, 31]
target = 18

result = binary_search(arr, target)
if result != -1:
    print(f"{target} bulundu indeks: {result}")
else:
    print(f"{target} bulunamadı")

target = 10
result = binary_search(arr, target)
if result != -1:
    print(f"{target} bulundu indeks: {result}")
else:
    print(f"{target} bulunamadı")

target = 20
result = binary_search(arr, target)
if result != -1:
    print(f"{target} bulundu indeks: {result}")
else:
    print(f"{target} bulunamadı")

target = 2
result = binary_search(arr, target)
if result != -1:
    print(f"{target} bulundu indeks: {result}")
else:
    print(f"{target} bulunamadı")

target = 31
result = binary_search(arr, target)
if result != -1:
    print(f"{target} bulundu indeks: {result}")
else:
    print(f"{target} bulunamadı")
