import heapq
import sys

input = sys.stdin.readline

n = int(input())
noodles = []
t = 0

#입력 받는 부분
for _ in range(n):
    deadline, noodleCnt = map(int,input().split())
    noodles.append([deadline,noodleCnt])
# 데드라인의 오름차순, 컵라면 개수의 내림차순으로 정렬
noodles.sort(key=lambda x:(x[0],-x[1]))
# 완료된 숙제를 담는 배열 heapq로 컵라면 개수의 오름차순으로 우선순위큐 사용할꺼임, q의 길이가 숙제의 개수 = 지금까지 걸린시간
q = []
for noodle in noodles:
    deadline, noodleCnt = noodle
    
    # 지금까지 완료된 숙제가 없으면 바로 넣으면 된다.
    if not q :  
        heapq.heappush(q,noodleCnt)
        
    # q의 길이가 현재까지 완료한 숙제를 완성하는데 걸린 시간인데 그게 데드라인보다 적으면 그냥 넣으면 된다.
    elif len(q) < deadline :
        heapq.heappush(q, noodleCnt)
        
    # 만약 지금까지 완료한 숙제때문에 지금 하려는 숙제가 데드라인을 넘긴 경우
    elif len(q) == deadline :
        
        # 지금 하려는 숙제의 컵라면 개수가 지금까지 한 숙제의 컵라면 개수의 최소값보다 크다면 그걸 빼고 지금껄 대신 하면된다.
        if noodleCnt > q[0]:
            heapq.heappop(q)
            heapq.heappush(q,noodleCnt)

print(sum(q))
