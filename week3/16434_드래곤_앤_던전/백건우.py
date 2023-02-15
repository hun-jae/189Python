import sys
from math import ceil
input = sys.stdin.readline
N, ATK = map(int,input().split())

rooms = []
for _ in range(N):
    rooms.append(list(map(int,input().split())))

l = 1
r = sys.maxsize # maxHp의 범위가 정해져 있지 않으므로 가능한 큰 값을 설정한다.
ans = 0
while l <= r:
    canWin = True   # 현재 maxHp로 던전을 돌 수 있는지 판별
    mid = (l+r)//2  # maxHp를 탐색한다.
    curHp = mid
    curATK = ATK
    for room in rooms:  # 방을 돈다.
        if room[0] == 1 :  # 드래곤이 있는 방에 들어갔을 때
            monsterATK, monsterHp = room[1], room[2]
            if curATK >= monsterHp :    # 용사의 공격력이 드래곤의 체력보다 같거나 크면 체력손실없이 바로 다음방으로 넘어간다.
                continue
            curHp -= (ceil(monsterHp/curATK)-1)*monsterATK # 몬스터를 죽일 때까지 n회 공격했다면 용사는 n-1회 공격 받았다.(용사가 먼저 공격하니까)
            if curHp <= 0: # 몬스터를 죽였을 때 용사의 hp가 0이하이면 마지막 공격전에 죽은상태이므로 실패
                canWin = False
                break
        elif room[0] == 2:  #포션 방일 때
            curATK += room[1]
            if curHp + room[2] > mid :
                curHp = mid
            else :
                curHp += room[2]
        if not canWin:
            break
    if canWin :
        r = mid-1
        ans = mid
    else :
        l = mid+1
print(ans)
