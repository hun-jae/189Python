from collections import deque
from sys import stdin
n = int(stdin.readline())
buildings = list(map(int, stdin.readline().split()))
# 기본 접근은 스택으로 왼쪽 오른쪽 두번 돌려야함
# 스택을 쌓을 때 result에 idx를 idx차이를 min으로 주면(오른쪽에만) idx를 구할 수 있음

result = [200000] * n
stack = []
resultCntLeft = [0] * n
for idx, i in enumerate(buildings):
    while stack and stack[-1][1] < i:
        popIdx, popI = stack.pop()
        result[popIdx] = idx
    if len(stack) > 0:
        k = -1
        for k in range(len(stack) - 1, -1, -1):
            if i < stack[k][1]:
                break
        if stack[k][1] > i:
            k = stack[k][0]
            resultCntLeft[idx] = resultCntLeft[k] + 1

    stack.append([idx, i])

# 반대편
# 반대로하는건 뒤집은 뒤 idx = n-1 - idx
buildings = buildings[::-1]
stack = []
resultCntRight = [0] * n
for idx, i in enumerate(buildings):
    idx = n - 1 - idx  # 진짜 building의 idx임
    while stack and stack[-1][1] < i:
        popIdx, popI = stack.pop()
        result[popIdx] = result[popIdx] if result[popIdx] - popIdx < popIdx - idx else idx
    if len(stack) > 0:
        k = -1
        for k in range(len(stack) - 1, -1, -1):
            if i < stack[k][1]:
                break
        if stack[k][1] > i:
            k = stack[k][0]
            resultCntRight[idx] = resultCntRight[k] + 1

    stack.append([idx, i])

for i in range(n):
    if result[i] == 200000: #아무도 못본친구
        print(0)
    else:
        print(resultCntLeft[i] + resultCntRight[i], end=" ")
        #print(resultCntLeft[i], end=" ")
        #print(resultCntRight[i], end=" ")
        print(result[i] + 1)
