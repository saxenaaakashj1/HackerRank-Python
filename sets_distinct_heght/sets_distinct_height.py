def average(array):
    # Convert the list to a set to remove duplicates,
    # then compute the average of those unique values
    return round(sum(set(array)) / len(set(array)), 3)


if __name__ == "__main__":
    n = int(input())  # Number of elements (not directly used)
    arr = list(
        map(int, input().split())
    )  # Read and convert input to list of integers
    result = average(arr)
    print(result)  # Print the average rounded to 3 decimal places
