n = int(input())
eggs = [list(map(int, input().split())) for _ in range(n)]
max_ = -1
def dfs(depth, sum):
    global max_

    if depth == len(eggs):
        max_ = max(max_, sum)
        return
    
    hp, power = eggs[depth]
    if hp <= 0:
        dfs(depth+1, sum)
        return
    
    for i in range(len(eggs)):
        if i == depth:
            continue
        hp2, power2 = eggs[i]
        
        if hp2 <= 0:
            continue

        #set var
        hp -= power2
        hp2 -= power
        if hp <= 0:
            sum += 1
        if hp2 <= 0:
            sum += 1
        eggs[depth] = [hp, power]
        eggs[i] = [hp2, power2]
        
        dfs(depth+1, sum)

        #rollback var
        if hp <= 0:
            sum -= 1
        if hp2 <= 0:
            sum -= 1
        hp += power2
        hp2 += power
        eggs[depth] = [hp, power]
        eggs[i] = [hp2, power2]

    #모든 계란이 깨져 있는 경우
    max_ = max(max_, sum)
dfs(0, 0)
print(max_)