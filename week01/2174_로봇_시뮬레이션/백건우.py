mv_y = [-1,0,1,0]
mv_x = [0,1,0,-1]

A, B = map(int, input().split()) #board 가로 세로 크기
N, M = map(int, input().split()) #로봇 개수, 명령의 수
board = [[0 for _ in range(A)] for _ in range(B)]
robot = [[]]
actions = []
for i in range(N):
    x, y ,dir = input().split()
    if dir == 'N' :
        dir = 0
    elif dir == 'E' :
        dir = 1
    elif dir == 'S' :
        dir = 2
    elif dir == 'W' :
        dir = 3
    robot.append([B-int(y), int(x)-1, dir])
    board[B-int(y)][int(x)-1] = i+1

for _ in range(M):
    robotNum, order, itr = input().split()
    robotNum = int(robotNum)
    itr = int(itr)
    y,x, dir = robot[robotNum]
    for _ in range(itr):
        if order == 'L':
            dir = (dir - 1) % 4
            robot[robotNum][2] = dir
        elif order == 'R':
            dir = (dir + 1) % 4
            robot[robotNum][2] = dir
        elif order == 'F' :
            ny = y + mv_y[dir]
            nx = x + mv_x[dir]
            if ny < 0 or ny >= B or nx < 0 or nx >= A :
                print('Robot {} crashes into the wall'.format(robotNum))
                exit(0)
            if board[ny][nx] != 0 :
                print('Robot {} crashes into robot {}'.format(robotNum, board[ny][nx]))
                exit(0)
            board[ny][nx] = robotNum
            board[y][x] = 0
            y = ny
            x = nx
            robot[robotNum] = [y, x, dir]
print("OK")
