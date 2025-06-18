# Import the namedtuple factory from the collections module
from collections import namedtuple

n = int(input())
columns = input().split()
# Create a namedtuple class 'Student' with the given column names
Student = namedtuple("Student", columns)

total_marks = 0
# Loop through each student's record
for _ in range(n):
    values = input().split()
    student = Student(*values)
    total_marks += int(student.MARKS)

# Print the average marks rounded to 2 decimal places
print(round(total_marks / n, 2))
