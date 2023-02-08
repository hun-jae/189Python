import sys
input = sys.stdin.readline

seq = input()
opens = closes = res = 0
prev = ''

for x in seq:
    if x == '(': opens += 1
    if x == ')':
        closes += 1
        if prev == '(': res += (opens - closes)
        else: res += 1

    prev = x

print(res)