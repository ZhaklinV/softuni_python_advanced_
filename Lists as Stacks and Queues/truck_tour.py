# The petrol pumps are numbered 0 to (N−1) (both inclusive)
# the truck consumes 1 liter of petrol per 1 kilometer, and its tank has infinite petrol capacity
from collections import deque

count_pump = int(input())
pumps = deque()

first_pump = None

for _ in range(count_pump):
    action = [int(x) for x in input().split()]
    pumps.append(action)

for i in range(count_pump):
    tank = 0
    not_full_circle = False

    for amount_petrol, distance in pumps:
        tank += amount_petrol
        if tank >= distance:
            tank -= distance

        else:
            not_full_circle = True
            break

    if not_full_circle:
        pumps.append(pumps.popleft())
    else:
        first_pump = i
        break

print(first_pump)
