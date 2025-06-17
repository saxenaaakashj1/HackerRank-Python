import cmath  # Import the cmath module for complex number operations

# Read a complex number from input (e.g., "1+2j") and convert it to
# a complex type
z = complex(input())

# Print the magnitude (modulus) of the complex number sqrt(1^2 + 2^2)
print(abs(z))

# Print the phase (angle in radians) of the complex number
print(cmath.phase(z))
