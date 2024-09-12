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

"""
def Find(x):
    if boss[x] == 0:
        return x

    result = Find(boss[x])
    boss[x] = result # 경로 압축
    return result
    # return Find(boss[x]) # 경로 압축 반영

def Union(t1, t2):
    a = Find(t1)
    b = Find(t2)
    if a == b: return
    boss[b] = a


boss = [0,0,0,0,0,0,5,6]

Union(6, 7)
Union(5, 6)
Union(1, 2)

if Find(1) == Find(2):
    print('같은 그룹')
else:
    print('다른 그룹')
"""


"""
### Union-Find 문제
# 같은 그룹이면 'O'
# 다른 그룹이면 'X'

def Find(x):
    if boss[x] == 0:
        return x

    result = Find(boss[x])
    boss[x] = result
    return result


def Union(t1, t2):
    A = Find(t1)
    B = Find(t2)
    if A == B: return # 이미 보스가 같으면 A
    boss[B] = A # 아니면 B를 바꿈


N = int(input())
boss = [0]*100
for i in range(N):
    a, b = map(int,input().split())
    Union(a, b)


Q = int(input())
for i in range(Q):
    c, d = map(int,input().split())
    if Find(c) == Find(d): print('O')
    else: print('X')


print(boss)
"""


# 문제 veintidos: cycle 판단 코드
# cycle이 있다 => 간선을 한 번씩만 이용했을 때 제자리로 돌아올 수 있음

## Cycle의 여부를 Union-Find로 찾을 수 있음(양방향만 가능)


"""
4
A B
B C
D E
C A

"""

# 전략 1. 문자를 아스키코드로 바꿈
# 전략 2. a와 b가 같은 그룹이면 "Cycle 발견!!" 출력

"""
Cycle 발견 시 발견이라고 출력
"""

"""
def Find(x):
    if boss[x] == 0: return x

    result = Find(boss[x])
    boss[x] = result
    return result

def Union(t1, t2):
    a = Find(t1)
    b = Find(t2)
    if a == b: return 
    else: boss[b] = a

N = int(input())
boss = [0] * 100

for _ in range(4):
    a, b = map(ord,input().split())
    if Find(a) == Find(b):
        print("cycle 발견!!!")
        break
    else:
        Union(a, b)

## 라우터에 활용하는 것이 MST
# -> 라우터는 경로를 돌아가더라도 트래픽이 적은 경로로 연결 하는 것이 효율 좋음
"""

# Kruskal Algorithm

"""
9
A B 3
A C 5
B C 2
B D 1
A D 15
C D 2
E D 3
E D 6
A E 18

"""


"""
# 1. 비용을 기준으로 오름차순

# 2. 같은 그룹인지 판단하고 다른 그룹이면 그룹맺기

# 다 같이 친구가 되려면 어떻게 해야할까?

def Find(x):
    if boss[x] == 0: return x

    result = Find(boss[x])
    boss[x] = result
    return result


def Union(t1, t2):
    a = Find(t1)
    b = Find(t2)
    if a == b: return
    else: boss[b] = a

N, M = map(int, input().split())
arr = []

for _ in range(N):
    a, b, c = input().split()
    arr.append((int(c), ord(a), ord(b)))

boss = [0] * 100
arr.sort()

sum_v = 0
cnt = 0

for i in range(N):
    a, b, c = arr[i][1],arr[i][2], arr[i][0]
    if Find(a) == Find(b): continue
    if cnt == M-1: break
    else:
        Union(a, b)
        cnt += 1
        sum_v += c

print(sum_v)
"""

"""

alist= [[0]*6 for _ in range(6)]

alist[0][1] = 15
alist[1][2] = 5
alist[2][3] = 6
alist[2][4] = 2
alist[3][5] = 7
alist[4][5] = 1
alist[0][3] = 30

print(alist)

used = [0] * 6
min_v = float('inf')

def dfs(now, end, sum_v):
    global min_v
    if now == end:
        min_v = min(min_v,sum_v)
        return

    for i in range(len(alist[now])):
        if alist[now][i] == 0: continue
        if used[i]: continue
        used[i] = 1
        dfs(i,end, sum_v + alist[now][i])
        used[i] = 0

dfs(0, 5, 0)

print(min_v)
"""


"""import heapq

MAP = [[0] * 6 for _ in range(6)]

MAP[0][1] = 15
MAP[0][2] = 30
MAP[1][2] = 5
MAP[2][3] = 6
MAP[2][4] = 2
MAP[3][5] = 7
MAP[4][5] = 1


def dijkstra(start):
    n = len(MAP)  # 노드 수 6개
    result = [float('inf')] * n
    result[start] = 0 # 시작 노드 초기화

    #우선순위 큐 초기화
    q = [(0, start)]  # 비용, 노드

    while q:
        price, now = heapq.heappop(q) # 현재 최소 비용인 노드 선택
        if result[now] < price: continue # 이미 처리된 노드면 패스

        for i in range(n):
            if MAP[now][i] == 0: continue
            next_price = MAP[now][i] # 다음 노드까지의 비용
            price_sum = price + next_price
            if result[i] > price_sum: # 최단비용 갱신
                result[i] = price_sum
                heapq.heappush(q, (price_sum,i)) # 새로운 경로를 큐에 추가

    return  result



result = dijkstra(0)

print(result)
print(result[5])
"""


import heapq

arr = [[0]*6 for _ in range(6)]

arr[0][1] = 5
arr[0][2] = 10
arr[1][0] = 5
arr[1][5] = 9
arr[2][5] = 1
arr[0][3] = 7
arr[3][4] = 1
arr[4][5] = 6


def dijkstra(start):
    n = len(arr)
    result = [float('inf')] * n
    result[start] = 0

    # 우선순위 큐 초기화
    q = [(0, start)] # 비용, 노드

    while q:
        price, now = heapq.heappop(q)
        if result[now] < price: continue # 이미 처리된 노드면 패스

        for i in range(n):
            if arr[now][i] == 0: continue
            next_price = arr[now][i]
            price_sum = price + next_price
            if result[i] > price_sum:
                result[i] = price_sum
                heapq.heappush(q,(price_sum,i))
    return result

result = dijkstra(0)
print(result)