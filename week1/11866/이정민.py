n,k=map(int,input().split())
dp=[0]*n
answer=[]
for i in range(n):
    dp[i]=i+1
pick=0
for j in range(n):
    tmp = (pick+k-1) % (n-j)
    answer.append(dp[tmp])
    del dp[tmp]
    pick=tmp


a = ", ".join(map(str, answer))
print('<',a,'>',sep="")