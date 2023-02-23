n = int(input())

cnt5 = 0
cnt2 = 0
ans = 0
while True:
    if n%2 == 1 :   # n이 홀수이면 5를 빼줘서 짝수로 만든다.
        n -= 5
        cnt5 += 1
        if n < 0 :  # 5를 뺐을때 n이 0보다 작아진다면 이건 거스름돈을 주는게 불가능하다 -> -1 출력
            print("-1")
            exit(0)
    elif n%2 == 0 : # 먼저 2원짜리의 개수를 구한다.
        cnt2 += n//2
        break

while cnt2 >= 5:  # 2원 짜리 5개가 모이면 5원짜리 2개로 바꿔줄 수 있다.
    cnt2 -= 5
    cnt5 += 2
print(cnt2+cnt5)
