n, m = map(int, input().split())
T = list(map(int, input().split()))

if m == 0:
    res = 0
elif m == 1 :
    res = max(T)
elif m > 1:
    i, j = 0, m-1
    res = sum(T[i:j+1])
    cur = sum(T[i:j+1])

    for j in range(m, n):
        cur += T[j]
        cur -= T[i]
        res = max(res, cur)
        i += 1

print(res)
