/**
*  pypy로만 통과. 현재 right에서 구간의 합이 k를 넘겼다면 이후의 right가 가리키는 수가 전부 양수이므로 이후의 right모두 통과한다.
*  싫은 데요 처럼 누적합으로 바꾸면 python으로 통과할 듯 귀찮으니까 패스
*/
import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
k = int(input())

left, right = 0, 0
ans = 0
while right < n:
    cur = sum(nums[left:right+1])
    if cur > k :
        ans += n - right
        left += 1
        if left > right :
            right += 1
    else :
        right += 1
print(ans)
