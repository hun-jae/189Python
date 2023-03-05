from heapq import heappush as push, heappop as pop
import sys
input = sys.stdin.readline

"""
접근 1: 앞에서부터 접근하면 가능한 선택지가 너무 많아서 최선이 뭔지 파악하기 어려움
    당장 그리디하게 선택해도, 데드라인 때문에 로직을 파악하기 쉽지 않음
접근 2: 뒤에서부터 접근하면 개인적으로 이해하기가 편했음 (데드라인 지난 애들은 고려x)

res := 얻을 수 있는 총 컵라면 수
power := 일을할 수 있는 능력. 1초에 1씩 증가
t := 현재 시각, 가능한 마지막 시간에서 0까지 순차적으로 감소
tasks := 현재 시간 t에서 선택 가능한 문제들
"""

N = int(input())
info = sorted([list(map(int, input().split())) for _ in range(N)])

res, power, t = 0, 0, info[-1][0]
tasks = []

while 0 < t:
    power += 1
    while info and t <= info[-1][0]:
        push(tasks, -info.pop()[1])

    if 0 < power and tasks:
        res += -pop(tasks)
        power -= 1

    t -= 1

print(res)