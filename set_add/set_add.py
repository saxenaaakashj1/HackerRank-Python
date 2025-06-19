# Read the total number of country stamp entries
n = int(input())

# Initialize an empty set to store unique country names
country_stamps = set()

# Read each country name and add it to the set
for _ in range(n):
    country = input()
    country_stamps.add(country)  # Sets automatically ignore duplicates

# Print the total number of unique country stamps
print(len(country_stamps))
