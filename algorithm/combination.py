visit = []
def combination(arr, m):
    if len(visit) == m:
        yield visit
    else:
        for j in range(len(arr)):
            visit.append(arr[j])
            yield from combination(arr[j+1:], m)
            visit.pop()

for i in combination([1,2,3,4,5], 3):
    print(i)

def permutation(arr, i=0):
    if len(arr) - 1 == i:
        yield arr
        return
    else:
        for j in range(i, len(arr)):
            arr[i],arr[j] = arr[j], arr[i]
            yield from permutation(arr, i+1)
            arr[i],arr[j] = arr[j], arr[i]
permutation([1,2,3,4])