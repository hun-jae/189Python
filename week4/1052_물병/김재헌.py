# #코드 길이 줄임
n, k = map(int, input().split())
while True:
    k-=1
    for i in range(25):
        if 2**i >=n:
            if k==0 or 2**i==n:
                print(2 ** i - n)
                exit(0)
            n-=2**(i-1)
            break

#직관적인 코드
# n, k = map(int, input().split())
# while k>1:
#     k-=1
#     for i in range(25):
#         if 2**i >n:
#             n-=2**(i-1)
#             break
#         if 2**i == n:
#             print(0)
#             exit(0)
#
# for i in range(25):
#     if 2**i == n:
#         print(0)
#         break
#     if 2**i > n:
#         print(2**i - n)
#         break