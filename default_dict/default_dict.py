from collections import defaultdict

# Read two integers:
# n = number of words in group A
# m = number of query words in group B
n, m = map(int, input().split())

# Initialize a defaultdict where each key maps to a list
# This will store each word from group A and all its 1-based indices
word_indices = defaultdict(list)

# Read each word from group A and store its position (1-based) in the
# defaultdict
for index in range(1, n + 1):
    word = input()
    word_indices[word].append(index)

# Read all query words (group B) and store them in a list
words = list()
for _ in range(m):
    words.append(input())

# For each query word:
for word in words:
    if word in word_indices:
        # If the word exists in group A, print all its positions 
        # separated by spaces
        print(" ".join(map(str, word_indices[word])))
    else:
        # If not found, print -1
        print("-1")
