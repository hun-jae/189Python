# from math import ceil
# import sys
# N, HAtk = map(int, input().split())
# rooms = [list(map(int, input().split())) for _ in range(N)]
# curHP = 0
# maxHP = sys.maxsize
# cnt = 0
# #처음엔 물약을 다 쓴다는 가정 하에 몬스터 돌림
# # 두번째엔 물약 다 썼을때 즉 쉽게 깬 난이도기준 체력에서 돌림
# # 그럼 이번엔 물약효율 다 못뽑아서 체력 달리겠지
# # 그럼 다음번엔 maxHP에서 min을 더해보면
#
#     for i in range(N):
#         t, a, h = rooms[i]
#         if t == 2:
#             tmpHAtk += a
#             curHP += h
#             if curHP > maxHP:
#                 curHP = maxHP
#         elif t == 1:
#             curHP -= (ceil(h/tmpHAtk) - 1) * a
#             min_ = min(min_, curHP)
#     #print(min_, curHP, maxHP)
#     if cnt==1:
#         maxHP = -min_
#         curHP = maxHP
#     else:
#         if min_ == 0:
#             break
#         maxHP += -min_
#         curHP = maxHP
# print(maxHP+1)
import math
p=input
n,k=map(int,p().split())
h,m=0,0
for i in range(n):
    t,a,c=map(int,p().split())
    if t-1:
        k += a
        h = min(h + c, 0)
    else:
        h -= math.ceil(c / k - 1) * a
    m=min(m,h)
print(-m+1)