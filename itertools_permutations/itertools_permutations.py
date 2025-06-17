from itertools import permutations  # Import the permutations function

# Take input: a string and a number separated by space
s, r = input().split()

# Convert string to uppercase and generate all permutations of length r
# Wrap in list so we can sort it later
possible_permutations = list(permutations(s.upper(), int(r)))

# Sort permutations in lexicographic order and print them
for permutation in sorted(possible_permutations):
    print("".join(permutation))  # Join tuple into a string