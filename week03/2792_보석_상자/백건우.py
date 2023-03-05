# 질투심( 한 학생이 가질 수 있는 최대 개수의 보석)이 최소가 되어야한다.
# python으로 시간초과 pypy로만 통과함
#import sys
#input = sys.stdin.readline
# 위의 두 줄 추가하니까 python으로도 통과함 무조건 넣어야 할듯

N, M = map(int,input().split())
jewels = []
for _ in range(M):
    jewels.append(int(input()))

l = 1
r = max(jewels)  # 한 학생에게 줄 수 있는 보석의 최대 개수는 특정 색의 보석의 최대 개수
ans = 0
while l <= r :
    mid = (l+r)//2 # 질투심(=한 학생에게 최대로 나눠줄 수 있는 보석의 개수)
    cnt = 0
    for jewel in jewels: # 각 보석의 개수를 mid로 나누면 각 보석을 몇명의 학생들에게 나눠줄 수 있는지 알 수 있음
        cnt += jewel//mid
        if jewel%mid != 0 : # 보석의 나머지가 있다면 이것도 학생에게 분배해야 하니까 +1해야된다.
            cnt += 1
    if cnt <= N : #분배가 가능한 경우
        r = mid - 1
        ans =mid
    else : #분배가 불가능한 경우
        l = mid + 1
print(ans)
