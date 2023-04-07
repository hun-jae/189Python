###   단순하게 표 채워보고 점화식 보이면 그대로 풀면 되는듯
#               k\n   1  2  3  4  5  6
#               1     1  1  1  1  1  1
#               2     2  3  4  5  6  7
#               3     3  6  10 15 21 18
#               4     4  10 20 25 46 64
###

n, k = map(int, input().split())

dp = [[0 for _ in range(n+1)] for _ in range(k+1)]
for i in range(1, n+1):
    dp[1][i] = 1   # k = 1 인 경우 자기자신 밖에 없으니까 무조건 1임
for i in range(1, k+1):
    dp[i][1] = i

for y in range(2, k+1):
    for x in range(2, n+1):
        dp[y][x] = dp[y-1][x]+dp[y][x-1]

print(dp[k][n]%1000000000)
