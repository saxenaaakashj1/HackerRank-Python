import re  # Import the regular expressions module

# Read the number of test cases from user input
test_cases = int(input())

# Read each test case input, remove leading/trailing spaces,
# and store in a list
numbers = [input().strip() for _ in range(test_cases)]

# Define a regular expression pattern to validate floating-point numbers
# The pattern allows:
#  - An optional '+' or '-' sign at the beginning
#  - Either:
#     a) One or more digits, a dot, and one or more digits
#        (e.g., 12.34, +0.56, -3.14)
#     b) Just a dot followed by one or more digits (e.g., .99, -.25, +.8)
pattern = r"^[+-]?((\d+\.\d+)|(\.\d+))$"

# Loop through each number and apply the regex match
for number in numbers:
    # If the number matches the float pattern, print True;
    # otherwise, print False
    if re.match(pattern, number):
        print(True)
    else:
        print(False)
