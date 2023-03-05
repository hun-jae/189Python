"""
문제 정보
    로봇 시뮬레이션 (골드 5)
    https://www.acmicpc.net/problem/2174
    *
작성
    양승현
    2023 02 24
"""

import sys
input = sys.stdin.readline

# row B col A
A, B = map(int, input().split())

# N robots, M operations
N, M = map(int, input().split())

# d: {num: [x, y, heading_dir], ...}
d = {}
X, Y, DIR = 0, 1, 2

NESW = ['N', 'E', 'S', 'W']
MOVE = {'N': (0, 1), 'W': (-1, 0), 'S': (0, -1), 'E': (1, 0)}

# return the new direction of the robot
def rotate(cur, cnt, op):
    next_idx = NESW.index(cur) + (cnt if op == 'R' else -cnt)
    return NESW[next_idx % 4]

# the robot #num moves forward repeat times
def forward(num, repeat):
    x, y, dir = d[num]
    dx, dy = MOVE[dir]

    # move to the heading direction repeat times
    for i in range(1, repeat+1):
        nx, ny = x+dx*i, y+dy*i

        # case 1: out of bound
        if not (0 < nx <= A and 0 < ny <= B):
            print(f'Robot {num} crashes into the wall')
            return False

        # case 2: collision with another robot
        for other in d:
            if other == num: continue
            ox, oy, _ = d[other]
            if (nx, ny) == (ox, oy):
                print(f'Robot {num} crashes into robot {other}')
                return False

        # if moveable, update location
        d[num] = [nx, ny, dir]

    return True


def operate():
    res = True
    for _ in range(M):
        num, op, repeat = input().split()
        num, repeat = int(num), int(repeat)

        if not res:
            continue    # failure already found

        # operation 1: move forward
        if op == 'F':
            res = forward(num, repeat)
        # operation 2, 3: rotate left or right
        else:
            d[num][DIR] = rotate(d[num][DIR], repeat, op)

    return res


# take input
for num in range(1, N+1):
    x, y, dir = input().split()
    d[num] = [int(x), int(y), dir]

# run the test case
if operate():
    print('OK')

