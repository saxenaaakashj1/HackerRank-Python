from collections import (
    Counter,
)  # Import Counter to count occurrences of each room number

# Read the size of each group (K) — not used here but relevant for the
# problem context
size = int(input())

# Read all room numbers as strings, count their occurrences using Counter
rooms = Counter(input().split())

# Iterate through the counted room numbers
for room in rooms:
    # If a room appears only once, it's the Captain's room
    if rooms[room] == 1:
        print(room)


"""Alternate Solution - More efficient and optimized"""

# # Read the group size K (number of family members per group)
# k = int(input())

# # Read the list of room numbers (each family room appears K times, 
# # captain's room appears once)
# rooms = list(map(int, input().split()))

# # Calculate the sum of unique room numbers (includes captain's room 
# # and each family room once)
# unique_sum = sum(set(rooms))

# # Calculate the total sum of all room numbers (includes repeated family 
# # rooms + captain's room once)
# total_sum = sum(rooms)

# # Use the mathematical trick to find the captain's room number
# # (K * unique_sum - total_sum) // (K - 1) 
# captain_room = (k * unique_sum - total_sum) // (k - 1)

# # Print the captain's room number
# print(captain_room)
