def main():
    # Read the number of students
    n = int(input())

    # Check if the number of students is within the acceptable range
    if 2 <= n <= 10:
        # Create a dictionary where the key is the student's name
        # and the value is a list of their marks (converted to float)
        students = {
            student[0]: [float(mark) for mark in student[1:]]
            for student in (input().split(" ") for _ in range(n))
        }

        # Read the name of the student whose average marks are to be
        # queried
        query_name = input()

        # Check if the query_name is in the students dictionary
        # If it is, calculate the average of the student's marks and
        # print it
        # If not, do nothing (None)
        (
            print(f"{sum(students[query_name]) / 3:.2f}")
            if query_name in students
            else None
        )


# Standard Python boilerplate to ensure the main function is called when the
# script is executed
if __name__ == "__main__":
    main()
