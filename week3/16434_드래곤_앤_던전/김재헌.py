from math import ceil
import sys
N, HAtk = map(int, input().split())
rooms = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
maxHP = sys.maxsize

l = 0
r = maxHP

while l < r:
    flag = 1
    atk = HAtk
    curHp = (l+r) // 2

    for room in rooms:
        t, a, h = room
        
        if t == 1: #몬스터
            curHp -= a*(ceil(h / atk) - 1)
            if curHp <=0: #중간에 죽으면
                l = (l + r) // 2 + 1
                flag=0
                break

        elif t == 2: #물약
            curHp = min(curHp+h, (l+r)//2)
            atk += a

    if flag: #다 끝나도 살아있으면
        r = (l + r) // 2
print(l)

