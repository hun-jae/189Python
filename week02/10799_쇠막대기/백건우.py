import sys

input = sys.stdin.readline
pipes = list(input())
q = []
ans = 0
for idx, cur in enumerate(pipes):
    if cur == '(':
        q.append(cur)
    elif cur == ')':
        q.pop()
        if pipes[idx-1] == '(' : # case of lazer
            ans += q.count('(')
        elif pipes[idx-1] == ')' : # case not lazer
            ans += 1
print(ans)
