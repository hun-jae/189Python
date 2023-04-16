n = int(input())

numbers = []
for i in range(n):
    numbers.append(int(input()))

start = 0
end = start + 1

dist_sum = sum(numbers)
right_sum = numbers[0]
ans = 0

while start < end:
    #print("start :  ", start, " end:  ", end," sum : ",tmp_sum)
    left_sum = dist_sum - right_sum
    if (right_sum <= left_sum and end <= n - 1):
        ans = max(ans, right_sum)
        right_sum += numbers[end]
        end += 1
    elif (right_sum <= left_sum and end == n):
        end = 0
        right_sum += numbers[end]
    elif (right_sum > left_sum):
        ans = max(ans, left_sum)
        right_sum -= numbers[start]
        start += 1

print(ans)