def main():
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

def print_full_name(first, last):
    # The message uses an f-string to format the output
    print(f"Hello {first} {last}! You just delved into python.")

if __name__ == "__main__":
    main()