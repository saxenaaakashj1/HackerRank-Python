# Read two integers from input:
# N = number of students
# X = number of subjects
N, X = map(int, input().split())

# Read X lines of input, where each line contains N float numbers
# (scores of students in one subject).
# 'map(float, input().split())' converts the input line into floats.
# '[...] for _ in range(X)' repeats this process X times (for each subject).
# 'zip(*[...])' transposes the list so we group scores per student
# instead of per subject.
scores = list(zip(*[map(float, input().split()) for _ in range(X)]))

# For each student's scores (now grouped per student),
# calculate the average by summing the scores and dividing by X
# (number of subjects).
# Round the average to 1 decimal place and print it.
for score in scores:
    print(round(sum(score) / X, 1))
