b,a = map(int, input().split())
n, m = map(int, input().split())
robots = []
conv = {'N' : 0, 'W' : 1, 'S' : 2, 'E' : 3} #상좌하우
# L이면 +1 R이면 -1
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
for i in range(n):
    inputY, inputX, d = input().split()
    y = int(inputY) - 1
    x = a - int(inputX)
    d = conv[d]
    robots.append([x,y,d])
crushRobot = -1
i = 0

for i in range(m): #각 명령별로
    index, op, cnt = input().split()
    index = int(index) - 1
    cnt = int(cnt)
    x, y, d = robots[index]
    if op=='F':
        ny = y + dy[d] * cnt
        nx = x + dx[d] * cnt
        minT2 = 200
        minIdx = -1
        for j in range(len(robots)):
            x2, y2, d2 = robots[j]
            if d in [0,2]: #위아래로 움직일 때
                t, t2, nt, f, f2, ab = x, x2, nx, y, y2, a
            else:
                t, t2, nt, f, f2, ab = y, y2, ny, x, x2, b
            plusMinus = 1 if t < nt else -1
            if f == f2: #움직이는 축에 로봇이 있으면
                if t2 in range(t + plusMinus, nt + plusMinus, plusMinus):
                    #양수로 움직이고 있으면 가장 작을 때 만난 로봇
                    #반대로 움직이면 가장 클 때 만난 로봇
                    if minT2 > t2 * plusMinus:
                        minT2 = t2 * plusMinus
                        minIdx = j+1
        if minIdx != -1:
            print("Robot",(index+1),"crashes into robot",minIdx)
            exit(0)
        if nx >= a or nx < 0 or ny >= b or ny < 0:
            print("Robot",(index+1),"crashes into the wall")
            exit(0)
        robots[index] = [nx, ny, d]
    elif op == "L":
        d += cnt
        d %= 4
        robots[index] = [x,y,d]
    else:
        d -= cnt
        d %= 4
        robots[index] = [x, y, d]
print("OK")
