def main():
    # Call the validate_string function with the user's input
    validate_string(input())


def validate_string(s):
    if 0 < len(s) < 1000:
        # Check if the string contains any alphanumeric characters
        # (letters or numbers)
        print("True") if any([ch.isalnum() for ch in s]) else print("False")

        # Check if the string contains any alphabetic characters
        # (letters only)
        print("True") if any([ch.isalpha() for ch in s]) else print("False")

        # Check if the string contains any digits (numbers only)
        print("True") if any([ch.isdigit() for ch in s]) else print("False")

        # Check if the string contains any lowercase letters
        print("True") if any([ch.islower() for ch in s]) else print("False")

        # Check if the string contains any uppercase letters
        print("True") if any([ch.isupper() for ch in s]) else print("False")


if __name__ == "__main__":
    # Execute the main function when the script is run
    main()
