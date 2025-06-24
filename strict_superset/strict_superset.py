# Read set A from input (space-separated integers)
A = set(map(int, input().split()))

# Read the number of sets B to compare against A
n = int(input())

# Assume A is a strict superset initially
strict_superset = True

# Loop through each of the n sets B
for _ in range(n):
    # Read set B from input
    B = set(map(int, input().split()))

    # Check if A is a strict superset of B
    # Condition 1: All elements of B must be in A
    # Condition 2: A and B must not be equal
    if not (all(element in A for element in B) and A != B):
        # If either condition fails, A is not a strict superset
        strict_superset = False

# Print the final result: True if A is a strict superset of all B sets,
# else False
print(strict_superset)


"""alternate with built-in function"""

# # Read the initial set A from input and convert elements to integers
# A = set(map(int, input().split()))

# # Read the number of sets to compare against A
# n = int(input())

# # Assume A is a strict superset unless proven otherwise
# strict_superset = True

# # Loop through each of the n sets
# for _ in range(n):
#     # Read set B and convert to a set of integers
#     B = set(map(int, input().split()))

#     # Check if A is NOT a strict superset of B
#     # A must contain all elements of B AND be different from B
#     if not (A.issuperset(B) and A != B):
#         # If condition fails for any B, set result to False and break loop
#         strict_superset = False
#         break

# # Output the result: True if A is a strict superset of all B sets,
# # otherwise False
# print(strict_superset)
