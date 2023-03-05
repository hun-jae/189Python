from collections import deque

N = int(input())
seq = [int(x) for x in input().split()]
q = deque([(x, i+1) for i, x in enumerate(seq)])

# q에는 움직일 숫자와 자신의 번호가 튜플형태로 저장
# 다음에 터뜨릴 풍선은 항상 큐의 처음에 오도록 회전
while q:
    move, num = q.popleft()
    print(num, end=' ')
    if not q: break

    # move가 양수인 경우는 popleft()가 한 번의 연산을 대신하므로 -move+1
    q.rotate(-move+1 if 0 < move else -move)
