input()  # Read the number of students subscribed to the English newspaper
english = set(
    map(int, input().split())
)  # Read roll numbers of English newspaper subscribers

input()  # Read the number of students subscribed to the French newspaper
french = set(
    map(int, input().split())
)  # Read roll numbers of French newspaper subscribers

# Calculate the number of students who subscribed to only one newspaper
# (either English or French, but not both)
print(len(english ^ french))
