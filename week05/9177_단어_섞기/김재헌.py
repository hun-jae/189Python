n = int(input())
for tc in range(1, n+1):
    a, b, c = input().split()
    a += " "
    b += " "
    stack = [] #(pa, pb, pc)
    pa, pb, pc = 0, 0, 0 # pointA, pointB, pointC
    while True:
        if pa==len(a) and pb == len(b):
            break
        if c[pc] != a[pa] and c[pc] != b[pb]: #틀린 경우
            if not stack:
                break
            pa, pb, pc = stack.pop()
            pb += 1
            pc += 1

        elif c[pc] == a[pa] and c[pc] == b[pb]: # 둘 다 되는 경우엔
            #a 넣고 stack에 넣어줌
            stack.append((pa, pb, pc))
            pa += 1
            pc += 1
        else:
            if a[pa] == c[pc]:
                pa += 1
                pc += 1
            else:
                pb += 1
                pc += 1
        if pc == len(c):
            break
    if pc==len(c):
        print(f"Data set {tc}: yes")
    else :
        print(f"Data set {tc}: no")