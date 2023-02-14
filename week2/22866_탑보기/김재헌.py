from collections import deque
from sys import stdin
n = int(stdin.readline())
buildings = list(map(int, stdin.readline().split()))
# 기본 접근은 스택으로 왼쪽 오른쪽 두번 돌려야함
# 스택을 쌓을 때 result에 idx를 idx차이를 min으로 주면(오른쪽에만) idx를 구할 수 있음

result = [200000] * n

#왼쪽
stack = []
resultCntLeft = [0] * n #왼쪽에 보이는 건물 수
for idx, i in enumerate(buildings):
    while stack and stack[-1][1] < i: #자신보다 작은 빌딩이 스택 top에 있으면 빼주고, 자신을 상대 빌딩의 result에 추가
        popIdx, popI = stack.pop()
        result[popIdx] = idx
    if len(stack) > 0: #작은 빌딩을 다 뺐는데 빌딩이 남아있다면
        #자신과 같은 높이의 빌딩이 있을 수 있으므로 자신보다 큰 빌딩을 찾아야함
        k = -1
        for k in range(len(stack) - 1, -1, -1): 
            if i < stack[k][1]: #자신보다 높은 빌딩의 stack에서의 index : k
                break
        if stack[k][1] > i: #디버깅하다가 추가된 코든데 최적화를 하지 못함 (자신보다 높은 빌딩이 스택에 존재할 때)
            k = stack[k][0] #자신보다 높은 빌딩의 실제 index를 k에 저장
            resultCntLeft[idx] = resultCntLeft[k] + 1 #자신의 왼쪽으로 보이는 건물 수

    stack.append([idx, i])

# 오른쪽
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
    if result[i] == 200000: #아무도 못본 빌딩이면 0만 출력
        print(0)
    else:
        print(resultCntLeft[i] + resultCntRight[i], end=" ")
        print(result[i] + 1)
