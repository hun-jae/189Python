t = int(input())
for test_case in range(t):
    n = int(input())
    note1 = list(map(int, input().split()))
    m = int(input())
    note2 = list(map(int, input().split()))

    note1.sort()
    for num in note2:
        ans = 0
        left, right = 0, len(note1)-1
        while left <= right:
            mid = (left+right) // 2

            if note1[mid] < num:
                left = mid+1
            elif note1[mid] > num:
                right = mid-1
            elif note1[mid] == num:
                ans = 1
                break
        print(ans)