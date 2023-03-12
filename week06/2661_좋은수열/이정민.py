N = int(input())

permu = []

def dfs(cnt, permu):
    if cnt == N:
        for p in permu:
            print(p, end = '')
        exit(0)

    for i in range(1, 4):
        permu.append(i)
        check = False
        #최대로 확인해야 되는 경우가 문자열 반이니까 범위도 문자열의 반
        for j in range(1, len(permu)//2+1):
            #끝에서부터 인접 문자열 길이를 늘리며 확인
            if permu[-j:] == permu[-2*j:-j]:
                check = True
                break
        if check == False:
            dfs(cnt+1, permu)
        permu.pop()

dfs(0, permu)