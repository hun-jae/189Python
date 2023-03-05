N, K, D = map(int,input().split())
acorns = []
for _ in range(K):
    acorns.append(list(map(int,input().split())))
l = 1       # 상자의 최소 개수
r = 1000000 # 상자의 최대 개수
ans = 1000000
while l <= r :
    mid = (l+r)//2              # 마지막 도토리가 들어갈 상자를 이분 탐색으로 찾는다.
    cnt = 0
    for acorn in acorns :       # 선택한 상자(mid)까지 각 규칙을 통해 들어갈 도토리의 개수를 센다.
        start, end, itr = acorn
        if start <= mid <= end :# 선택한 상자가 규칙의 시작 지점보다 크고 끝 지점보다 작으면 시작지점부터 선택한 상자까지 들어갈 도토리의 개수를 센다.
            cnt += (mid-start)//itr + 1 # 시작 지점에도 도토리가 들어가니까 + 1 해줘야 한다.
        elif mid > end :        # 선택한 상자가 끝 지점보다 크다면 규칙의 시작부터 끝상자까지 들어갈 개수를 구한다.
            cnt += (end-start)//itr + 1

    if cnt >= D :
        r = mid - 1
        ans = min(mid, ans)
    else :
        l = mid + 1
print(ans)
