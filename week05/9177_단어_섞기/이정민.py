#시간 초과...

from collections import deque

N = int(input())

for i in range(N):
    arr = list(map(str, input().split(' ')))
    q1 = deque(arr[0])
    q2 = deque(arr[1])
    q3 = deque(arr[2])

    while (len(q3)>0):
        if len(q1) == 0 : str1 = '0'
        elif len(q2) == 0 : str2 = '0'
        else:
            str1 = q1[0]
            str2 = q2[0]
        str3 = q3[0]

        if str3 == str1 or str3 == str2:
            if(str1 == str2):
                check = q3[1]
                if len(q1) > 1 and q1[1] == check:
                    q1.popleft()
                    q3.popleft()
                elif len(q2) > 1 and q2[1] == check:
                    q2.popleft()
                    q3.popleft()
            else:
                if str1 == str3:
                    q1.popleft()
                    q3.popleft()
                elif str2 == str3:
                    q2.popleft()
                    q3.popleft()
        elif str3 != str1 and str3 != str2:
            break;

    if len(q3) != 0:
        print("Data set %d: no"%(i+1))
    else:
        print("Data set %d: yes"%(i+1))