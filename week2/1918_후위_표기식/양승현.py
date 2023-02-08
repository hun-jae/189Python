prior = {'+': 0, '-': 0, '*': 1, '/': 1, '(': 2, ')': 2}
comp = lambda x, y: prior[x] <= prior[y]

seq, stack = input(), []

for op in seq:
    # case 1: operand
    if op not in prior:
        print(op, end='')
        continue

    # case 2: parenthesis
    if op == ')':
        while stack[-1] != '(':
            print(stack.pop(), end='')
        stack.pop()
        continue

    # case 3: operates
    while stack and comp(op, stack[-1]):
        if stack[-1] == '(': break
        print(stack.pop(), end='')

    stack.append(op)

while stack:
    print(stack.pop(), end='')