# 루트부터 순서대로 진행
# 왼쪽으로 쭉 가고
# dfs함수는 왼쪽으로 갈 때 자신의 부모의 위치, depth를 알려줘야함
#                      return은 자신의 자식 노드의 총 개수
#         오른쪽으로 갈땐 자신의 위치, depth를 알려줘야함
#                      return 은 알빠아님
import sys

sys.setrecursionlimit(100000)

n = int(input())
tr = [[] for _ in range(n + 1)]
min_ = [100000 for _ in range(n + 1)]
max_ = [0 for _ in range(n + 1)]
check_root_node = [True for _ in range(n + 1)]

for i in range(n):
    x, l, r = map(int, input().split())
    if l != -1:
        check_root_node[l] = False
    if r != -1:
        check_root_node[r] = False
    tr[x] = [l, r]

for i in range(1, n + 1):
    if check_root_node[i]:
        root_node = i
        break


def dfs(v, num_left_nodes, depth):
    left, right = tr[v]

    if left != -1:
        left_child_nodes = dfs(left, num_left_nodes, depth + 1)
    else:
        left_child_nodes = 0

    position = num_left_nodes + left_child_nodes + 1

    if right != -1:
        right_child_nodes = dfs(right, position, depth + 1)
    else:
        right_child_nodes = 0
    num_child_nodes = left_child_nodes + right_child_nodes

    min_[depth] = min(min_[depth], position)
    max_[depth] = max(max_[depth], position)

    return num_child_nodes + 1


dfs(root_node, 0, 1)

max_width = 0
for i in range(1, n + 1):
    if max_[i] - min_[i] + 1 > max_width:
        max_width = max_[i] - min_[i] + 1
        max_row = i

print(max_row, max_width)
