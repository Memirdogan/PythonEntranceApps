def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        idx_min = i
        for j in range(i + 1, n):
            if arr[j] < arr[idx_min]:
                idx_min = j
        arr[i], arr[idx_min] = arr[idx_min], arr[i]
    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def main():
    print("Sıralama Algoritmaları")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Insertion Sort")

    choice = int(input("Hangi sıralama algoritmasını kullanmak istiyorsunuz? (1-3): "))
    arr = list(map(int, input("Sıralamak istediğiniz elemanları aralarında boşluk bırakarak giriniz: ").split()))

    if choice == 1:
        sorted_arr = bubble_sort(arr)
    elif choice == 2:
        sorted_arr = selection_sort(arr)
    elif choice == 3:
        sorted_arr = insertion_sort(arr)
    else:
        print("Geçersiz seçim")
        return

    print("Sıralanmış dizi:", sorted_arr)

if __name__ == "__main__":
    main()