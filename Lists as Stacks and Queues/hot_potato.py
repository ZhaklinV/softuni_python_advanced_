from collections import deque

kids_names = deque(input().split())
burning_toss = int(input())

while len(kids_names) > 1:
    kids_names.rotate(-burning_toss)
    print(f'Removed {kids_names.pop()}')

print(f"Last is {kids_names[0]}")
