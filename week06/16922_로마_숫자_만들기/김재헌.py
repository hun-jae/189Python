# 주석친 코드는 시간초과가 날거라서 수정한 코드
# n = int(input())
# nums = set()
#
# def search(depth, num):
#     if depth == n:
#         nums.add(num)
#         return
#     for i in [1, 5, 10 ,50]:
#         search(depth + 1, num + i)
#
# search(0, 0)
# print(len(nums))

# 이전에 시작했던 숫자부터 시작해서 중복을 제거
n = int(input())
nums = set()
numList = [1, 5, 10, 50]


def search(depth, num, start):
    if depth == n:
        nums.add(num)
        return
    for i in range(start, 4):
        search(depth + 1, num + numList[i], i)


search(0, 0, 0)
print(len(nums))
