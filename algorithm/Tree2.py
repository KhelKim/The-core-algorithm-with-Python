import time
import pprint
start_time = time.time()
pp = pprint.PrettyPrinter(width=80)


def tree_finance():
    ntrees = 0

    for x in range(n):
        for y in range(n):
            if not tree_age[x][y]:
                continue
            dead_tree = 0
            count = 0
            tmp = len(tree_age[x][y])
            while count < tmp:
                if tree_age[x][y][count] <= field_food[x][y]:
                    field_food[x][y] -= tree_age[x][y][count]
                    tree_age[x][y][count] += 1
                else:
                    t = tree_age[x][y].pop()
                    dead_tree += int(t / 2)
                    count -= 1
                    tmp = len(tree_age[x][y])
                count += 1

            field_food[x][y] += dead_tree

    for x in range(n):
        for y in range(n):
            field_food[x][y] += fix_food[x][y]
            if not tree_age[x][y]:
                continue
            reproduce = ((x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y - 1), (x, y + 1), (x + 1, y - 1), (x + 1, y), (x + 1, y + 1))
            for tmptmp in range(len(tree_age[x][y])):
                if (tree_age[x][y][tmptmp] % 5) == 0:
                    for i, j in reproduce:
                        if i >= 0 & i < n:
                            if j >= 0 & j < n:
                                tree_age[i][j] = [1] + tree_age[i][j]
                        else:
                            pass

    for nx in range(n):
        for ny in range(n):
            ntrees += len(tree_age[nx][ny])

    print(tree_age)
    return ntrees


n, m, k = map(int, input().split(" "))

field_food = []
tree_age = []
fix_food = []

for _ in range(n):
    field_food.append([5 for _ in range(n)])
    tree_age.append([[] for _ in range(n)])
    fix_food.append(list(map(int, input().split(" "))))

for _ in range(m):
    c, r, age = map(int, input().split(" "))
    tree_age[c - 1][r - 1].append(age)

result = 0

for _ in range(k):
    result = tree_finance()

print(result)

print("--- %s seconds ---" % (time.time() - start_time))
