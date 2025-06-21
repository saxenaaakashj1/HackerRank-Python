input()  # Read the number of students subscribed to the English newspaper
english = set(
    map(int, input().split())
)  # Read English subscribers' roll numbers and store them in a set

input()  # Read the number of students subscribed to the French newspaper
french = set(
    map(int, input().split())
)  # Read French subscribers' roll numbers and store them in a set

# Calculate the total unique students who subscribed to at least one newspaper
print(len(english | french))
