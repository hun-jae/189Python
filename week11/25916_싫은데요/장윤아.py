N, M = map(int, input().split()) #구멍개수, 부피
sizes = list(map(int, input().split()))

# 합이 M 이하이면서 연속된 수들의 합의 최대
res = 0
if N==1:
    if sizes[0] <= M :
        res = sizes[0]
    elif sizes[0] > M:
        res = 0
elif N>1:
    left, right = 0, 1
    total = 0
    if sizes[left] <= M:
        total += sizes[left]

    while left <= right and right < N:
        if total + sizes[right] <=M:
            total += sizes[right]
            right += 1

        elif total + sizes[right] > M:
            if sizes[right]>M and right+1 <= N-1:
                left = right+1
                right += 1
                total = 0
            else:
                total -= sizes[left]
                left += 1

        res = max(res, total)

print(res)
