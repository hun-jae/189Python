_, m = map(int, input().split())
days = list(map(int, input().split()))

cur = l = r = 0
res = -float('inf')

while r < len(days):
    if m <= r:
        cur -= days[l]
        l += 1

    cur += days[r]
    r += 1

    res = max(res, cur)

print(res)
