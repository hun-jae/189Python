def belman(start):
    minDis[start] = 0
    for i in range(1, n+1):
        # 매 반복마다 '모든 간선'을 확인한다.
        for j in range(1, n+1):
            for next, time in edges[j]:
                if minDis[next] > minDis[j] + time:  # 작은 값으로 갱신
                    minDis[next] = minDis[j] + time
                    if i == n : # 갱신이 계속되는 경우 음의 사이클
                        return True
    return False

T = int(input())
for tc in range(1, T+1):
    n, m, w = map(int, input().split()) # 지점의 수, 도로의 개수, 웜홀의 개수
    minDis = [100001 for _ in range(n+1)]
    edges = [[] for _ in range(n+1)]

    # 도로 입력, 도로는 방향 x, 시간+
    for _ in range(m):
        s, e, t = map(int, input().split())
        edges[s].append([e, t])
        edges[e].append([s, t])


    # 웜홀 입력, 웜홀은 방향 o, 시간-
    for _ in range(w):
        s, e, t = map(int, input().split())
        edges[s].append([e,-t])

    if belman(1): #  순환이 존재 한다면
        print("YES")
    else :
        print("NO")
