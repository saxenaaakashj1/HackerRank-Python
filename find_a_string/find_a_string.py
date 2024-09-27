def main():
    # Read the input string and the substring to search for, stripping any
    # leading/trailing whitespace.
    string = input().strip()
    sub_string = input().strip()

    # Call the count_substring function if the string length is within
    # the specified range.
    # The result is printed only if the string's length is between 1
    # and 200 inclusive.
    (
        print(count_substring(string, sub_string))
        if 1 <= len(string) <= 200
        else None
    )


def count_substring(string, sub_string):
    count = 0  # Initialize a counter to track the number of occurrences
    start = 0  # Initialize the starting index for searching

    while True:
        # Find the first occurrence of the substring starting from the
        # current 'start' index
        start = string.find(sub_string, start)

        # If no more occurrences are found, break the loop
        if start == -1:
            break

        # Increment the count for each found occurrence
        count += 1

        # Move the start index by 1 to allow for overlapping occurrences
        start += 1

    return count  # Return the total count of overlapping occurrences


if __name__ == "__main__":
    # Run the main function if this script is executed
    main()
