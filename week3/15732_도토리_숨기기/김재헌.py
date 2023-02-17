N, K, D = map(int, input().split())
ruleList = []
for i in range(K):
    ruleList.append(list(map(int, input().split())))
start = 1
end = N
while start <= end:
    mid = (end + start) // 2
    sum = 0
    for s, e, arith in ruleList:
        if s > mid:
            continue
        sum += (min(e, mid) - s) // arith + 1
        if sum >= D:
            end = mid - 1
            answer = mid
            break
    if sum < D:
        start = mid + 1
print(answer)