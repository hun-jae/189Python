A, B = input().split()
res = -1
visited = set()

def bt(cnt, temp):
    global res
    if cnt == len(A):
        res = max(res, int(temp))
        return

    for i in range(len(A)):
        # conditions: no leading zero, no duplication, no bigger than B
        if int(temp + A[i]) == 0: continue
        if i in visited: continue
        if len(B) <= len(A) and int(B[:cnt + 1]) < int(temp + A[i]): continue

        visited.add(i)
        bt(cnt+1, temp+A[i])
        visited.remove(i)


bt(0, '')
print(res)
