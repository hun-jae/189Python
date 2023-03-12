N = int(input())
num = [1, 5, 10, 50]
count = 0
numbers = [0]*N
tmp = []

def combination(start, cnt, num, N, numbers, tmp):
    if cnt == N:
        tmp.append(sum(numbers))
        return

    for i in range(start, 4, 1):
        numbers[cnt] = num[i]
        combination(i, cnt+1, num, N, numbers, tmp)

combination(0, 0, num, N, numbers, tmp)

answer = set(tmp)

print(len(answer))