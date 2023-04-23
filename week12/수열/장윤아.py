N, K = map(int, input().split()) #전체, 연속 일수
temperatures = list(map(int, input().split()))

if K==1:
    res = max(temperatures)
elif K>1:
    i, j = 0, K-1
    res = sum(temperatures[i:j+1])
    sumOfTemperature = sum(temperatures[i:j+1])
    for j in range(K, N):
        sumOfTemperature += temperatures[j]
        sumOfTemperature -= temperatures[i]
        res = max(res, sumOfTemperature)
        i += 1

print(res)
