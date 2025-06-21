a = int(input())  # Read base number 'a' as an integer
b = int(input())  # Read exponent 'b' as an integer
m = int(input())  # Read modulus 'm' as an integer

# Print a raised to the power of b (a^b)
print(pow(a, b))

# Print (a raised to the power of b) modulo m -> (a^b) % m
# This uses Python's built-in modular exponentiation, which is efficient
# for large numbers
print(pow(a, b, m))
