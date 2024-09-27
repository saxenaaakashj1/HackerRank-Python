import re


def main():
    s = input()
    print(solve(s))


def solve(s):
    # Check if the string contains only letters, digits, and spaces, ignoring case sensitivity.
    # Also, strip leading/trailing whitespace before applying regex to
    # ensure valid matches.
    matches = re.search(r"^[a-z0-9 ]+$", s.strip(), re.IGNORECASE)

    # Ensure that the string length is between 1 and 999 characters and
    # matches the regex pattern
    if 0 < len(s) < 1000 and matches:
        # Split the string into words, capitalize each word's first
        # letter, and then join the words back together with spaces.
        return " ".join([name.capitalize() for name in s.split(" ")])
    else:
        # If the string doesn't meet the criteria, return it unchanged.
        return s


if __name__ == "__main__":
    main()
