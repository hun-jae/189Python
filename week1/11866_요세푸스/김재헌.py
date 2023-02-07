from collections import deque
n, k = map(int, input().split())
que = deque([i for i in range(1,n+1)])
result = []
cnt = 0
while que:
    for i in range(k-1):
        que.append(que.popleft())
    result.append(que.popleft())
print("<", end="")
for i in range(n-1):
    print(result[i], end=", ")
print(result[n-1], end="")
print(">")
