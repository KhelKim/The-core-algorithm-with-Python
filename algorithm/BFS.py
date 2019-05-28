def init():
    global queue
    queue = ["start"]


visited = []
while queue:
    n = queue.pop(0) # 현위치
    if n not in visited: # 현위치와 연결된 노드 중 다음에 큐에 들어갈 조건
        print("do something")
    # 현재 큐에서 해야하는일
    # something
