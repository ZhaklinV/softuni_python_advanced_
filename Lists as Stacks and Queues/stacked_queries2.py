count = int(input())
work_stack = []

for _ in range(count):
    query = input()

    if query[0] == '1':
        _, number = query.split()
        work_stack.append(int(number))

    if work_stack:
        if query == '2':
            work_stack.pop()

        elif query == '3':
            print(max(work_stack))

        elif query == '4':
            print(min(work_stack))

while work_stack:
    element = work_stack.pop()
    if work_stack:
        print(element, end=', ')
    else:
        print(element)
