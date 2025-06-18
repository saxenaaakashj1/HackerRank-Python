# Read number of elements in the first set (not directly used)
m = int(input())
# Read elements of the first set
M = set(map(int, input().split()))

# Read number of elements in the second set (not directly used)
n = int(input())
# Read elements of the second set
N = set(map(int, input().split()))

# Compute symmetric difference: elements in either M or N, but not both
result = M ^ N  # equivalent to M.symmetric_difference(N)

# Print the symmetric difference in sorted order
for item in sorted(result):
    print(item)
