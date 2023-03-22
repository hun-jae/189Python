#4개 중 중복 허용하여 N개 뽑은 후, 각각의 합을 set으로 하여 길이를 구해준다.
rome = [1,5,50,10]
N = int(input())
mySet = set()
choice = [0]*N

def dfs(cnt):
    global choice
    if cnt == N:
        mySet.add(sum(choice))
        return

    for i in range(4):
        choice[cnt] = rome[i]
        if sum(choice) in mySet: continue
        dfs(cnt+1)
        choice[cnt] = 0

dfs(0)
print(len(mySet))