input()  # Read the number of students subscribed to the English newspaper
english = set(
    map(int, input().split())
)  # Read English subscribers' roll numbers and store them in a set

input()  # Read the number of students subscribed to the French newspaper
french = set(
    map(int, input().split())
)  # Read French subscribers' roll numbers and store them in a set

# Calculate the total number of unique students who subscribed to both
# newspapers
print(len(english & french))
