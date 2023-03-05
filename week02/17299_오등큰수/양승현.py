from collections import Counter
import sys
input = sys.stdin.readline

N = int(input())
nums = [int(x) for x in input().split()]
# 해당 숫자의 등장 횟수를 기준삼아 right 리스트를 정렬 상태로 유지
# 그러면 특정 index에서 우측에 조건이 성립하는 수를 빠르게 탐색 가능
#   문제에서 요구하는 가장 왼쪽(오른쪽 역시) right의 양 끝에 존재하게 됨 -> O(1)
# right에 아무것도 없다면 성립하는 숫자가 없는 것이므로 -1 출력
cnt, right, res = Counter(nums), [], []

for i in range(N-1, -1, -1):
    while right and cnt[right[-1]] <= cnt[nums[i]]:     # 정렬
        right.pop()

    res.append(right[-1] if right else -1)
    right.append(nums[i])

for n in res[::-1]: print(n, end=' ')

