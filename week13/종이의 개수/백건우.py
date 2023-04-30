n = int(input())
board = []
ans = [0,0,0]
for _ in range(n):
    board.append(list(map(int,input().split())))

def divide(y, x, N):
    color = board[y][x]
    for py in range(y, y+N):
        for px in range(x, x+N):
            if board[py][px] != color:
                divide(y,x,N//3)
                divide(y,x+N//3,N//3)
                divide(y,x+(N//3)*2,N//3)
                divide(y+N//3, x, N // 3)
                divide(y+N//3, x + N // 3, N // 3)
                divide(y+N//3, x + (N // 3) * 2, N // 3)
                divide(y+(N//3)*2, x, N // 3)
                divide(y+(N//3)*2, x + N // 3, N // 3)
                divide(y+(N//3)*2, x + (N // 3) * 2, N // 3)
                return

    if color == -1 :
        ans[0] += 1
    elif color == 0 :
        ans[1] += 1
    else :
        ans[2] += 1

divide(0,0,n)
for num in ans :
    print(num)
