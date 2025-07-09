import re  # Import the 're' module

# Define a regular expression pattern that matches either a
# comma ',' or a period '.'
regex_pattern = r"[.,]"

# Take input from the user and split the string wherever a comma or
# period occurs
# Then join the resulting list of strings with newline characters and
# print each part on a new line
print("\n".join(re.split(regex_pattern, input())))
