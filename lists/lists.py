def main():
    # Read the number of commands from user input
    N = int(input())

    # Define a list of valid commands
    dataset = ["insert", "remove", "append", "sort", "pop", "reverse", "print"]

    # Read and parse each command from user input
    commands = [
        [command[0], *[int(item) for item in command[1:]]]
        for command in (input().strip().split(" ") for _ in range(N))
    ]
    # Commands are converted to a list where command[0] is the command type and the rest are its arguments

    # Initialize an empty list to apply commands
    data = []

    # Process each command
    for command in commands:
        # Check if the command is valid
        if command[0] not in dataset:
            continue  # Skip invalid commands

        # Execute the appropriate operation based on the command type
        if command[0] == "insert":
            # Insert an element at the specified index
            data.insert(command[1], command[2])
        elif command[0] == "remove":
            # Remove the first occurrence of the specified element
            data.remove(command[1])
        elif command[0] == "append":
            # Append an element to the end of the list
            data.append(command[1])
        elif command[0] == "sort":
            # Sort the list in ascending order
            data.sort()
        elif command[0] == "pop":
            # Remove and return the last element of the list
            data.pop()
        elif command[0] == "reverse":
            # Reverse the order of elements in the list
            data.reverse()
        elif command[0] == "print":
            # Print the current state of the list
            print(data)

# Ensure that the main function runs only if this script is executed directly
if __name__ == "__main__":
    main()