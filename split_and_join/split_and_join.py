def main():
    line = input()
    print(split_and_join(line))


def split_and_join(line):
    # Split the input string by spaces and join the resulting list with
    # hyphens
    # line.split(" ") splits the string into a list of substrings
    # "-".join() joins the substrings with hyphens
    return "-".join(line.split(" "))


if __name__ == "__main__":
    main()
