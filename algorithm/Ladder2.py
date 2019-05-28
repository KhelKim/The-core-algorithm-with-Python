import sys
from collections import deque

n, m, h = list(map(int, sys.stdin.readline().split()))
bars = deque([])
for _ in range(m):
    tmp = list(map(int, sys.stdin.readline().split()))
    bars.append((tmp[0]-1, tmp[1]-1))

board = [[0] * n for _ in range(h)]
while bars:
    x, y = bars.pop()
    board[x][y] = 1
    board[x][y+1] = 2

#print(n, m, h)
#print(board)
#print('###########################top####################')

## 내려가기
def down(board):
    for j in range(n):
        location = j
        for i in range(h):
            if board[i][location] == 0:
                continue
            if board[i][location] == 1:
                location += 1
                continue
            if board[i][location] == 2:
                location -= 1
                continue
        if j != location:
            return False
    return True

def dfs(board):
    global count
    visit = deque([])
    count = 0
    def generator(limit=3, i=0):
        global count
        if len(visit) == limit:
            return
        else:
            for j in range(i, (n-1)*h):
                x = j // (n-1)
                y = j % (n-1)
                ## 조건
                if board[x][y] != 0: continue
                if board[x][y+1] != 0: continue
                visit.append((x,y))
                board[x][y] = 1
                board[x][y+1] = 2
                #print(board)
                tmp = down(board)
                if tmp:
                    if len(visit) <= limit:
                        limit = len(visit)
                        count = limit
                generator(limit, i=j+1)
                visit.pop()
                board[x][y] = 0
                board[x][y+1] = 0
    generator()
if down(board):
    print(0)
else:
    dfs(board)
    if count:
        print(count)
    else:
        print(-1)