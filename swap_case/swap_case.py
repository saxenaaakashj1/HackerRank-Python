def main():
    # Read input from the user and print the result of swap_case function
    print(swap_case(input("String: ")))

def swap_case(s):
    # Create a new string where each character's case is swapped
    # List comprehension iterates through each character in the input string
    # Convert uppercase to lowercase and vice versa
    return "".join([ch.lower() if ch.isupper() else ch.upper() for ch in s])

if __name__ == "__main__":
    main()

# Note: This case swapping can be done in a single step using the built-in string method swapcase()
# Example: result = input("String: ").swapcase()