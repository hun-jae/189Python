n = int(input())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

def floyd():  # 플로이드 그냥 돌림
    for m in range(n):
        for s in range(n):
            for e in range(n):
                if board[s][m] != 0 and board[m][e] != 0:  # 경로 존재하면 1로 
                    board[s][e] = 1

floyd()
for line in board:
    for node in line :
        print(node, end=" ")
    print()
