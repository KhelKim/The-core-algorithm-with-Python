import sys
from collections import deque
n, m, k = list(map(int, sys.stdin.readline().split()))
A = deque([])
for _ in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    A.append(tmp)
trees_alive = deque([])
for _ in range(m):
    tmp = list(map(int, sys.stdin.readline().split()))
    trees_alive.append((tmp[0]-1, tmp[1]-1, tmp[2]))
# trees_alive = sorted(trees_alive, key=lambda trees_alive: trees_alive[2])
board = [[5] * n for _ in range(n)]
adjacent = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
baby_trees = deque([])
dead_board = [[0] * n for _ in range(n)]


def spring():
    global trees_alive
    global able_to_reproduction
    trees_alive_output = deque([])
    able_to_reproduction = deque([])
    while baby_trees:
        x, y, age = baby_trees.popleft()
        if board[x][y] < age:
            continue
        board[x][y] -= age
        age += 1
        trees_alive_output.append((x, y, age))
    while trees_alive:
        x, y, age = trees_alive.popleft()
        if board[x][y] < age:
            dead_board[x][y] += age // 2
            continue
        board[x][y] -= age
        age += 1
        if age % 5 == 0:
            able_to_reproduction.append((x, y, age))
        trees_alive_output.append((x, y, age))
    trees_alive = trees_alive_output
    return


def fall():
    global baby_trees
    baby_trees = deque([])
    while able_to_reproduction:
        x, y, age = able_to_reproduction.popleft()
        for dx, dy in adjacent:
            nx, ny = x+dx, y+dy
            if nx < 0:
                continue
            if n <= nx:
                continue
            if ny < 0:
                continue
            if n <= ny:
                continue
            baby_trees.append((nx, ny, 1))
    return


def winter():
    for i in range(n):
        for j in range(n):
            board[i][j] += A[i][j] + dead_board[i][j]
            dead_board[i][j] = 0
    return


for _ in range(k):
    spring()
    if trees_alive == deque([]):
        break
    fall()
    winter()
    # print(board, trees_alive, baby_trees, able_to_reproduction, 'check')

print(len(trees_alive) + len(baby_trees))
