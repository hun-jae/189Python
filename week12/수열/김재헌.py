n,k = map(int,input().split())
arr = list(map(int,input().split()))
sum_ = max_ = sum(arr[:k])
for i in range(n-k):
    sum_ = sum_ + arr[i+k] - arr[i]
    max_ = max(max_, sum_)
print(max_)
