import sys

input = sys.stdin.readline

n = int(input())
rooms=[]
for _ in range(n):
    num, start, end = map(int,input().split())
    rooms.append([start,end])
rooms.sort(key=lambda x:(x[1], x[0]))

ans = 0
# while문을 돌면서 한 강의실씩 가능한 수업을 구하는 식으로 할려고 했는데 시간초과났음
# while문 한번이 강의실 한 개임 while문 끝나고 다시 돌면 강의실이 1개 새로 생긴것
visit = [False for _ in range(n)]
while visit.count(False) > 0:
    ans += 1  # while문의 반복 횟수 = 강의실의 개수
    last = 0
    for idx, room in enumerate(rooms):
        if visit[idx] : continue  # 이미 이전 강의실에 배정된 수업이면 넘어간다.
        curStart, curEnd = room 
        if curStart >= last :   # 현재 강의실에 배정가능한 수업이면 배정한다.
            visit[idx] = True
            last = curEnd
print(ans)
