from collections import deque

n = int(input())
paper = list(map(int, input().split()))
balloons = []

for i in range(n):
    balloons.append(i+1)

balloons = deque(balloons)

for j in range(n):
    tmp = balloons.popleft()
    print(tmp)
    if paper[tmp-1]>0:
        balloons.rotate(-paper[tmp-1]+1)
    else:
        balloons.rotate(-paper[tmp-1])
