N = int(input())
res = 0
weight = [0] * N
cap = [0] * N

for i in range(N):
    cap[i], weight[i] = map(int, input().split())

def bt(cnt):
    global res

    if cnt == N:    # base case
        res = max(res, len([n for n in cap if n <= 0]))
        return

    if cap[cnt] <= 0:   # current egg is broken
        bt(cnt+1)
        return

    hit_cnt = 0
    for i in range(N):
        if i == cnt: continue       # same egg
        if cap[i] <= 0: continue    # broken egg
        hit_cnt += 1

        cap[cnt] -= weight[i]
        cap[i] -= weight[cnt]
        bt(cnt+1)
        cap[cnt] += weight[i]
        cap[i] += weight[cnt]

    if hit_cnt == 0:                # no egg is hit
        bt(cnt+1)


bt(0)
print(res)
