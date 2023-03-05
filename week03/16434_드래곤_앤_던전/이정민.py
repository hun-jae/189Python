import sys
input = sys.stdin.readline

N, Hatk = map(int, input().split())
rooms = []

for i in range(N):
    rooms.append(list(map(int, input().split())))

l = 1
#얼마나 필요할지 몰라서 가장 큰 값으로 설정
r = int(1e18)

while l <= r:
    mid = (l+r)//2
    #용사의 초기 생명력, 공격력
    hp = mid
    atk = Hatk
    #용사의 생존 여부
    hero = True

    for room in rooms:
        if room[0] == 1:
            #몬스터의 공격력과 생명력
            m_atk = room[1]
            m_hp = room[2]
            #몬스터가 바로 죽는 경우
            if m_hp <= atk:
                continue
            #몬스터가 죽을 때까지
            while (m_hp > 0):
                m_hp = m_hp - atk
                if m_hp < 0:
                    break
                hp = hp - m_atk
                #용사가 먼저 죽는 경우
                if hp <= 0:
                    hero = False
                    break
        elif room[0] == 2:
            atk = atk + room[1]
            hp = hp + room[2]
            #포션 섭취시 hp가 초기 hp 보다 높은 경우
            if hp > mid:
                hp = mid
        #용사가 죽은 경우
        if hero == False:
            l = mid+1
            break
    #용사가 살아있는 경우
    if hero == True:
        r = mid - 1

print(l)
