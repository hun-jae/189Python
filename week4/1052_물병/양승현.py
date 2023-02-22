"""
Bit Manipulation
문제 재해석
    N: N을 이진수로 보고 계산 (1+1+...+1, N개)
    K: 이진수에서의 1의 개수가 K 이하여야함
    결국 N에 1씩 몇 번을 더해야 (구매) 1의 개수를 K개 이하로 만들 수 있을까?
* N & -N -> 비트열에서 마지막 1의 위치 반환하므로 바로 계산 가능
"""

N, K = map(int, input().split())

cnt = 0
while K < f'{N:b}'.count('1'):
    cnt += N & -N
    N += N & -N

print(cnt)

