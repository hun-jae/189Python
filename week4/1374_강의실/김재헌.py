import heapq, sys
input = sys.stdin.readline
n = int(input())
lectures = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: x[1])
que = []
for lec in lectures:
    if que and que[0] <= lec[1]:
        heapq.heappop(que)
    heapq.heappush(que, lec[2])
print(len(que))