
#테스트 케이스의 수
T = int(input())

for times in range(T):

    N = int(input())
    note1 = list(map(int, input().split(' ')))

    M = int(input())
    note2 = list(map(int, input().split(' ')))

    note1.sort()

    for i in range(M):
        num = note2[i]
        l = 0
        r = N - 1
        answer = 0
        while l <= r:
            mid = (l + r) // 2
            if note1[mid] == num:
                answer = 1
                break
            elif note1[mid] < num:
                l = mid + 1
            elif note1[mid] > num:
                r = mid - 1
        print(answer)