def main():
    s = input()
    i, c = input().split()
    i = int(i)
    print(mutate_string(s, i, c))


def mutate_string(string, position, character):
    # Create a new string by replacing the character at the specified
    # position
    # string[:position] gets the substring before the position
    # character is added at the position
    # string[position+1:] gets the substring after the position
    return string[:position] + character + string[position + 1 :]


if __name__ == "__main__":
    main()
