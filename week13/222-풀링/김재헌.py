N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]


def find_second_num(arr):
    n = len(arr)
    if n == 2:
        second = first = -float('inf')

        for line in arr:
            for num in line:
                if num >= first:
                    second = first
                    first = num
                elif second <= num <= first:
                    second = num
        return second

    result_list = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            tmp_arr = []
            for k in range(i * n//2, (i+1) * n//2):
                tmp_arr.append(arr[k][j * n//2 : (j+1) * n//2])
            result_list[i][j] = find_second_num(tmp_arr)
    return find_second_num(result_list)


print(find_second_num(graph))
