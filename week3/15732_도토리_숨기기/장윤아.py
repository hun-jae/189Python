n, k, d = map(int, input().split())
rules = [list(map(int, input().split())) for _ in range(k)]

left, right = 1, n
while left <= right:
    mid = (left+right)//2 #도토리가 들어있는 마지막 상자 번호
    cnt = 0
    for rule in rules:
        start, end, gap = rule
        
        if mid < start: continue #마지막 상자가 start보다 앞쪽이면 안됨
        cnt += (min(end,mid)-start) // gap + 1

    if cnt >= d:
        right = mid - 1
        res = mid

    elif cnt < d:
        left = mid + 1

print(res)


'''
기존 아이디어
import sys
input = sys.stdin.readline
n, k, d = map(int, input().split())
boxes = []
for _ in range(k):
    start, end, gap = map(int, input().split())
    boxes.append(start)
    while True:
        start += gap
        if start <= end:
            boxes.append(start)
        else:
            break

boxes.sort()
res = 0
left, right = 0, n

while left <= right:
    mid = (left+right)//2
    if mid+1 == d:
        res = boxes[mid]
        break
    elif mid+1 < d:
        mid = right + 1
    elif mid+1 > d:
        mid = left - 1

print(res)
'''
