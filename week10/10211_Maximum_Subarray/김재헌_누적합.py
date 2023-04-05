T = int(input())
for tc in range(T):
    n = int(input())
    org_array = list(map(int,input().split()))
    prefix_array = [0]
    for idx, i in enumerate(org_array):
        prefix_array.append(prefix_array[idx] + i)
    max_ = -float('inf')
    for i in range(len(prefix_array)-1):
        for j in range(i+1, len(prefix_array)):
            max_ = max(max_, prefix_array[j] - prefix_array[i])
    print(max_)