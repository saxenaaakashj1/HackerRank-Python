# Read the number of test cases
test_cases = int(input())

# Iterate through each test case
for _ in range(test_cases):
    try:
        # Try to read two integers a and b
        a, b = map(int, input().split())

        # Print the result of integer division
        print(a // b)

    # Handle division by zero
    except ZeroDivisionError as e:
        print(f"Error Code: {e}")

    # Handle non-integer inputs or incorrect format
    except ValueError as e:
        print(f"Error Code: {e}")