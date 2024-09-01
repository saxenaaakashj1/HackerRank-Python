def main():
    n = int(input().strip())
    if n % 2 == 0 and n in range(2, 6):
        print("Not Weird")
    elif n % 2 == 0 and n in range(6, 21):
        print("Weird")
    elif n % 2 == 0 and n in range(20, 101):
        print("Not Weird")
    else:
        print("Weird")


if __name__ == "__main__":
    main()