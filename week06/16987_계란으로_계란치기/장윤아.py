#푸는중

N = int(input())
eggs = [list(map(int, input().split())) for _ in range(N)]
broken = [int(1e9)]*N
res = 0
flag1, flag2 = False, False
tmp = 0

def crash(idx):
    global eggs, res, tmp, flag1, flag2, broken
    if idx == N-1:
        print(tmp)
        res = max(res, tmp)
        return

    if broken[idx] < 0: return

    for i in range(idx+1, N):
        if broken[i] < 0: continue #깨진계란

        #부딪히기
        broken[idx] = eggs[idx][0] - eggs[i][1]
        broken[i] = eggs[i][0] - eggs[idx][1]

        if broken[idx] < 0:
            print(f'{idx} 왼쪽 깨짐')
            tmp += 1
            crash(idx+1)
            broken[idx] = int(1e9)
            tmp -= 1

        if broken[i] < 0:
            print(f'{idx} 오른쪽 깨짐')
            tmp += 1
            break

crash(0)
print(res)
