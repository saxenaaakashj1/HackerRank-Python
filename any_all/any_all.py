int(input())  # Read the number of elements (not used further in the code)
numbers = list(map(int, input().split()))  # Read the list of integers

# Check if all numbers are positive
if not all(number > 0 for number in numbers):
    print(False)
    exit()

# Loop through each number to check for palindromes
for number in numbers:
    n = number  # Create a copy of the number for manipulation
    rev = 0  # Initialize reversed number
    while n != 0:
        rem = n % 10  # Extract the last digit
        rev = rev * 10 + rem  # Append digit to the reversed number
        n //= 10  # Remove the last digit from the number
    if rev == number:  # If the number is a palindrome
        print(True)
        exit()

# If no palindromic number is found
print(False)
