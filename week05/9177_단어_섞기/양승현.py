T = int(input())
for tc in range(1, T+1):
    w1, w2, target = input().split()
    dp = [[0] * (len(w2)+1) for _ in range(len(w1)+1)]
    dp[0][0] = 1
    for i in range(len(w1)+1):
        for j in range(len(w2)+1):
            if i > 0 and dp[i-1][j] and w1[i-1] == target[i+j-1]:
                dp[i][j] = 1
            if j > 0 and dp[i][j-1] and w2[j-1] == target[i+j-1]:
                dp[i][j] = 1
    print(f'Data set {tc}: {"yes" if dp[-1][-1] else "no"}')
