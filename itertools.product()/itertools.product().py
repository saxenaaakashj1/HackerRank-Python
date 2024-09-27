# Importing product from itertools to compute Cartesian product
from itertools import product


def main():
    # Read two lines of input, each split into a list of strings
    A = input().split()
    B = input().split()

    # Call the function to compute the Cartesian product of A and B
    cartesian_product(A, B)


def cartesian_product(A, B):
    # Check if both lists have lengths greater than 0 and less than 30
    if 0 < len(A) < 30 and 0 < len(B) < 30:
        # Convert the string lists A and B into integers using map
        A = map(int, A)
        B = map(int, B)
        # Compute and print the Cartesian product of A and B, unpacking
        # the result with *
        print(*product(A, B))


if __name__ == "__main__":
    main()  # Entry point to execute the main function
