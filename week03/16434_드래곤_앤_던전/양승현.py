from math import ceil

N, H_ATK = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(N)]
MAX_HP = sum([x[2]*x[1] for x in info])  # assume my att=1, require MAX_HP

def simulate(HP, atk=H_ATK):
    hp = HP
    for monster, m_atk, m_hp in info:
        if monster == 1:
            hit = ceil(m_hp / atk)-1
            hp -= m_atk * hit
        else:
            atk += m_atk
            hp = min(hp+m_hp, HP)

        if hp <= 0: return False

    return True

l, r = 0, MAX_HP+1
while l < r:
    mid = (l+r)//2
    if simulate(mid):
        r = mid
    else:
        l = mid+1

print(l)
