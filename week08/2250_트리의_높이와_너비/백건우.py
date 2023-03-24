# 가장 왼쪽부터 탐색하면서 노드 열의 위치 새겨줌
# 왼쪽, 가운데, 오른쪽 노드가 있을 때 가운데 노드의 열 번호는 왼쪽 노드와 그 하위 노드를 전부 포함한 숫자 다음이다.

import sys
from collections import defaultdict

input = sys.stdin.readline
n = int(input())

tree={}
degreeLen = defaultdict(list)
isStart = [True for _ in range(n+1)]
for _ in range(n):
    node, l, r =map(int,input().split())
    tree[node] = [l, r]
    if l != -1 : # 다른 노드의 하위 노드이면 시작 노드 아니다.
        isStart[l] = False
    if r != -1 :
        isStart[r] = False

start = 0
for i in range(1, n+1):
    if isStart[i]: # 시작 노드
        start = i
        break

col = 0 # 열 번호
def dfs(idx, degree):
    global col
    if tree[idx][0] != -1 : # 왼쪽 노드가 존재하면 그 노드 다음이 현재 노드의 열번호다.
        dfs(tree[idx][0], degree+1)

    if not degree in degreeLen : # 현재 노드가 없으면 
        degreeLen[degree].append(col)
    elif len(degreeLen[degree]) == 2: # 나중에 탐색된 노드가 더 오른쪽에 있다.
        degreeLen[degree][1] = col
    elif len(degreeLen[degree]) == 1: 
        degreeLen[degree].append(col)
    col += 1

    if tree[idx][1] != -1: # 현재 노드 다음부터가 오른쪽 노드 시작임
        dfs(tree[idx][1], degree+1)

dfs(start, 1)

ansDegree = 10001
ansLen = 0
for key in degreeLen: # degreeLen의 key가 degree고 item이 가장 왼쪽 열, 가장 오른쪽 열이다.
    tempLen = 0
    if len(degreeLen[key]) == 1 : # 만약 같은 degree에 노드가 한개라면
        tempLen = 1
    else : # 같은 degree에 노드가 여러개라면
        tempLen = degreeLen[key][1] - degreeLen[key][0] + 1

    if tempLen > ansLen :
        ansLen = tempLen
        ansDegree = key
    elif tempLen == ansLen :
        if ansDegree > key :
            ansDegree = key

print('{} {}'.format(ansDegree, ansLen))
