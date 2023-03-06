n = int(input())
guitar = [input() for _ in range(n)]
def sortGui(guitar):
    for i in range(len(guitar) - 1, 0, -1):
        for j in range(len(guitar)-1):
            flag = False
            if len(guitar[j]) > len(guitar[j + 1]):
                flag = True

            elif len(guitar[j]) == len(guitar[j+1]):
                sum1, sum2 = 0, 0
                for num in guitar[j]:
                    if num.isdigit():
                        sum1 += int(num)
                for num in guitar[j+1]:
                    if num.isdigit():
                        sum2 += int(num)
                if sum1 > sum2:
                    flag = True
                elif sum1==sum2:
                    if guitar[j] > guitar[j+1]:
                        flag = True
                else:
                    continue
            else:
                continue
            if flag:
                guitar[j], guitar[j + 1] = guitar[j + 1], guitar[j]
    return guitar
print('\n'.join(sortGui(guitar)))