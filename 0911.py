"""
# 문제 11 인접리스트, 그래프의 dfs(used배열 지우지 않기, 모든 노드 1회)

def dfs(now):

    print(now, end=' ')
    for i in range(len(arr[now])):
        next = arr[now][i]
        if visited[next]: continue
        visited[next] = 1

        # 한 번도 안 간 곳이면 재귀호출
        dfs(next)


arr = [[] for _ in range(4)]

arr[0] = [1, 3]
arr[1] = [2]
arr[2] = [0, 3]
arr[3] = [2]

print(arr)

visited = [0] * 4
visited[0] = 1
dfs(0)

"""
"""
# 문제 12 인접행렬, 그래프의 dfs(used배열 지우지 않기, 모든 노드 1회)

m = [[0]*4 for _ in range(4)]


m[0][1] = 1
m[0][3] = 1
m[1][2] = 1
m[2][0] = 1
m[2][3] = 1
m[3][2] = 1

def dfs2(now):
    print(now, end=" ")

    for i in range(len(m[now])):
        next = m[now][i]
        if next == 0: continue
        if visited[i]: continue
        visited[i] = 1
        dfs2(i)

visited = [0] * 4
visited[0] = 1
dfs2(0)

"""

"""
# 0번 노드에서 2번 노드로 가는 경로 개수
m = [[0] * 3 for _ in range(3)]

m[0][1] = 1
m[1][2] = 1
m[2][0] = 1
m[0][2] = 1

def dfs(now):
    global cnt

    if now == 2:
        cnt += 1
        return

    for i in range(len(m[now])):
        next = m[now][i]
        if next == 0: continue
        if visited[i]: continue
        visited[i] = 1
        dfs(i)
        visited[i] = 0


visited = [0] * 3
visited[0] = 1
cnt = 0
dfs(0)
print(cnt)
"""


"""
## 문제 14: 모든 경로 탐색, 인접행렬, 매개변수 추가

## 가중치값

matrix = [[0] * 4 for _ in range(4)]

matrix[0][1] = 7
matrix[0][2] = 20
matrix[0][3] = 8
matrix[1][2] = 5
matrix[2][0] = 15
matrix[3][2] = 6

used = [0] * 4

def dfs(now, sum_v):

    # 2번 노드에 도착했을 때, sum_v 출력
    if now == 2:
        print(sum_v, end=" ")
    
    for i in range(4):
        if matrix[now][i] == 0: continue
        if used[i]: continue
        used[i] = 1
        dfs(i, sum_v + matrix[now][i])
        used[i] = 0


used[0] = 1
dfs(0, 0)

"""



"""
# 15-1 모든 노드를 1회 탐색 (4 출발)
# 15-2 모든 경로를 1회 탐색 (4 출발)

# 15-3 a, b 입력 a->b까지 가는 경로의 개수
# 15-4 a, b 입력 a->b까지 가는 가장 비싼 비용과 싼 비용


MAP = [[0,2,6,3,0,0],
       [2,0,7,4,0,0],
       [6,7,0,0,0,0],
       [3,4,2,0,0,0],
       [0,0,1,0,0,7],
       [0,0,0,0,0,0],]


used = [0] * 6

def dfs1(now):

    print(now, end=" ")
    for i in range(6):
        if MAP[now][i] == 0: continue
        if used[i]: continue
        used[i] = 1
        dfs1(i)

used[4] = 1
print("15-1")
dfs1(4)

used2 = [0] * 6

def dfs2(now):

    print(now, end=' ')
    for i in range(6):
        if MAP[now][i] == 0: continue
        if used2[i]: continue
        used2[i] = 1
        dfs2(i)
        used2[i] = 0


used2[4] = 1
print()
print("15-2")
dfs2(4)


used3 = [0] * 6
a, b = map(int, input().split())

def dfs3(now, b):
    global cnt

    if now == b:
        cnt += 1
        return

    for i in range(6):
        if MAP[now][i] == 0: continue
        if used3[i]: continue
        used3[i] = 1
        dfs3(i, b)
        used3[i] = 0

cnt = 0
used3[a] = 1
print()
print('15-3')
dfs3(a, b)
print(cnt)


used4 = [0] * 6

def dfs4(now, sum_v):
    global min_v, max_v

    if now == b:
        max_v = max(max_v, sum_v)
        min_v = min(min_v, sum_v)

    for i in range(6):
        if MAP[now][i] == 0: continue
        if used4[i]: continue
        used4[i] = 1
        dfs4(i, sum_v+MAP[now][i])
        used4[i] = 0

min_v = float('inf')
max_v = float('-inf')

used4[a] = 1
print()
print("15-4")
dfs4(a, 0)
print(max_v, min_v)
"""


