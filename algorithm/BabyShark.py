############# bfs
import sys

n = int(sys.stdin.readline())
board = []
for _ in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    board.append(tmp)
moves = ((1, 0),(-1, 0),(0, 1),(0, -1))
shark_body = 2
shark_eat = 0
shark_dis = 0
def init():
    global shark_location
    global queue
    global check
    queue = []
    check = [[False] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j] == 9:
                shark_location = (i, j)
                board[i][j] = 0
                check[i][j] = True
                queue.append((i, j, 0))
                break
init()
## print(board,'\n', check, '\n',queue, 'top') ###########
while queue:
    #### bfs
    x, y, d = queue.pop(0)
    ##### q.append
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if nx < 0: continue
        if n <= nx: continue
        if ny < 0: continue
        if n <= ny: continue
        if board[nx][ny] > shark_body: continue
        if check[nx][ny] == True: continue
        queue.append((nx, ny, d + 1))
        check[nx][ny] = True
    if queue == []:
        pass
    elif d == queue[0][2]:
        continue
    ## print(queue, '\n', check, '\n', board, 'middle')
    #### eat!!!
    tmp_que = sorted(queue, key=lambda x: (x[0], x[1]))
    for now_x, now_y, now_d in tmp_que:
        if 0 < board[now_x][now_y] < shark_body:
            shark_eat += 1
            shark_dis += now_d
            board[now_x][now_y] = 9
            if shark_eat == shark_body:
                shark_body += 1
                shark_eat = 0
            init()
            break
print(shark_dis)