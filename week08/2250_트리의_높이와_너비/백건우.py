# 가장 왼쪽부터 탐색하면서 노드 열의 위치 새겨줌
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
    if l != -1 :
        isStart[l] = False
    if r != -1 :
        isStart[r] = False

start = 0
for i in range(1, n+1):
    if isStart[i]:
        start = i
        break

col = 0
def dfs(idx, degree):
    global col
    if tree[idx][0] != -1 :
        dfs(tree[idx][0], degree+1)

    if not degree in degreeLen :
        degreeLen[degree].append(col)
    elif len(degreeLen[degree]) == 2:
        degreeLen[degree][1] = col
    elif len(degreeLen[degree]) == 1:
        degreeLen[degree].append(col)
    col += 1

    if tree[idx][1] != -1:
        dfs(tree[idx][1], degree+1)

dfs(start, 1)

ansDegree = 10001
ansLen = 0
for key in degreeLen:
    tempLen = 0
    if len(degreeLen[key]) == 1 :
        tempLen = 1
    else :
        tempLen = degreeLen[key][1] - degreeLen[key][0] + 1

    if tempLen > ansLen :
        ansLen = tempLen
        ansDegree = key
    elif tempLen == ansLen :
        if ansDegree > key :
            ansDegree = key

print('{} {}'.format(ansDegree, ansLen))
