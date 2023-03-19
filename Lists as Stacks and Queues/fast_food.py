from collections import deque

quantity_of_food = int(input())
quantity_food_in_order = deque(int(num) for num in input().split())

print(max(quantity_food_in_order))

while quantity_of_food > 0 and quantity_food_in_order:

    current_order = int(quantity_food_in_order.popleft())
    if not quantity_food_in_order:
        print("Orders complete")
        break

    if quantity_of_food >= current_order:
        quantity_of_food -= current_order
    else:
        quantity_food_in_order.appendleft(current_order)
        print(f"Orders left:", *quantity_food_in_order)
        break
