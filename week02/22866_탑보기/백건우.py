import sys
sys.setrecursionlimit(10**9)
INF = sys.maxsize
input = sys.stdin.readline
N = int(input())
buildings = list(map(int,input().split()))
isFind = [False for _ in range(N)]
canSeeR = [0 for _ in range(N)]
canSeeL = [0 for _ in range(N)]
minDis = [[INF,0] for _ in range(N)] #거리, 번호

def dfsRight(idx):
    if isFind[idx] == True:
        return canSeeR[idx]+1
    isFind[idx] = True
    for i in range(idx+1, N):
        if buildings[idx] < buildings[i]:
            if minDis[idx][0] > i - idx :
                minDis[idx][0] = i - idx
                minDis[idx][1] = i
            canSeeR[idx] = dfsRight(i)
            return canSeeR[idx] + 1
    return canSeeR[idx]+1 # 오른쪽의 마지막 건물일 때

def dfsLeft(idx):
    if isFind[idx] == True:
        return canSeeL[idx]+1
    isFind[idx] = True
    for i in range(idx-1, -1, -1):
        if buildings[idx] < buildings[i]:
            minDis[idx][0] = idx - i
            minDis[idx][1] = i
            canSeeL[idx] = dfsLeft(i)
            return canSeeL[idx] + 1
    return canSeeL[idx]+1 # 왼쪽의 마지막 건물일 때

for i in range(len(buildings)-1,-1,-1):
    if isFind[i] == False:
        isFind[i] = True
        for idx in range(i-1, -1,-1):
            if buildings[i] < buildings[idx] :
                minDis[i][0] = i - idx  #거리
                minDis[i][1] = idx        #번호
                canSeeL[i] = dfsLeft(idx)
                break

isFind = [False for _ in range(N)]
for i in range(len(buildings)):
    if isFind[i] == False:
        isFind[i] = True
        for idx in range(i+1, N):
            if buildings[i] < buildings[idx] :
                if minDis[i][0] > idx-i :
                    minDis[i][0] = idx-i
                    minDis[i][1] = idx
                canSeeR[i] = dfsRight(idx)
                break


for idx in range(N):
    cnt = canSeeR[idx] + canSeeL[idx]
    if cnt == 0:
        print("0")
    else :
        print('{} {}'.format(cnt, minDis[idx][1]+1))
