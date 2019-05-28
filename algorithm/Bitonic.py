input_numbers = [1, 5, 2, 1, 4, 3, 4, 5, 2, 1]


def find_candi(arr):
    up = []
    down = []
    if len(arr) == 1:
        return False
    else:
        first = arr[0]
        for i in arr[1:]:
            if i > first:
                up.append(i)
            elif i < first:
                down.append(i)
        return up, down


print(find_candi(input_numbers))