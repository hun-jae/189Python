import sys
import math
input = sys.stdin.readline

N, M = map(int, input().split(" "))
#색깔별 보석 개수를 저장할 배열
colors = []

for i in range(M):
    colors.append(int(input()))

l = 1
#질투심이 최대가 되는 경우
r = max(colors)

while l <= r :
    #보석을 나눠준 학생의 수
    count = 0
    mid = (r+l)//2
    for c in colors:
            #나머지가 남는 경우를 고려하여 ceil 사용
            count = count + math.ceil(c/mid)
    if count <= N:
        r = mid - 1
    else:
        l = mid + 1

print(l)
