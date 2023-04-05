for tc in range(1, int(input())+1):
    N = int(input())
    arr = [int(x) for x in input().split()]

    res = prev = -float('inf')
    for n in arr:
        prev = max(n, prev+n)
        res = max(res, prev)

    print(res)
