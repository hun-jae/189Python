N = int(input())            # number of nodes
graph = {}                  # graph[node_num] = [left, right]
root = set(range(1, N+1))   # root candidates

for _ in range(N):
    node_num, left, right = map(int, input().split())
    if left in root: root.remove(left)      # root cannot be a child
    if right in root: root.remove(right)
    graph[node_num] = [left, right]

root = root.pop()

# level_min[level] = minimum node number in the level
level_min = [N + 1] * (N + 1)
level_max = [0] * (N + 1)
cnt = 0     # current node number := inorder guarantees the order

def inorder(n, level):
    global cnt
    l, r = graph[n]

    # traverse left
    if 0 < l: inorder(l, level+1)

    # visit current node
    cnt += 1
    level_min[level] = min(level_min[level], cnt)
    level_max[level] = max(level_max[level], cnt)

    # traverse right
    if 0 < r: inorder(r, level+1)


inorder(root, 1)

# find the level with the maximum width
opt_level, opt_width = 1, 0
for lev, (min_, max_) in enumerate(zip(level_min, level_max)):
    if opt_width < max_ - min_:
        opt_level, opt_width = lev, max_ - min_

print(opt_level, opt_width+1)
