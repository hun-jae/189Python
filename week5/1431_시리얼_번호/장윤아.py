from functools import cmp_to_key
n = int(input())
serialNumbers = [input() for _ in range(n)]

def comp(x,y):
    if len(x)<len(y): #길이가 짧은 것이 앞으로 온다
        return -1
    elif len(x)==len(y): #길이가 같으면
        sumOfNumsInX = sum([int(i) for i in x if i.isdecimal()])
        sumOfNumsInY = sum([int(i) for i in y if i.isdecimal()])
        if sumOfNumsInX < sumOfNumsInY: #숫자의 합이 더 작은 것이 앞으로 온다
            return -1
        elif sumOfNumsInX > sumOfNumsInY: #숫자의 합이 더 큰 것이 뒤로 간다
            return 1
        else: #합이 같다
            for i in range(len(x)):
                if x[i] < y[i]: #사전순으로 더 빠른 것이 앞으로 온다
                    return -1
                elif x[i] > y[i]:
                    return 1
    else: #길이가 길면 뒤로 간다
        return 1

serialNumbers.sort(key = cmp_to_key(comp))
for serial in serialNumbers:
    print(serial)