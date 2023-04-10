# 12738 가장 긴 증가하는 부분 수열 3 푸는 것처럼 품
# 배열 뒤집어서 가장 긴 증가하는 부분 수열 = 원래 배열의 가장 긴 감소하는 부분 수열
import bisect as bs

n = int(input())
nums = list(map(int,input().split()))
ans = []
for num in nums[::-1]: # 배열을 뒤 부터 접근
    if not ans:
        ans.append(num)
    else:
        if num > ans[-1]:
            ans.append(num)
        else:
            ans[bs.bisect_left(ans,num)] = num
print(len(ans))
