clothes_stack = [int(x) for x in input().split()]
capacity_of_rack = int(input())
# sum_of_clothes = 0
current_rack = capacity_of_rack
count_rack = 1

while clothes_stack:
    current_cloth = clothes_stack[-1]
    if current_cloth <= current_rack:
        current_rack -= current_cloth
        clothes_stack.pop()

    else:
        count_rack += 1
        current_rack = capacity_of_rack

print(count_rack)
