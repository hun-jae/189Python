'''
이거 k가 1 또는 2임
경우의 수 다 구해도 되지만 그러지 않기로..
분할정복으로 안품ㅎㅎ
'''

k = int(input())
x, y = map(int,input().split())
x -= 1
y = 2**k - y

num = 1
board = [[1 for _ in range(2**k)] for _ in range(2**k)]
def divide(y,x,n):
    global num
    if n == 2 :
        for py in range(y, y+n):
            for px in range(x, x+n):
                board[py][px] = num
        num += 1
        return
    divide(y,x,n//2)
    divide(y,x+n//2,n//2)
    divide(y+n//2,x,n//2)
    divide(y+n//2,x+n//2,n//2)
    divide(y+1,x+1,n//2)
divide(0,0,2**k)
if k == 1 or (1 <= y <= 2 and 1 <= x <= 2):
    board[y][x] = -1
else :
    if 0 <= y <= 1 and 0 <= x <= 1 :
        board[1][1] = board[0][0]
        board[y][x] = -1
    elif 0 <= y <= 1 and 2 <= x <= 3 :
        board[1][2] = board[0][3]
        board[y][x] = -1
    elif 2 <= y <= 3 and 0 <= x <= 1 :
        board[2][1] = board[3][0]
        board[y][x] = -1
    elif 2 <= y <= 3 and 2 <= x <= 3 :
        board[2][2] = board[3][3]
        board[y][x] = -1
for line in board:
    print(' '.join(map(str,line)))
