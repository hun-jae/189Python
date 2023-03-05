n = int(input())

bigger = n//5

while(1):
    tmp = n - (bigger*5)
    if(tmp % 2 == 0):
        print(bigger+(tmp//2))
        break
    else:
        bigger = bigger - 1
        if bigger < 0:
            print(-1)
            break


