# 1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5

expression = input()
par_stack = []

for index in range(len(expression)):
    if expression[index] == "(":
        par_stack.append(index)

    if expression[index] == ')':
        start_index = par_stack.pop()
        print(expression[start_index:index + 1])
