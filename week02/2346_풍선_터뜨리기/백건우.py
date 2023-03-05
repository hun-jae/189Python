import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
balloons = deque(enumerate(map(int, input().split())))

while balloons:
    idx, rot = balloons.popleft()
    print(idx+1, end=" ")

    if rot > 0:
        balloons.rotate(-(rot - 1))
    elif rot < 0:
        balloons.rotate(-rot)
