#시간 초과 실패
l = int(input())
ad = input()

for i in range(1, l+1) : # 가능한 광고의 길이는 1부터 n까지, 처음 시작부분 부터 길이가 1~l인 부분 수열을 고르고 탐색한다.
    isCorrect = True
    cur = ad[:i]
    for j in range(i,l,i):
        if not cur.startswith(ad[j:j+i]):
            isCorrect = False
            break
    if isCorrect :
        print(i)
        break
