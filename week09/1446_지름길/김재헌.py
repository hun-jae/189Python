import heapq

# 각 s, t 를 노드라고 생각하자 그리고 받아오는 것은 노드 간의 거리
# 시작노드에서 갈 수 있는 거리는 모두 각자의 거리로 초기화
# 시작노드에서의 지름길은 거리 다시 설정해줌
# 이후 가장 짧은 거리의 노드를 찾아서 해당노드에서 뻗어가는 친구들 거리 세팅
N, D = map(int, input().split())
max_loc = 0
min_loc = int(1e9)
graph = [[] for _ in range(D+1)]
distance = [int(1e9)] * (D+1)

for i in range(N):
    s, t, d = map(int, input().split())
    if t > D or t-s <= d:
        continue
    max_loc = max(max_loc, t)
    graph[s].append((t, d))
    if s!=0:
        graph[0].append((s, s))
    graph[0].append((t, t))

# for t, d in graph[0]:
#     distance[t] = min(distance[t], d)
print(graph[0])
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        #print(q)
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for next in graph[node]:
            cost = distance[node] + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))
        # print(distance[0], end=", ")
        # print(distance[10], end=", ")
        # print(distance[50], end=", ")
        # print(distance[70], end=", ")
        # print(distance[80], end=", ")
        # print(distance[140], end=", ")
        # print(distance[160], end=", ")
        # print(distance[180], end=", ")
        # print(distance[190], end=", ")
        # print(distance[450], end=", ")
        # print(distance[900])
dijkstra(0)

# for node in node_set:
#     print(node, distance[node])
print(D - max_loc + distance[max_loc])