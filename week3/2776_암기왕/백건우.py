# import sys
# input = sys.stdin.readline

# T = int(input())        # 테스트 케이스의 개수
# for _ in range(T):
#     N = int(input())
#     yeon = set(map(int, input().split())) # set으로 입력받아야 시간초과 안남
#     M = int(input())
#     diary = list(map(int, input().split()))
#     for num in diary: # diary를 순회해 set안에 존재하는지 찾는다.
#         if num in yeon :
#             print("1")
#         else:
#             print("0")

import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    yeon = list(map(int, input().split()))
    yeon.sort()
    M = int(input())
    diary = list(map(int, input().split()))
    for num in diary:
        l = 0
        r = len(yeon)-1
        isIn = False
        while l <= r:
            mid = (l+r)//2
            if yeon[mid] == num :
                isIn = True
                break
            elif yeon[mid] > num :
                r = mid-1
            else :
                l = mid +1
        if isIn :
            print("1")
        else :
            print("0")
