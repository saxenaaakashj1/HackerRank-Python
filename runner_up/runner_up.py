def main():
    # Read the number of scores from the user
    n = int(input())

    # Check if the number of scores is within the valid range
    if 2 <= n <= 10:
        # Read all scores in a single line, split by spaces, convert to
        # integers, and sort them in descending order
        scores = sorted([int(score) for score in input().split()], reverse=True)

        # Find the second highest score
        for i in range(1, n):
            if scores[i] != scores[0]:
                print(scores[i])
                break


# Run the main function if this script is executed
if __name__ == "__main__":
    main()
