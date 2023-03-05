import sys

N, M = map(int, input().split())
T = []
for _ in range(N):
    T.append(int(input()))

# 심사가 끝나는 최소 시간을 이분탐색한다. 최소시간을 각 심사대에서 걸리는 시간으로 나누면 각 심사대에서 최소시간동안 심사한 사람 수가 나오고 이를 모두 더하면 심사가 끝난 모든 인원의 수가 나온다.
left = 0
right = sys.maxsize # right의 범위 설정을 잘해야한다. sys.maxsize로 해도 통과되지만 주어진 조건에서 최악의 경우를 생각하면 심사대가 1개일 때 심사에 걸리는 시간 Tk를 10^9이라 한다면 M(사람 수)이 10^9일 때 right = Tk x M = 10^18이 된다. 
ans = 0
while left <= right:
    mid = (left+right)//2  #현재의 최소시간
    finish = 0
    for t in T:   # 현재의 최소시간일 때 처리가능한 심사 수
        finish += mid//t

    if finish < M:# 심사한 인원(finish)이 친구의 수보다 적다. -> 심사 시간을 늘려야 한다.
        left = mid+1
    elif finish >= M : # 심사한 인원(finish)이 친구의 수보다 많다. -> 심사 시간을 줄여도 된다.
        ans = mid
        right = mid-1
print(ans)
