def main():
    square(int(input()))


def square(n):
    if 1 <= n <= 20:
        #  * is used to unpack the list so that print can handle each item separately
        print(*[i**2 for i in range(n)], sep="\n")


if __name__ == "__main__":
    main()
