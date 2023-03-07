from functools import lru_cache

N = int(input())
res = set()

@lru_cache(maxsize=1_000_000)
def bt(cnt, temp):
    if cnt == N:
        res.add(temp)
        return

    for add in [1, 5, 10, 50]:
        bt(cnt+1, temp+add)

bt(0, 0)
print(len(res))
