import sys
from collections import Counter

input = sys.stdin.readline
N = int(input())
nums = list(map(int,input().split()))

stack = []
cnt = Counter(nums) #각 원소의 개수를 딕셔너리에 담는다. 시간 복잡도 N

# 아래가 처음 시도 count함수가 N번 반복되기 때문에 시간 복잡도가 최대 N*N이다.
# cnt = {}
# for num in set(nums):
#     cnt[num] = nums.count(num)

ans = [-1 for _ in range(N)]

for idx in range(N-1,-1,-1):
    while len(stack) > 0 and cnt[stack[-1]] <= cnt[nums[idx]] : #현재 위치의 원소보다 더 적게 출연한 원소를 스택에서 뺀다.
        stack.pop()
    if stack :
        ans[idx] = stack[-1]
    stack.append(nums[idx])

for num in ans :
    print(num,end=" ")
