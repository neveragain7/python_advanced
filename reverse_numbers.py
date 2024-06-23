numbers = input().split()

stack = []
for _ in range(len(numbers)):
    element = numbers.pop()
    stack.append(element)

print(' '.join(stack))
