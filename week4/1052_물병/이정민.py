#아직 풀이중...
#그리디라서 현재 값에서 뺄 수 있는 가장 큰 2의 제곱을 빼는 방식으로 풀면 된다고 생각했는데... 실패...
import math

N, K = map(int, input().split())

#N이 K보다 같거나 작으면 0 출력 후 종료
if( N <= K ):
    print(0)
    quit()

for i in range(K):
    #N 이하의 가장 큰 2의 제곱의 지수 찾기
    find = 0
    while(pow(2, find) < N):
        find = find+1
    N = N - pow(2, find-1)
    #N이 0 이면 K번 이하로 나누어 떨어진 것이므로 0 출력
    if N == 0:
        print(0)
        quit()

print(pow(2, find-1)-N)
