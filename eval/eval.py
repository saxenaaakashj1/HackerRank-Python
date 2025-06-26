# Prompt the user to enter a Python expression and remove
# leading/trailing whitespace
expression = input().strip()

# Check if the expression does NOT start with 'print'
# If it doesn't, evaluate the expression and print the result
# This avoids printing 'None' if the expression itself is a print() call
if not expression.startswith("print"):
    # Evaluate the expression and print the result
    print(eval(expression))

# Always evaluate the expression, so that any print() calls in the input
# are executed. For example, if the user enters 'print(3 + 5)', this
# line ensures it gets printed
eval(expression)
