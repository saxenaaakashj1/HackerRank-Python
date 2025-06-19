from itertools import combinations

# Read input: a string and an integer r
string, size = input().split()

# List to store all possible combinations upto to size 'size'
possible_combinations = []

# Generate combinations of length 1 to size using sorted characters
# for lexicographic order
for i in range(1, int(size) + 1):
    possible_combinations.append(list(combinations(sorted(string.upper()), i)))

# Print each combination, one per line
for combination in possible_combinations:
    for letter in combination:
        print("".join(letter))
