number_of_lines = int(input())
stack = []
result = []
for _ in range(number_of_lines):
    command = input().split()

    if command[0] == "1":
        number = int(command[1])
        stack.append(number)
    elif command[0] == "2":
        if stack:
            stack.pop()
    elif command[0] == "3":
        if stack:
            max_number = max(stack)
            print(max_number)
    elif command[0] == "4":
        if stack:
            min_number = min(stack)
            print(min_number)

for _ in range(len(stack)):
    element = stack.pop()
    result.append(element)

str_result = [str(number) for number in result]
print(', '.join(str_result))
