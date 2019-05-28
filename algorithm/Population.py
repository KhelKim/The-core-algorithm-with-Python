import sys
from collections import deque
n, l, r = list(map(int, sys.stdin.readline().split()))
board = []
for _ in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    board.append(tmp)
moves = (1, 0), (0, 1), (-1, 0), (0, -1)

def init(i=0, j=0):
    global queue
    queue = deque([])
    queue.append((i,j))
    check[i][j] = True
def bfs():
    global check
    check = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if check[i][j] != False: continue
            init(i, j)
            sum_ = board[i][j]
            locations = deque([(i, j)])
            while queue:
                x, y = queue.popleft()
                #### 조건
                for dx, dy in moves:
                    nx, ny = x + dx, y + dy
                    if nx < 0: continue
                    if n <= nx: continue
                    if ny < 0: continue
                    if n <= ny: continue
                    if check[nx][ny] != False: continue
                    if l <= abs(board[x][y] - board[nx][ny]) <= r:
                        queue.append((nx, ny))
                        locations.append((nx, ny))
                        sum_ += board[nx][ny]
                        check[nx][ny] = True
            mean = sum_ // len(locations)
            while locations:
                x, y = locations.popleft()
                check[x][y] = mean
    return check

count = 0

while True:
    tmp = bfs()
    if tmp == board:
        break
    count += 1
    board = tmp
print(count)