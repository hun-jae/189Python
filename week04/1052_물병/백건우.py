# 문제는 n을 2의 n제곱 꼴로 만들면 된다.
twoPow = []
for i in range(24,0,-1):
    twoPow.append(2**i)

n, k =map(int,input().split())
if n <= k :  # n이 k보다 작으면 그대로 들고가면 된다.
    print("0")
    exit(0)
nums = []
for i in range(k-1):  # k-1개 까지 2의 n제곱을 찾는다. 
    for j in range(len(twoPow)):
        if n >= twoPow[j] :  # n보다 작은 수 중에서 가장 큰 2의 n제곱을 찾아서 nums에 집어넣는다.
            n -= twoPow[j]
            nums.append(twoPow[j])
            break
nums.append(n) # 2의 n제곱들을 찾고난 뒤 남은 숫자를 2의 n제곱으로 만들면 문제가 풀린다. 
ans = 0

# 1. 2의 n제곱을 모두 찾고난 뒤 남은 수는 1인데 그것까지 집어넣고도 배열의 길이가 k보다 짧다면 물을 더 살 필요가 없다.
# 2. num[-1]은 k-1번까지 찾고 남은 n인데 그게 2의 n제곱 or 1 or 0 이면 물을 더 살 필요가 없다. 
if len(nums) < k or nums[-1] in twoPow or nums[-1] == 1 or nums[-1] == 0:  
    ans = 0
# 3. num[-1]이 2의 n제곱이 아니면 2의 n제곱으로 만들어야한다.
elif not nums[-1] in twoPow:
    twoPow.reverse()
    for i in range(len(twoPow)):
        if twoPow[i] > nums[-1] :
            ans = twoPow[i] - nums[-1]
            break
print(ans)
