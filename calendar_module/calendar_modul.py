import calendar  # Import the built-in calendar module

# Take input from the user in the format MM DD YYYY, split it, 
# and convert each to an integer
month, date, year = map(int, input().split())

# Get the index of the weekday (0 = Monday, 6 = Sunday) using 
# calendar.weekday
weekday_index = calendar.weekday(year, month, date)

# Get the name of the day from calendar.day_name using the index, 
# then convert it to uppercase
day_name = calendar.day_name[weekday_index].upper()

# Print the final result
print(day_name)
