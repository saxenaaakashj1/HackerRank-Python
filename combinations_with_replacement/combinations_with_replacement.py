from itertools import combinations_with_replacement

# Take input: a string of characters and the combination length
n, r = input().split()

# Generate all possible combinations with replacement
# 1. Convert characters to uppercase
# 2. Sort them to ensure output is in lexicographic order
# 3. Use combinations_with_replacement to allow repeating elements
possible_combinations = list(
    combinations_with_replacement(
        sorted(n.upper()),  # Sort to guarantee lexicographic order
        int(r)              # Convert r to integer for combination length
    )
)

# Print each combination as a joined string
for combination in possible_combinations:
    print("".join(combination))