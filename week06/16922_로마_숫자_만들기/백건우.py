# 백트래킹으로 1, 5, 10 ,50 의 개수를 구하고 set을 이용해 중복 숫자를 제거한다.
n = int(input())

def dfs(idx, numCnt):
    global n, ans
    if 2 == idx :  # 50의 개수는 n - 이전 숫자들이 선택된 개수
        cnt[3] = n - numCnt
        temp = 0 # temp 통해 계산
        for num, curCnt in enumerate(cnt):
            temp += nums[num] * curCnt
        ans.add(temp)
        return
    for i in range(n-numCnt,-1,-1):
        cnt[idx+1] = i
        dfs(idx+1, numCnt+i)

ans = set()
cnt = [0 for _ in range(4)]
nums = [1,5,10,50]


for i in range(n,-1,-1): # 첫 번째 자리 수의 개수를 0 부터 n까지 고름
    cnt[0] = i  # 1,5,10,50 각각의 개수 저장
    dfs(0, i)
print(len(ans))
