# 접근 1
# To reviwer : 실패한 방법이라 접근2 보시면 돼요!
# 컵라면 높은 수 대로 정렬을 한 뒤에 데드라인 빠른 순으로 정렬한다
# 같은 수라면 데드라인 빠른거 먹음
# 해당 데드라인 맨 끝에 그 컵라면 수 먹음

# 접근 2
# 데드라인을 젤 마지막부터 줄여나가면서 해당위치에 들어올 컵라면 수를 찾는다? 6에 1개, 5에 x, 4에 x, 3에 2개, 2에 5개, 1에 7개
# 그럼 priority que 이용해서 해당 데드라인에 컵라면이 몇 개 들어올 지 찾자

import heapq
import sys

input = sys.stdin.readline
n = int(input())
lamens = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: -x[0]) #deadline이 긴 순으로 정렬
pointer = 0
answer = 0
que = []
for dead in range(lamens[0][0], 0, -1):
    for i in range(pointer, n):  # 데드라인까지 먹을수 있는 라면을 que에 넣어줌
        if lamens[i][0] < dead:  # 해당 라면의 데드라인이 현재 데드라인보다 작다면 끝내줌
            pointer = i
            break
        heapq.heappush(que, -lamens[i][1])
        if i >= n - 1: #모든 라면이 que에 들어갔을 때 pointer 갱신
            pointer = n
    if que:
        answer -= heapq.heappop(que)
print(answer)
