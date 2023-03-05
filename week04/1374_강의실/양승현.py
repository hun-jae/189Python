from heapq import heappush as push, heappop as pop
import sys
input = sys.stdin.readline

"""
접근 1: info를 시작시간 순서로 sort하여 항상 빠른 시작시간 기준으로 봄
접근 2: heapq에 종료시간이 이른 시간순으로하여 track
접근 3: 만약 이번에 시작하는 강의 전에 끝나느 게 있으면 빼내고 시작

Info := [[시작시간, 종료시간], ...]
res: 강의실의 개수 tracking -> 가장 피크 시간의 강의실 개수가 정답
q: 현재 이용중인 강의실 정보 track
"""

N = int(input())
info = sorted([list(map(int, input().split()[1:])) for x in range(N)])
res, q = 0, []

for start, end in info:
    if q and q[0] <= start: pop(q)
    push(q, end)

    res = max(res, len(q))

print(res)