from collections import deque
"""
q = deque()

q.append(5)
q.append(4)
q.append(3)

for i in range(5):
    num = q.popleft()
    q.append((num * 55 + 17) % 11)

while q:
    print(q.popleft())

"""


"""
alist = [[] for _ in range(7)]

alist[5] = [3, 1]
alist[3] = [2]
alist[1] = [4]
alist[4] = [0, 6]

q = deque()

q.append(5)

while q:
    now = q.popleft()
    print(now, end = " ")
    for i in range(len(alist[now])):
        next = alist[now][i]
        q.append(next)
"""
"""
name = 'ACBQTPR'

alist = [[0]* 7 for _ in range(7)]

alist[0][1] = 1
alist[0][2] = 1
alist[0][3] = 1
alist[2][4] = 1
alist[3][5] = 1
alist[3][6] = 1


q = deque()

q.append(0)

while q:
    now = q.popleft()
    print(name[now], end=" ")
    for i in range(len(alist[now])):
        if alist[now][i] == 0: continue
        q.append(i)
"""


"""
# DFS탐색

A - B - C - D - E - F - G

D - C - E - F - B - G

# BFS 탐색

A - B - D - C - G - E - F

D - C - E - F - B - G

"""

"""

# 그래프 BFS 탐색
# 그래프는 cycle이 있어서 무한 loop

alist = [[] for _ in range(5)]

alist[0] = [1, 2]
alist[1] = [0, 2]
alist[2] = [0, 1, 3]
alist[3] = [2, 4]
alist[4] = [3]

used = [0] * 5

def bfs(now):

    q = deque()

    q.append(now)
    used[now] =1

    while q:

        now = q.popleft()
        print(chr(now+ord('A')), end= ' ')
        for i in range(len(alist[now])):
            next = alist[now][i]
            if used[next]: continue
            q.append(next)
            used[next] = 1
            # used[next] = 0 => BFS에서는 할 필요 업음


bfs(3)
"""

"""
# A -> D까지 가는 최소 횟수

alist = [[] for _ in range(5)]

alist[0] = [1, 4]
alist[1] = [3, 4]
alist[2] = [0]
alist[3] = [0, 2]
alist[4] = []

def bfs(start, end):
    min_v = float('inf')
    q = deque()
    used = [0] * 5
    q.append((start,0))
    used[start] = 1

    while q:
        now, level = q.popleft()
        if now == end:
            return min(min_v, level)

        for i in range(len(alist[now])):
            next = alist[now][i]
            if used[next]: continue
            used[next] = 1
            q.append((next,level + 1))

    return -1


result = bfs(0, 3)
print(result)


"""



### Union-Find 구현

# 1. 7의 보스가 0이 아니면? 재귀
# 2. 6의 보스가 0이 아니면? 재귀
# 3. 5의 보스가 0이면? return 5


def Find(x):
    if boss[x] == 0:
        return x

    result = Find(boss[x])
    return result

def Union(t1, t2):
    a = Find(t1)
    b = Find(t2)
    if a == b: return
    boss[b] = a


boss = [0,0,0,0,0,0,5,6]

Union(6, 7)
Union(5, 6)
Union(1, 2)

if Find(2) == Find(6):
    print('같은 그룹')
else:
    print('다른 그룹')