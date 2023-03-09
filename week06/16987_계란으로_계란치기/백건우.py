n = int(input())

eggs = []
for _ in range(n):
    eggs.append(list(map(int, input().split()))) #  내구도 무게

def dfs(eggIdx):
    global ans
    if eggIdx == len(eggs):  # 마지막 계란까지 다 들었으면 깨진 계란 개수 센다.
        cnt = 0
        for egg in eggs:
            if egg[0] <= 0 :
                cnt += 1
        ans = max(ans,cnt)
        return
    if eggs[eggIdx][0] <= 0 : # 손에 든 계란이 이미 깨진 계란이면 다음으로 넘어간다.
        dfs(eggIdx+1)
        return

    isAllBroken = True # 현재 손에 든 계란 말고 다 깨졌으면 나머지 계란 개수 세고 끝낸다.
    for targetIndex in range(n):
        if targetIndex == eggIdx: continue
        if eggs[targetIndex][0] > 0:
            isAllBroken = False
            break
    if isAllBroken:
        ans = max(ans, n - 1)
        return

    for i in range(n):
        if i == eggIdx or eggs[i][0] <= 0: # 현재 손에 든 계란이면 다음으로 넘어간다.
            continue
        elif eggs[i][0] > 0: # 계란을 깰 수 있으면 깬다.
            eggs[i][0] -= eggs[eggIdx][1]
            eggs[eggIdx][0] -= eggs[i][1]
            dfs(eggIdx + 1)
            eggs[i][0] += eggs[eggIdx][1]
            eggs[eggIdx][0] += eggs[i][1]

curEgg = 0
ans = 0
# 내구도 무게
for i in range(n):
    if i == curEgg :
        continue
    if eggs[i][0] > 0 :
        eggs[i][0] -= eggs[curEgg][1]
        eggs[curEgg][0] -= eggs[i][1]
        dfs(curEgg+1)
        eggs[i][0] += eggs[curEgg][1]
        eggs[curEgg][0] += eggs[i][1]
print(ans)
