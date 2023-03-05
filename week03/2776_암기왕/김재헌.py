import sys
T = int(input())
for tc in range(T):
    n = int(input())
    note1 = sorted(list(map(int, sys.stdin.readline().split())))
    n2 = int(input())
    note2 = list(map(int, sys.stdin.readline().split()))

    for num in note2:
        l = 0
        r = n - 1
        while l <= r:
            mid = (l + r) // 2
            if note1[mid] == num:
                print(1)
                break
            elif note1[mid] < num:
                l = mid + 1
            elif num < note1[mid]:
                r = mid - 1
        else:
            print(0)