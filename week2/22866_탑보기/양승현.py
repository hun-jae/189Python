N = int(input())
h_lst = [int(x) for x in input().split()]

# 좌측, 혹은 우측으로 보이는 빌딩의 높이들을 담는(append) 배열
# 가려져서 보이지 않는 높이는 pop으로 제거하면 항상 sorting 돼있음
left, right = [], [] # [[높이, 번호], ..]
MAX = float('inf')

# 좌우로 보이는 빌딩의 개수, 최종 정답
result = [0 for _ in range(N)]

# 좌, 혹은 우측에 보이는 빌딩 중 가장 가까운 인덱스 저장
near_l = [MAX for _ in range(N)]
near_r = [MAX for _ in range(N)]


# 각 건물에서 오른쪽을 보는 과정 (우 -> 좌 이동)
for i in range(N-1, -1, -1):
    # 새로 들어오는 것보다 낮거나 같으면 전부 pop, 어차피 안 보임
    while right and right[-1][0] <= h_lst[i]: right.pop()
    result[i] += (len(right))

    if right: near_r[i] = right[-1][1]
    right.append([h_lst[i], i+1])

# 각 건물에서 왼쪽을 보는 과정, 똑같음
for i in range(N):
    while left and left[-1][0] <= h_lst[i]: left.pop()
    result[i] += len(left)

    if left: near_l[i] = left[-1][1]
    left.append([h_lst[i], i+1])

# 위의 결과를 바탕으로 좌측과 우측에 보이는 건물 중 가장 가까운 건물 계산
near = []
for i in range(N):
    ldist, rdist = abs(i+1-near_l[i]), abs(i+1-near_r[i])
    if ldist == MAX: near.append(near_r[i])     # 좌측 안보임
    elif rdist == MAX: near.append(near_l[i])   # 우측 안보임
    else: near.append(near_l[i] if ldist <= rdist else near_r[i])


for see, n in zip(result, near):
    if see: print(see, n)
    else: print(0)
