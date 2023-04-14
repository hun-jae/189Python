"""
KKRKK -> R 양 끝에 K가 2개씩 붙어있으니까 5
RRKRR -> 중간의 K를 제외하면 총 R의 개수가 4임
중간에 있는 글자를 몇개 지워서 가장 긴 대칭 수열을 찾는다.
실패 코드 - 아이디어는 맞았는데 투포인터 구현부분을 잘못해서 시간초과남

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
"""
import sys

input = sys.stdin.readline
s = list(input())

totalK = s.count('K')
cnt = 0
left = []
right = []
for i in range(len(s)):
    if s[i] == 'K':
        cnt += 1
    elif s[i] == 'R':
        left.append(cnt)
        right.append(totalK - cnt)

ans = 0
l, r = 0, len(right) - 1   # 넓은 범위에서 줄여나간다.
while l <= r :
    ans = max(ans, r - l + 1 + 2 * min(left[l],right[r]))
    if left[l] < right[r]:   # left[l]이 right[r]보다 작으면 r을 아무리 줄여도 결국 최대로 가능한 k의 개수는 left[l]이다. 따라서 left[l]을 더 크게 만들어서 가능한 k의 개수를 더 늘려야 한다.
        l += 1
    else :  # 위와 
        r -= 1
print(ans)
