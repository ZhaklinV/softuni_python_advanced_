from collections import deque

quantity_water = int(input())
name = input()
get_water_queue = deque()

while not name == "Start":
    get_water_queue.append(name)
    name = input()

command = input()
while not command == 'End':
    if command.isdigit():
        litters = int(command)
        current_name = get_water_queue.popleft()
        if quantity_water >= litters:
            quantity_water -= litters
            print(f"{current_name} got water")
        else:
            print(f"{current_name} must wait")

    else:
        _, litters_to_fill = command.split()
        quantity_water += int(litters_to_fill)

    command = input()

print(f"{quantity_water} liters left")
