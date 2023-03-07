N = int(input())

def bt(cnt, temp):
    if cnt == N:
        print(temp)         # print and exit
        exit()

    for i in range(1, 4):
        temp += str(i)
        for j in range(1, (cnt+1)//2+1):
            if temp[-j:] == temp[-2*j:-j]: break
        else:
            bt(cnt+1, temp) # can proceed
        temp = temp[:-1]

bt(0, '')
