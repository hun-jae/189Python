from collections import deque

N = int(input())
seq = [int(x) for x in input().split()]
q = deque([(x, i+1) for i, x in enumerate(seq)])

# order q to have next pop in index 0
while q:
    move, num = q.popleft()
    print(num, end=' ')
    if not q: break

    if 0 < move:
        q.rotate(-move+1)
    else:
        q.rotate(-move)
