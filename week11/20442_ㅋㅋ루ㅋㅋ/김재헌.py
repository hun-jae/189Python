#맨왼쪽K와 맨 오른쪽 K 내부에 있는 R의 개수(:=cnt_r)를 세자 (전체 R의 개수도 세야함)
#max_값은 전체 R의 수로 잡고 시작
#처음값을 2 + cnt_r로 잡고 이후 K를 하나씩 좁혀가면서 (+2 - 빠진R의개수)
#내부의 R이 다 사라지면 break
#남아있다면 max_ 비교 후 continue
arr = list(input())
left = right = -1
ans = cnt_r = cnt_r_after_k = 0
for idx, cur in enumerate(arr):
    if cur == "K":
        cnt_r_after_k = 0
        if left == -1:
            left = idx
        right = idx

    else:
        ans += 1
        if left != -1:
            cnt_r_after_k += 1
            cnt_r += 1

cnt_r -= cnt_r_after_k

val = 2 + cnt_r
while cnt_r > 0:
    ans = max(ans, val)
    cur_cnt = 0

    for l in range(left+1, right+1):
        if arr[l] == "K":
            left = l
            break
        else:
            cur_cnt += 1

    for r in range(right-1, left-1, -1):
        if arr[r] == "K":
            right = r
            break
        else:
            cur_cnt += 1
    cnt_r -= cur_cnt #cnt_r := K내부에 있는 R의 개수
    val += (2-cur_cnt)

print(ans)