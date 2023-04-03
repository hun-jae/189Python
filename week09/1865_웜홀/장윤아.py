tc = int(input())
def bellman(start):
    distance = [int(1e9)]*(n+1)
    distance[start] = 0

    for i in range(n): #n번 도는 것
        for s, e, t in info:
            if distance[e] > t+distance[s]:
                distance[e] = t+distance[s]
                if i == n-1:
                    return True
    return False

for test_case in range(tc):
    n, m, w = map(int, input().split())
    info = []
    for i in range(m): #도로 정보
        s, e, t = map(int, input().split())
        info.append([s,e,t])
        info.append([e,s,t])
    for i in range(w): #웜홀 정보
        s, e, t = map(int, input().split())
        info.append([s,e,-t])

    if bellman(1) : print("YES")
    else: print("NO")
