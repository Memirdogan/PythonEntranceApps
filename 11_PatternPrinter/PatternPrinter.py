def create_square(size):
    for i in range(size):
        for j in range(size):
            if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


def main():
    size = int(input("Desenin boyutunu girin: "))
    create_square(size)


if __name__ == "__main__":
    main()
