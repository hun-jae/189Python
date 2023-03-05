stack = list(input())
sum = 0 #전체 조각 수
cnt = 0 #현재 쇠막대기의 수
for i in range(len(stack)):
    if stack[i] == ")":
        cnt -= 1 #쇠막대기가 끝나든 레이저이든 )가 나오면 현재 쇠막대기 개수를 줄여줌
        if stack[i-1] == "(": #레이저이면
            sum += cnt
            sum -= 1
    elif stack[i] == "(": #쇠막대기이든 레이저이든 (가 나오면 현재 쇠막대기 개수와 전체 수를 늘려줌
        cnt += 1
        sum += 1
print(sum)