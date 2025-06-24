# Read two space-separated integers from input and assign them to
# x and k
x, k = map(int, input().split())

# Read the polynomial expression as a string
P = input()

# Evaluate the polynomial expression using the current value of x
# Compare the result of the evaluation to k and print True if they are
# equal, otherwise False
print(eval(P) == k)
