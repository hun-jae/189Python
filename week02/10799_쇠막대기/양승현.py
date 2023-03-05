import sys
input = sys.stdin.readline

seq = input()
opens = closes = res = 0
prev = ''

# 열린 횟수와 닫힌 횟수를 추적하여 조각의 개수 계산
for x in seq:
    if x == '(': opens += 1
    if x == ')':
        closes += 1

        # 닫히는 경우 1: 레이저인 경우 닫히지 않은 막대기들만큼 생성
        if prev == '(':
            res += (opens - closes)
        # 닫히는 경우 2: 꼬투리 += 1
        else:
            res += 1

    prev = x

print(res)