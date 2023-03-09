# 순열로 가능한 숫자 모두 구한다.
a, b = input().split()
nums = list(a)
b = int(b)

def dfs(idx):
    global lenNum, ans, b
    if idx == lenNum: # 숫자 순서 다 정해지면 값 비교
        if nums[seq[0]] == '0' : # 시작숫자가 0 이면 빠져나간다.
            return
        temp = '' # 뽑은 순서대로 숫자 만든다.
        for cur in seq:
            temp += str(nums[cur])
        temp = int(temp)
        if temp < b  : # 정답 
            if ans == -1 :
                ans = temp
            else :
                ans = max(ans, temp)
        return

    for i in range(lenNum):  # 순열로 숫자 뽑는 부분
        if visit[i] :
            continue
        visit[i] = True
        seq[idx] = i
        dfs(idx+1)
        visit[i] = False

lenNum = len(nums)
visit = [False for _ in range(lenNum)]  
seq = [0 for _ in range(lenNum)] # 숫자 순서 저장
ans = -1 # 초기 정답은 -1
for i in range(lenNum): # 순열로 숫자 뽑는다.
    visit[i] = True
    seq[0] = i
    dfs(1)
    visit[i] = False
print(ans)
