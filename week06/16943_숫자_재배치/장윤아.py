def dfs(idx, word):
    global res, visited
    if idx == len(A):
        if int(word) < int(B) and int(word)>res:
            res = int(word)
        return

    for i in range(len(A)):
        if idx==0 and A[i]=='0': continue
        #if idx==0 and int(A[i]) > int(B[0]): continue

        if not visited[i]:
            visited[i] = 1
            dfs(idx+1, word+A[i])
            visited[i] = 0

dfs(0, '')
print(res)
