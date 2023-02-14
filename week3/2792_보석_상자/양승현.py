from math import ceil
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
colors = [int(input()) for _ in range(M)]

need_person = lambda bound: sum([ceil(c/bound) for c in colors])

l, r = 1, max(colors)+1
while l < r:
    mid = (l+r) // 2
    if need_person(mid) <= N:
        r = mid
    else:
        l = mid + 1

print(l)