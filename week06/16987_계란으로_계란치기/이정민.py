N = int(input())

#내구도 저장
strong = []
#무게 저장
weight = []

for _ in range(N):
    s, w = map(int, input().split(' '))
    strong.append(s)
    weight.append(w)

answer = []

def dfs(egg, strong, weight, N, answer):
    if egg == N:
        count = 0
        #깨진 계란 개수 세기
        for e in strong:
            if e <= 0:
                count += 1
        #깨진 계란 수 저장
        answer.append(count)
        return
    #깰 수 있는 계란이 있는지 확인
    find = False
    for i in range(N):
        #이미 든 계란
        if i == egg:
            continue
        #든 계란이 이미 깨진 경우
        if strong[egg] <= 0:
            continue
        #깨진 계란은 패스
        if strong[i] <= 0:
            continue
        #하나라도 깨진 경우
        find = True
        strong[egg] -= weight[i]
        strong[i] -= weight[egg]
        dfs(egg+1, strong, weight, N, answer)
        strong[egg] += weight[i]
        strong[i] += weight[egg]
    #계란이 하나도 안 깨진 경우
    if find == False:
        dfs(egg+1, strong, weight, N, answer)

dfs(0, strong, weight, N, answer)
print(max(answer))