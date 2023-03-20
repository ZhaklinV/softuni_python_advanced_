from collections import deque

quantity_of_food = int(input())
orders = deque([int(num) for num in input().split()])

print(max(orders))

while orders:
    current_order = int(orders[0])

    if current_order > quantity_of_food:
        break

    quantity_of_food -= current_order
    orders.popleft()

if not orders:
    print("Orders complete")

else:
    print(f"Orders left:", *orders)
