# Read the number of elements in the initial set (not used, so stored in _)
_ = int(input())

# Read the set elements and store them in a set
s = set(map(int, input().split()))

# Read the number of commands to execute
commands = int(input())

# Loop through each command
for _ in range(commands):
    # Split the command into parts (e.g., "remove 3" → ["remove", "3"])
    command = input().split()

    # If the command has only one part, it's a method like 'pop'
    if len(command) == 1:
        # Dynamically call the method on the set (e.g., s.pop())
        getattr(s, command[0])()
    else:
        # For commands like 'remove 3' or 'discard 4',
        # call the method with an integer argument
        getattr(s, command[0])(int(command[1]))

# After executing all commands, print the sum of the remaining set elements
print(sum(s))
