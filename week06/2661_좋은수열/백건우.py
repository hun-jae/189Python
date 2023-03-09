n = int(input())

def dfs(s, idx):
    if idx == n:
        print(s)
        exit(0) # 작은 숫자부터 정답 숫자에 추가하기 때문에 가장 처음으로 들어오는 숫자가 정답임. 처음엔 이거 생각 못하고 계속 dfs 돌렸다가 시간초과남
    # 1~3 까지 숫자를 넣어준다.
    for i in range(1, 4):
        if str(i) == s[-1]: # 마지막 숫자랑 같으면 안됨
            continue
        if isGood(s + str(i)) : # 좋은 단어일 때
            dfs(s+str(i), idx+1)

def isGood(s): # 문자열의 절반 길이까지만 탐색하면됨
    for i in range(1, len(s)//2+1):
        if s[len(s)-i:] == s[len(s)-2*i:len(s)-i] : # 기존 숫자는 이미 좋은 수열이고 새로운 수가 추가된 부분만 좋은수열인지 판별하면 된다.
            return False
    return True

for i in range(1, 4):
    dfs(str(i), 1)
