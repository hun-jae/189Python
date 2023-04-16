#pypy3로 통과....
n = int(input())
numbers = list(map(int, input().split()))
k = int(input())

start = 0
end = start + 1

cnt = 0
sum_ = numbers[start]

while (start < end):
    if(sum_ <= k and end <= n-1):
        sum_ += numbers[end]
        end += 1
    elif(sum_ <= k and end == n):
        break
    elif (sum_ > k):
        sum_ -= numbers[start]
        start += 1
        cnt += n - end + 1

print(cnt)