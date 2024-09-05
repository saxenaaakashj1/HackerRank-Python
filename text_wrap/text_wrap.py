# import textwrap  # Optional: The 'textwrap' module contains a built-in function 'textwrap.fill()' that can perform this task directly.

def main():
    string, max_width = input().strip(), int(input())
    result = wrap(string, max_width)
    print(result)


def wrap(string, max_width):
    if 0<len(string)<1000 and 0<max_width<len(string):
    # Using list comprehension to slice the string into chunks of size max_width
    # Then joining those chunks with newline characters to form the final result
        return "\n".join([string[i:i+max_width] for i in range(0, len(string), max_width)])
    
    # The task can also be achieved using the built-in function `textwrap.fill()`, 
    # which automatically wraps text at the specified width.
    # return textwrap.fill(string, max_width)


if __name__ == "__main__":
    # The main function starts here when the script is executed
    main()