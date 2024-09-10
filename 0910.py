"""
alist = list([] for _ in range(4))
alist[1] = [0, 3]
alist[2] = [1, 3]

print(alist)
"""
"""
# 인접 리스트를 하드코딩하고 n을 입력받을 때 name을 출력

name = 'DURSK'

alist = list([] for _ in range(5))
alist[0] = [1,3,4]
alist[1] = [2]
alist[3] = [2,4]
alist[4] = [1,3]

n =int(input())

for i in range(len(alist[n])):
    print(name[alist[n][i]])
"""


# Tree, Graph => Tree < Graph
# Tree는 Cycle 때문에 무한 loop 발생 가능
# => 방지 코드 필요

# Tree 조건

# 문제 7: 인접행렬 하드코딩 후, 특정 노드의 번호를 입력하면 자식 노드의 이름을 출력

"""
name = 'ABTQVX'

MAP =[[0,1,1,1,0,0],
      [0,0,0,0,1,1],
      [0,0,0,0,0,0],
      [0,0,0,0,0,0],
      [0,0,0,0,0,0],
      [0,0,0,0,0,0],]

n = int(input())

for i in range(len(MAP[n])):
    if MAP[n][i] == 0: continue
    print(name[i])
"""
# 문제 8: DFS 인접행렬, 탐색 순서 출력(노드 번호 출력)
"""
MAP =[[0,1,1,1,0,0],
      [0,0,0,0,1,1],
      [0,0,0,0,0,0],
      [0,0,0,0,0,0],
      [0,0,0,0,0,0],
      [0,0,0,0,0,0],]


def dfs(now):
    print(now, end= ' ')
    for i in range(6):
        if MAP[now][i] == 0: continue # 뒤로 돌아감을 보여주는 코드
        dfs(i)

dfs(0)
"""


# 인접리스트 + path 배열 -> 탐색순서 출력

def dfs(level, now):
    global path
    print(chr(ord('A') + now), end = ' ')
    for i in range(len(m[now])):
        next = m[now][i]
        # A 에서 B로 들어간다
        path[level + 1] = chr(ord('A') + next)
        temp1 = path # 디버깅용
        dfs(level + 1, next)
        temp2 = path
        path[level + 1] = 0

m = [[] for _ in range(6)]
