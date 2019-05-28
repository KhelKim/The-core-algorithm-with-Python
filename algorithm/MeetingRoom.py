locations = [10, 4, 1, 2, 5, 7, 9]


def get_count_list(locations):
    max_loc = max(locations)
    min_loc = min(locations)
    count_list = []
    for i in range(min_loc, max_loc + 1):
        count = 0
        for loc in locations:
            count += abs(loc - i)
        count_list.append(count)
    return count_list


print(get_count_list(locations))
print(min(get_count_list(locations)))
