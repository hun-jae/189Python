"""
KKRKK -> R 양 끝에 K가 2개씩 붙어있으니까 5
RRKRR -> 중간의 K를 제외하면 총 R의 개수가 4임
중간에 있는 글자를 몇개 지워서 가장 긴 대칭 수열을 찾는다.
실패 코드
"""
import sys

input = sys.stdin.readline
s = list(input())
if not 'R' in s:
    print("0")
    exit(0)
totalK = s.count('K')
cnt = 0
left = [0 for _ in range(len(s))]
right = [0 for _ in range(len(s))]
for i in range(len(s)):
    if s[i] == 'K':
        cnt += 1
    elif s[i] == 'R':
        left[i] = cnt
        right[i] = totalK - cnt

ans = s.count('R')
for i in range(len(s)):
    if s[i] == 'R':
        cntR = 1
        ans = max(ans, cntR + 2*min(right[i], left[i]))
        for j in range(i - 1 , -1 , -1):
            if s[j] == 'R':
                cntR += 1
                ans = max(ans, cntR + 2*min(right[i], left[j]))
print(ans)
