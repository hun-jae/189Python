"""
case 1) N이 5보다 작거나 같은 경우 그냥 상수 출력
case 2) 아니면 상향식 dp 접근
    - 2원과 5원을 만드는 경우가 동전 1개를 쓰는 경우로 base case
    - dp[k] := k 원을 만들기 위해 필요한 최소 동전의 개수
"""

N = int(input())
if N <= 5:
    print([-1, -1, 1, -1, 2, 1][N])
    quit()

dp = [float('inf') for _ in range(N+1)]
dp[2] = dp[5] = 1

for i in range(1, N+1):
    if 2 <= i: dp[i] = min(dp[i], dp[i-2]+1)
    if 5 <= i: dp[i] = min(dp[i], dp[i-5]+1)

print(dp[N] if dp[N] < float('inf') else -1)