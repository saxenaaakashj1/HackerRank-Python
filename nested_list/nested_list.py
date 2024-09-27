def main():
    # Read the number of students
    n = int(input())

    if 2 <= n <= 5:
        # Collect student names and scores
        students = [[input(), float(input())] for _ in range(n)]

        # Extract and sort scores
        scores = sorted(student[1] for student in students)

        # Find the second lowest score
        second_lowest_score = None
        for score in scores:
            if score > scores[0]:
                second_lowest_score = score
                break

        # Collect names of students with the second lowest score
        names = sorted(
            student[0]
            for student in students
            if student[1] == second_lowest_score
        )

        # Print the names
        for name in names:
            print(name)


if __name__ == "__main__":
    main()
