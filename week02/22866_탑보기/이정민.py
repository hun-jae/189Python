n = int(input())
height = list(map(int, input().split()))

def l_view(n, arr):
   while(len(arr)>0):
       a = arr.pop()
       if a > n:
           n = a
           stack.append(len(arr) + 1)

def r_view(i, n, arr):
    for a in range(len(arr)):
        if arr[a] > n:
            stack.append(i+a+2)
            n = arr[a]

for i in range(len(height)):
    stack = []
    colsest = 0
    distance = 999999

    if(i == 0):
        right_view=height[1:]

        r_view(i, height[0],right_view)

    elif(i == (len(height)-1)):
        left_view=height[:i]

        l_view(height[i], left_view)

    else:
        left_view = height[:i]
        right_view = height[i+1:]

        r_view(i, height[i], right_view)
        l_view(height[i], left_view)

    for s in stack:
        new = abs((i+1)-s)

        if distance == new :
            closest=min(s,closest)
        elif distance>new:
            closest=s
            distance=new
            
    if len(stack)!=0:
        print("%d %d"%(len(stack), closest))
    else:
        print(0)

