def main():

    n = int(input())
    list_of_integers = input().strip().split(" ")

    # Convert the list of strings to a tuple of integers
    t = tuple(int(integer) for integer in list_of_integers)

    # Using PyPy 3 is recommended for calculating the hash of a tuple due to differences in hash implementation.
    # With Python 3, the hash values can vary across different runs or versions of Python, leading to inconsistency.
    # PyPy 3 provides consistent hash results across different runs and is often faster in computing such tasks.

    print(hash(t))


if __name__ == "__main__":
    main()
