#자기보다 작은것중 가장 큰 인덱스
n = int(input())
dp = []
arr = list(map(int, input().split()))

for i in range(n):
    max_ = 1
    for j in range(i):
        if dp[j][1] > arr[i]:
            max_ = max(max_, dp[j][0] + 1)
    dp.append((max_, arr[i]))

print(max(dp)[0])