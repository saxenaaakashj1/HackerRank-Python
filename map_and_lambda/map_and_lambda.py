# Entry point function: starts the program
def main():
    # Prompt the user to enter how many Fibonacci numbers to generate
    n = int(input("Enter the number of Fibonacci terms: "))

    # Generate the Fibonacci sequence up to n terms
    # Apply the cube function to each term
    # Convert the result to a list and print it
    print(list(map(cube, fibonacci(n))))


# Lambda function to compute the cube of a number
# Equivalent to: def cube(x): return x ** 3
cube = lambda x: x**3


# Function to generate a list of the first 'n' Fibonacci numbers
def fibonacci(n):
    # Handle edge case: non-positive input
    if n <= 0:
        return []

    # If n is 1, return only the first Fibonacci number
    elif n == 1:
        return [0]

    # If n is 2, return the first two Fibonacci numbers
    elif n == 2:
        return [0, 1]

    # For n > 2, build the Fibonacci sequence iteratively
    fib = [0, 1]  # Start with the first two numbers

    # Loop to compute the rest of the sequence
    for _ in range(2, n):
        # Each number is the sum of the two preceding numbers
        fib.append(fib[-1] + fib[-2])

    return fib


if __name__ == "__main__":
    main()
