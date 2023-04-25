n, m = map(int, input().split())
money = list(map(int, input().split()))
max_ = sum_ = sum(money[:m])
for i in range(n-m):
    sum_ = sum_ - money[i] + money[i+m]
    max_ = max(max_, sum_)
print(max_)
