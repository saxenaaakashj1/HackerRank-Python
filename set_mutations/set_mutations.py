# Read the size of the initial set A (not used, but required for input format)
int(input())

# Read elements of set A
A = set(map(int, input().split()))

# Read the number of set operations to perform
n = int(input())

# Perform each operation
for _ in range(n):
    # Read the command (e.g., 'update', 'intersection_update', etc.)
    command = input().split()

    # Read the other set B for the operation
    B = set(map(int, input().split()))

    # Use getattr to dynamically call the appropriate method on set A
    # command[0] contains the method name like 'update',
    # 'intersection_update', etc.
    getattr(A, command[0])(B)

# After all operations, print the sum of elements in set A
print(sum(A))
