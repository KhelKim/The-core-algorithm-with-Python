def permutation(arr, i = 0):
    if len(arr) - 1 == i:
        print(arr)
        return
    else:
        for j in range(i, len(arr)):
            arr[i], arr[j] = arr[j], arr[i]
            permutation(arr, i+1)
            arr[i], arr[j] = arr[j], arr[i]
#permutation([1,2,3,4])

def combination(arr, m):
    from collections import deque
    visit = deque([])
    def generator(arr, m, i=0):
        if len(visit) == m:
            print(visit)
            return
        else:
            for j in range(i, len(arr)):
                visit.append(arr[j])
                generator(arr, m, i=j+1)
                visit.pop()
    generator(arr, m)
#combination([1,2,3,4,5], 3)

def pi(arr, m):
    from collections import deque
    visit = deque([])
    def generator(arr, m):
        if len(visit) == m:
            print(visit)
            return
        else:
            for j in range(len(arr)):
                visit.append(arr[j])
                generator(arr, m)
                visit.pop()
    generator(arr, m)
#pi([1,2], 4)

