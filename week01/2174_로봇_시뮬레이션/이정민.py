a, b = map(int, input().split())
n, m = map(int, input().split())

map=[[0]*a]*b
order=[]
location=[]

for i in range(n):
    tmp_loc=input().split(' ')
    location.append(tmp_loc)

for j in range(m):
    tmp_order = input().split(' ')
    order.append(tmp_order)

watch=['N','W','S','E']

def R(loc):
    look=loc[2]
    now = watch.index(look)
    if now==0:
        loc[2]=watch[3]
    else :
        loc[2]=watch[now-1]

def L(loc):
    look = loc[2]
    now = watch.index(look)
    if now == 3:
        loc[2] = watch[0]
    else:
        loc[2] = watch[now +1]

def F(loc):
    x=int(loc[0])
    y=int(loc[1])
    look=loc[2]
    if look=='N':
        loc[1]=str(y+1)
    elif look=='W':
        loc[0]=str(x-1)
    elif look=='E':
        loc[0]=str(x+1)
    else:
        loc[1]=str(y-1)

for o in order:
    robot=int(o[0])-1
    want=o[1]
    times=int(o[2])
    for t in range(times):
        if want=='L':
            L(location[robot])
        elif want=='R':
            R(location[robot])
        else :
            F(location[robot])
            loc_x=location[robot][0]
            loc_y=location[robot][1]
            if int(loc_x)<1 or int(loc_y)<1 or int(loc_x)>a or int(loc_y)>b:
                print('Robot %d crashes into the wall'%(int(robot)+1))
                quit()
            for r in range(len(location)):
                if r==int(robot):
                    continue
                else:
                    tmp_x=location[r][0]
                    tmp_y=location[r][1]
                    if tmp_x==loc_x and tmp_y==loc_y:
                        print('Robot %d crashes into robot %d'%((int(robot)+1),r+1))
                        quit()



print('OK')