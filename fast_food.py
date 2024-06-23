from collections import deque

quantity = int(input())
orders = [int(order) for order in input().split()]

queue = deque(orders)

max_order = max(queue)

print(max_order)

orders_complete = True

for order in orders:
    if quantity >= order:
        queue.popleft()
        quantity -= order
    else:
        orders_complete = False
        break

stack = []

for order in queue:
    stack.append(str(order))

if orders_complete:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join(stack)}")
