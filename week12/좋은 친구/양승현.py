from collections import defaultdict

N, K = map(int, input().split())
name_len = [len(input()) for _ in range(N)] # 이름 길이 리스트
in_bound = defaultdict(int)                 # 윈도우 내의 {길이: 이름 개수}

res = l = r = 0

while r < len(name_len):
    # l을 증가시켜 좌측 윈도우 축소
    if K < r:                   # K < r이면 l을 움직여서 윈도우 이동
        out_ = name_len[l]  
        l += 1

        in_bound[out_] -= 1

    # r을 증가시켜 우측 윈도위 확장
    in_ = name_len[r]
    r += 1

    # 윈도우 내의 이름 길이가 같은 친구들이 찐친 
    res += in_bound[in_]

    in_bound[in_] += 1

print(res)
