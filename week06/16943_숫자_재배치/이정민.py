def permutation(cnt, N, max_list, Number, visited):
    if cnt == N:
        num = ""
        for j in range(N):
            num+=str(Number[-1-j])
        if int(num) < int(B) and len(str(int(num)))==N:
            max_list.append(int(num))
        return

    for i in range(N):
        if visited[i] != True:
            visited[i] = True
            Number[cnt] = A[i]
            permutation(cnt+1, N,max_list, Number,visited)
            visited[i] = False



A, B = map(str, input().split())

max_ = -1
N = len(A)

Number = [0]*N
max_list=[]
visited = [False]*N

permutation(0, N, max_list, Number, visited)
if max_list:
    print(max(max_list))
else:
    print(-1)