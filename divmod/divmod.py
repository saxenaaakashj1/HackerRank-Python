a = int(input())  # Read the first integer (numerator)
b = int(input())  # Read the second integer (denominator)

# Print the result of integer division
print(a // b)  # This gives the quotient without the remainder

# Print the remainder of the division
print(a % b)  # This gives the remainder after dividing a by b

# Print a tuple containing both quotient and remainder
print(divmod(a, b))  # Equivalent to (a // b, a % b)
