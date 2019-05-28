import sys
n, m, h = list(map(int, sys.stdin.readline().split()))
bars = []
for i in range(m):
    tmp = list(map(int, sys.stdin.readline().split()))
    bars.append(tmp)
board = [[0] * n for _ in range(h)]
for bar in bars:
    x, y = bar[0], bar[1]
    board[x-1][y-1] = 1
    board[x-1][y] = 2
## 내려가기
def down():
    #print(board, 'down')
    for i in range(n):
        location = i
        for j in range(h):
            if board[j][location] == 1:
                location += 1
            elif board[j][location] == 2:
                location -= 1
        if location != i:
            return False
    return True

success = False
## 출력
if down() == True:
    success = True
    print(0)
else:
    ## dfs
    flat_board = []
    for i in board:
        flat_board += i
    # print(flat_board, 'flat_board')
    hope_ = []
    from collections import deque
    visit = deque([])
    def hope(arr, m, i=0):
        global board, success, hope
        if len(visit) == m:
            return
        elif arr == []:
            return
        else:
            for t in range(i, len(arr)-1):
                if (t+1) % n == 0: continue
                height = t // n
                tmp = t % n
                if board[height][tmp] == 0 and board[height][tmp+1] == 0:
                    visit.append((height, tmp))
                    board[height][tmp] = 1
                    board[height][tmp+1] = 2
                    #print(visit, 'visit')
                    #print(board, 'board')
                    #print(down())
                    if down() == True:
                        success = True
                        hope_.append(len(visit))
                        #print(board, 'final_visit')
                        #print(len(visit))
                    hope(arr, m, i=t+1)
                    board[height][tmp] = 0
                    board[height][tmp+1] = 0
                    visit.pop()
    hope(flat_board, 3)
    if success == True:
        #print(hope_)
        print(min(hope_))
if success == False:
    print(-1)