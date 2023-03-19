count = int(input())
work_stack = []

for i in range(count):
    query = input()
    if query[0] == '1':
        _, number = query.split()
        work_stack.append(int(number))

    elif query == '2':
        if len(work_stack) > 0:
            work_stack.pop()

    elif query == '3':
        print(max(work_stack))

    elif query == '4':
        print(min(work_stack))

work_stack = list(reversed(work_stack))
print(*work_stack, sep=', ')
