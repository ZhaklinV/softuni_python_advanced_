from collections import deque


def convert_time_to_sec(time_data):
    hours, minutes, seconds = [int(x) for x in time_data.split(':')]
    return seconds + minutes * 60 + hours * 60 * 60


def convert_to_time(total_seconds):
    hours = total_seconds // (60 * 60)
    total_seconds %= (60 * 60)
    minutes = total_seconds // 60
    total_seconds %= 60
    return f'{hours:02d}:{minutes:02d}:{total_seconds:02d}'


input_line = input().split(';')
robots_data = {}
robots_timer = {}

for el in input_line:
    name, time = el.split('-')
    robots_data[name] = int(time)
    robots_timer[name] = -1

start_time = convert_time_to_sec(input())

products_deque = deque()
product = input()
while product != 'End':
    products_deque.append(product)
    product = input()

while products_deque:
    start_time += 1
    start_time %= 24 * 60 * 60
    item = products_deque.popleft()

    for name, busy_to_by_robots in robots_timer.items():
        if start_time >= busy_to_by_robots:
            robots_timer[name] = start_time + robots_data[name]
            print(f"{name} - {item} [{convert_to_time(start_time)}] ")
            break

    else:
        products_deque.append(item)
