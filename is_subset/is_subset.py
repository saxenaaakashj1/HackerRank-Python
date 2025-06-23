# Read the number of test cases
test_cases = int(input())

# Loop through each test case
for _ in range(test_cases):
    # Read the size of the first set (not used directly)
    int(input())

    # Read elements of the first set A
    A = set(map(int, input().split()))

    # Read the size of the second set (not used directly)
    int(input())

    # Read elements of the second set B
    B = set(map(int, input().split()))

    # Assume A is a subset of B initially
    isSubset = True

    # Check if all elements of A are present in B
    for element in A:
        if element not in B:
            isSubset = False
            break  # Exit early if any element of A is not in B

    # Print the result: True if A is a subset of B, otherwise False
    print(isSubset)

"""with built-in function"""

# # Read the number of test cases
# test_cases = int(input())

# for _ in range(test_cases):
#     int(input())
#     A = set(map(int, input().split()))
#     int(input())
#     B = set(map(int, input().split()))

#     # Use built-in method to check if A is a subset of B
#     print(A.issubset(B))
