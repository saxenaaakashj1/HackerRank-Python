def main():
    # Read the integer values for x, y, z, and n from user input
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    # Use list comprehension to generate all possible coordinates [i, j, k]
    # where i ranges from 0 to x, j ranges from 0 to y, and k ranges from 0 to z.
    # Filter out the coordinates where the sum of i, j, and k equals n.
    result = [
        [i, j, k]
        for i in range(0, x + 1)
        for j in range(0, y + 1)
        for k in range(0, z + 1)
        if i + j + k != n
    ]

    # Print the resulting list of coordinates that meet the condition
    print(result)


# Entry point of the program
if __name__ == "__main__":
    main()
