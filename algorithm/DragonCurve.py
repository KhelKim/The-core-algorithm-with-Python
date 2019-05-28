n = int(input())
information = []
for i in range(n):
    tmp = list(map(int, input().split()))
    information.append(tmp)

#n = 3
#information = [
#    [3, 3, 0 ,1],
#    [4, 2, 1, 3],
#    [4, 2, 2, 1]
#]

move = ((1, 0), (0, -1), (-1, 0), (0, 1))
board = []
def left_0(x, y, generation):
    board.append((x,y))
    if generation == 0:
        board.append((x+1,y))
    if generation == 1:
        board.append((x + 1, y))
        board.append((x + 1, y - 1))
    if generation == 2:
        board.append((x + 1, y))
        board.append((x + 1, y - 1))

def mat_mul(mat, vec):
    return [mat[0][0] * vec[0] + mat[0][1] * vec[1], mat[1][0] * vec[0] + mat[1][1] * vec[1]]
def mat_add(vec1, vec2):
    return [vec1[0]+ vec2[0], vec1[1] + vec2[1]]

def rot90(arr):
    rotation = []
    tmp = [[0, -1],[1, 0]]
    for data in arr:
        x, y = data[0], data[1]
        rotation.append(mat_mul(tmp, [x, y]))
    dx, dy = arr[-1][0] - rotation[-1][0], arr[-1][1] - rotation[-1][1]

    final_rot = []
    for vec in rotation[:-1]:
        final_rot = [mat_add(vec, [dx, dy])] + final_rot
    return final_rot

board = []
for i in information:
    vec = []
    x, y, direction, generation = i
    vec.append([x,y])
    if direction == 0: vec.append([x + 1, y])
    elif direction == 1: vec.append([x, y - 1])
    elif direction == 2: vec.append([x - 1, y])
    elif direction == 3: vec.append([x, y + 1])

    for j in range(generation):
        vec = vec + rot90(vec)
    board = board + vec

max_board = 0
for i in board:
    max_tmp = max(i)
    if max_tmp > max_board: max_board = max_tmp

count = 0
for i in range(max_board):
    for j in range(max_board):
        if [i, j] in board and [i+1, j] in board and [i, j+1] in board and [i+1, j+1] in board:
            count += 1
print(count)
