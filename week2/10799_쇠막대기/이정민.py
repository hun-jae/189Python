input = list(map(str, input()))

stack = []
sum = 0


for i in range(len(input)):
    if input[i] != ')':
        stack.append(input[i])
    else:
        if input[i-1] == ')':
            stack.pop()
            sum += 1
        else:
            stack.pop()
            sum += len(stack)

print(sum)