import sys
from collections import deque

n, m = list(map(int, sys.stdin.readline().split()))
board = []
for _ in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    board.append(tmp)
#print(n, m)
#print(board)
#print('###############################top##################################')
house_locations = []
chicken_locations = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 0: continue
        if board[i][j] == 1: house_locations.append((i, j))
        if board[i][j] == 2: chicken_locations.append((i, j))

#print(house_locations, chicken_locations)
#print('###############middle#################')
def dfs(arr, m):
    visit = deque([])
    def generator(i=0):
        if len(visit) == m:
            yield visit
            return
        else:
            for j in range(i, len(arr)):
                visit.append(arr[j])
                yield from generator(i=j+1)
                visit.pop()
    yield from generator()

candi = []
for combination in dfs(chicken_locations, m):
    distance = 0
    for x, y in house_locations:
        tmp = []
        for i, j in combination:
            distance_tmp = abs(x-i) + abs(y-j)
            if distance_tmp==1:
                tmp.append(distance_tmp)
                break
            tmp.append(distance_tmp)
        distance += min(tmp)
    candi.append(distance)
#print(candi)
print(min(candi))