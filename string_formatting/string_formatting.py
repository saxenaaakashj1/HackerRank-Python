def main():
    # Read an integer input from the user
    n = int(input())

    # Call the print_formatted function to format and print the numbers
    print_formatted(n)


def print_formatted(number):
    # Determine the width for formatting based on the length of the
    # binary representation of the largest number (i.e., 'number')
    width = len(bin(number)) - 2
    # Subtract 2 to remove the '0b' prefix from the binary
    # representation

    # Check if the number is within the valid range (1 to 99)
    if 1 <= number <= 99:
        # Loop from 1 to the given number, inclusive
        for i in range(1, number + 1):
            # First approach: Using string manipulation methods directly
            # Right-justify (rjust) each value (decimal, octal,
            # hexadecimal, binary) according to the width
            print(
                str(i).rjust(width),
                # Decimal representation of the number
                # (right-justified)
                oct(i)[2:].rjust(width),
                # Octal representation, remove '0o' prefix
                # (right-justified)
                hex(i)[2:].upper().rjust(width),
                # Hexadecimal representation, remove '0x', convert
                # to uppercase (right-justified)
                bin(i)[2:].rjust(width),
                # Binary representation, remove '0b' prefix
                # (right-justified)
            )

            # Second approach: Using the `format()` function for the
            # same result
            # `format()` is an alternative way to convert numbers into
            # different bases

            # print(
            #     str(i).rjust(width),
            ## Decimal representation (right-justified)
            #     format(i, "o").rjust(width),
            ## Octal representation using format() method
            ## (right-justified)
            #     format(i, "X").rjust(width),
            ## Hexadecimal (uppercase) using format() method
            ## (right-justified)
            #     format(i, "b").rjust(width)
            ## Binary representation using format() method
            ## (right-justified)
            # )


if __name__ == "__main__":
    # Call the main function to start the program
    main()
