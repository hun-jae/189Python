# lower_bound함수를 bisect 함수를 써서 풀려고 했는데 뭔가가 안됨
# 12738 가장 긴 증가하는 부분 수열 3 푸는 것처럼 품
# 배열 뒤집어서 가장 긴 증가하는 부분 수열 = 원래 배열의 가장 긴 감소하는 부분 수열
def lower_bound(target):
    left, right = 0, len(ans)

    while left < right:  # left와 right가 만나는 지점이 target값 이상이 처음 나오는 위치
        mid = (right + left) // 2

        if ans[mid] < target:
            left = mid + 1
        else:
            right = mid

    return right

n = int(input())
nums = list(map(int,input().split()))
ans = [1001]
for num in reversed(nums):
    if num > ans[-1]:
        ans.append(num)
    else:
        idx = lower_bound(num)
        ans[idx] = num
print(len(ans))
