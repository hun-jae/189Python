N = int(input())
h_lst = [int(x) for x in input().split()]

# self sorting stack
left, right = [], []
MAX = float('inf')

# number of visible buildings
result = [0 for _ in range(N)]

# near high index that being seen
near_r = [MAX for _ in range(N)]
near_l = [MAX for _ in range(N)]


# see right side
for i in range(N-1, -1, -1):
    while right and right[-1][0] <= h_lst[i]: right.pop()
    result[i] += (len(right))

    if right: near_r[i] = right[-1][1]
    right.append([h_lst[i], i+1])

# see left side
for i in range(N):
    while left and left[-1][0] <= h_lst[i]: left.pop()
    result[i] += len(left)

    if left: near_l[i] = left[-1][1]
    left.append([h_lst[i], i+1])

# need numbers of higher building near by
near = []
for i in range(N):
    ldist, rdist = abs(i+1-near_l[i]), abs(i+1-near_r[i])
    if ldist == MAX: near.append(near_r[i])
    elif rdist == MAX: near.append(near_l[i])
    else: near.append(near_l[i] if ldist <= rdist else near_r[i])


for see, n in zip(result, near):
    if see: print(see, n)
    else: print(0)
