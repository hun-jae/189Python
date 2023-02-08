from collections import deque
n = int(input())
#인덱스와, 종이의 숫자를 쌍으로 담아둠
inputs = list(map(int, input().split()))
que = deque([])
for i in range(1,n+1):
    que.append([i, inputs[i-1]])

idx, num = que.popleft()
result = [1]
while que:
    #하나가 빠지게 되면 양수일때는 한칸 덜 rotate해야함
    if num > 0:
        que.rotate(-(num-1))
    elif num < 0:
        que.rotate(-num)

    idx, num = que.popleft()
    result.append(idx)
for i in result:
    print(i, end=" ")

