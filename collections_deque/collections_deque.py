from collections import deque  # Import deque from collections module

n = int(input())  # Read the number of commands
d = deque()  # Create an empty deque

# Process each command
for _ in range(n):
    command = (
        input().split()
    )  # Split the input into command and optional argument

    if len(command) == 1:
        # If it's a method with no argument (like pop)
        getattr(d, command[0])()  # Dynamically call d.pop() etc.
    else:
        # If it's a method with one argument (like append)
        getattr(d, command[0])(
            int(command[1])
        )  # Call method with int argument

# Print all elements in the deque in a single line
for element in d:
    print(element, end=" ")
