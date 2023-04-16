n, m = map(int, input().split())

numbers = list(map(int, input().split()))

start = 0
end = start + 1

ans = 0
sum = numbers[0]

while start < end:
    if(sum > m):
        sum -= numbers[start]
        start += 1
    elif (sum <= m):
        ans = max(ans, sum)
        if(end >= n):
            break
        sum += numbers[end]
        end += 1
    if(start == end):
        if(start >= n):
            break
        sum = numbers[start]
        end += 1
print(ans)