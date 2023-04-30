n = int(input())

board = [list(map(int,input().split())) for _ in range(n)]

def divide(y,x,nn):
    if nn == 2 :
        temp = []
        for py in range(y, y+nn):
            for px in range(x, x+nn):
                temp.append(board[py][px])

    else :
        temp = [divide(y,x,nn//2),divide(y+nn//2,x,nn//2),divide(y,x+nn//2,nn//2),divide(y+nn//2,x+nn//2,nn//2)]
    temp.sort(reverse=True)
    return temp[1]

print(divide(0,0,n))
