import sys
n, m = list(map(int, sys.stdin.readline().split()))
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
from copy import deepcopy
board_copy = deepcopy(board)

cctvs = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 0: pass
        elif board[i][j] == 1: cctvs.append((i, j, 0))
        elif board[i][j] == 2: cctvs.append((i, j, 1))
        elif board[i][j] == 3: cctvs.append((i, j, 2))
        elif board[i][j] == 4: cctvs.append((i, j, 3))
        elif board[i][j] == 5: cctvs.append((i, j, 4))

############# cctv1
def cctv1_up(cctv):
    global board
    x, y = cctv[0], cctv[1]
    for i in range(x-1, -1, -1):
        if board[i][y] == 6: break
        if board[i][y] in (1,2,3,4): continue
        board[i][y] = '#'
def cctv1_down(cctv):
    global board
    x, y = cctv[0], cctv[1]
    for i in range(x+1, n):
        if board[i][y] == 6: break
        if board[i][y] in (1,2,3,4): continue
        board[i][y] = '#'
def cctv1_left(cctv):
    global board
    x, y = cctv[0], cctv[1]
    for j in range(y-1, -1, -1):
        if board[x][j] == 6: break
        if board[x][j] in (1,2,3,4): continue
        board[x][j] = '#'
def cctv1_right(cctv):
    global board
    x, y = cctv[0], cctv[1]
    for j in range(y+1, m):
        if board[x][j] == 6: break
        if board[x][j] in (1,2,3,4): continue
        board[x][j] = '#'

cctv1_fnc = [cctv1_up, cctv1_down, cctv1_left, cctv1_right]
############### cctv2
def cctv2_row(cctv):
    global board
    cctv1_left(cctv)
    cctv1_right(cctv)
def cctv2_col(cctv):
    global board
    cctv1_up(cctv)
    cctv1_down(cctv)
cctv2_fnc = [cctv2_row, cctv2_col]
########## cctv3
def cctv3_up(cctv):
    global board
    cctv1_up(cctv)
    cctv1_left(cctv)
def cctv3_down(cctv):
    global board
    cctv1_down(cctv)
    cctv1_right(cctv)
def cctv3_left(cctv):
    global board
    cctv1_left(cctv)
    cctv1_down(cctv)
def cctv3_right(cctv):
    global board
    cctv1_right(cctv)
    cctv1_up(cctv)
cctv3_fnc = [cctv3_left, cctv3_right, cctv3_up, cctv3_down]
########## cctv 4
def cctv4_up(cctv):
    global board
    cctv1_right(cctv)
    cctv1_up(cctv)
    cctv1_left(cctv)
def cctv4_down(cctv):
    global board
    cctv1_left(cctv)
    cctv1_down(cctv)
    cctv1_right(cctv)
def cctv4_left(cctv):
    global board
    cctv1_up(cctv)
    cctv1_left(cctv)
    cctv1_down(cctv)
def cctv4_right(cctv):
    global board
    cctv1_down(cctv)
    cctv1_right(cctv)
    cctv1_up(cctv)
cctv4_fnc = [cctv4_up, cctv4_down, cctv4_left, cctv4_right]
############ cctv5
def cctv5_all(cctv):
    global board
    cctv1_left(cctv)
    cctv1_right(cctv)
    cctv1_up(cctv)
    cctv1_down(cctv)
cctv5_fnc = [cctv5_all]

cctv1_direction = [0,1,2,3]
cctv2_direction = [0, 1]
cctv3_direction = [0,1,2,3]
cctv4_direction = [0,1,2,3]
cctv5_direction = [0]

cctv_fncs = [cctv1_fnc,cctv2_fnc,cctv3_fnc,cctv4_fnc,cctv5_fnc]
directions = [cctv1_direction, cctv2_direction, cctv3_direction,
              cctv4_direction, cctv5_direction]
#print(cctvs, 'cctvs')

possible = []
experiment = 1
for _, _, version in cctvs:
    possible.append(len(directions[version]))
    experiment *= len(directions[version])
#print(possible,experiment, 'possible')

from collections import deque
visit = deque([])
def pi(arr, m, i=0):
    if len(visit) == m:
        yield visit
    else:
        for j in range(len(arr)):
            visit.append(arr[j])
            yield from pi(arr, m, i+1)
            visit.pop()

def count_0():
    a = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0: a+=1
    return a
if cctvs == []:
    print(count_0())
else:
    visit = deque([])
    count = []
    for case in pi([0,1,2,3], len(cctvs)):
        run = False
        for i in range(len(case)):
            if case[i] >= possible[i]: run = True
        if run: continue

        #print(case, 'case')
        for i in range(len(case)):
            x, y, version = cctvs[i][0], cctvs[i][1], cctvs[i][2]
            direc = case[i]
            cctv_fncs[version][direc](cctvs[i])
        cur = count_0()
        board = deepcopy(board_copy)
        if cur == 0:
            count.append(cur)
            break
        else:
            count.append(cur)
    #print(count)
    print(min(count))