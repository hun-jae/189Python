from collections import Counter
n = int(input())
arr = list(map(int, input().split(" ")))

counter = Counter(arr)
check=[]
answer = []

while(len(arr)>0):
    tmp = arr[-1]
    if(len(check)==0):
        check.append(tmp)
        check.append(counter[tmp])
        answer.append(-1)
        arr.pop()
    else:
        if(counter[tmp]<check[-1]):
            answer.append(check[-2])
            check.append(tmp)
            check.append(counter[tmp])
            arr.pop()
        else :
            check.pop()
            check.pop()


for i in range(len(answer)):
    print(answer.pop(), end=' ')
