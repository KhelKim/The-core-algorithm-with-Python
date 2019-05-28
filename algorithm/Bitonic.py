input_numbers = [1, 5, 2, 1, 4, 3, 4, 5, 2, 1]


def find_candi(current, arr):
    up = []
    down = []
    for i, j in enumerate(arr):
        if current < i:
            up.append((i, j))
        elif current > i:
            down.append((i, j))
    return up, down


direction = True
current = []
def get_bitonic(arr, main_array, direction):
    if len(arr) == 0:
        return
    else:
        up, down = find_candi()
