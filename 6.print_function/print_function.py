def main():
    n = int(input())
    if 1<=n<=150:
        print(*[i for i in range(1, n+1)], sep="")


if __name__ == "__main__":
    main()