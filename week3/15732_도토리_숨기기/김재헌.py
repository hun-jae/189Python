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
        if sum >= D: #룰 하나씩마다 체크를 해주자
                     #해당 룰을 체크했을때 최대 도토리 넘어갔다면
                     #해당 위치보다 작거나 같은곳에 마지막 도토리 존재
            end = mid - 1
            answer = mid
            break
    if sum < D: # 다 돌았는데 마지막 도토리 못찾았으면 해당 위치보다 뒤에 있음
        start = mid + 1
print(answer)