# 우선순위 테이블과 우선순위 비교 함수 정의
prior = {'+': 0, '-': 0, '*': 1, '/': 1, '(': 2, ')': 2}
comp = lambda x, y: prior[x] <= prior[y]

seq, stack = input(), []

for op in seq:
    # 1. 피연산자인 경우 바로 출력
    if op not in prior:
        print(op, end='')
        continue

    # 2. ')'인 경우 '('까지 전부 pop
    if op == ')':
        while stack[-1] != '(':
            print(stack.pop(), end='')
        stack.pop()
        continue

    # 3. 연산자인 경우 우선순위가 높은 애들을 전부 pop
    while stack and comp(op, stack[-1]):
        if stack[-1] == '(': break
        print(stack.pop(), end='')

    # 3번의 경우에만 append
    stack.append(op)

while stack:
    print(stack.pop(), end='')