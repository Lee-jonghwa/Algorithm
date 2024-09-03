"""
N, Q = map(int, input().split())

logs = [list(map(int, input().split())) + [i] for i in range(N)]
logs.sort(key=lambda x: x[0])  # 통나무를 x좌표 기준으로 정렬

# 각 통나무의 부모 노드 (그룹) 정보를 저장하는 리스트
parent = [i for i in range(N)]

# 첫 번째 통나무부터 시작하여 점프 가능 여부를 판단하고 부모 노드 업데이트
current_group = 0
end_x = logs[0][1]
for i in range(1, N):
    start_x, end_x_new, _ = logs[i]

    # 이전 통나무의 끝점과 현재 통나무의 시작점이 겹치면 같은 그룹으로 설정
    if end_x >= start_x:
        parent[i] = current_group
        end_x = max(end_x, end_x_new)
    else:
        # 새로운 그룹 시작
        current_group = i
        parent[i] = current_group
        end_x = end_x_new

# 질의에 대한 답변
for _ in range(Q):
    a, b = map(int, input().split())
    # 두 통나무의 부모 노드가 같으면 점프 가능
    if parent[a - 1] == parent[b - 1]:
        print(1)
    else:
        print(0)
"""

N, Q = map(int, input().split())

arr = [list(map(int, input().split())) + [i] for i in range(N)]
arr.sort(key=lambda x: x[0]) # 통나무 정렬
connected = [i for i in range(N)] # 연결 여부

idx = arr[0][3] # 처음에 위치한 통나무의 idx
end = arr[0][1] # 처음에 위치한 통나무의 제일 끝 부분

for i in range(1, N):
    s = arr[i][0]
    e = arr[i][1]
    # 이전 통나무의 제일 끝부분 x좌표보다 현재 통나무의 제일 첫부분 x좌표가 작으면 점프로 이동 가능
    # 이동할 수 있다 -> connected 값이 같다
    # 현재 본 통나무의 제일 끝부분과 이전 통나무 제일 끝부분 중 더 긴 것으로 갱신
    if end >= s:
        end = max(end, e)
        connected[arr[i][3]] = idx
    # 아니라면 이동 불가능, 서로 다른 부모
    else:
        idx = arr[i][3]
        end = e

for _ in range(Q):
    x, y = map(int, input().split())
    if connected[x-1] == connected[y-1]: # 부모가 같음 == 점프 가능
        print(1)
    else:
        print(0)


"""
N, Q = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: x[0]) # 통나무 정렬
connected = [i for i in range(N)] # 연결 여부


# 그룹 추가
# [list(map(int, input().split())) + [i] for i in range(N)]
for i in range(N):
    arr[i].append(i)

idx = arr[0][3] # 처음에 위치한 통나무의 idx
end = arr[0][1] # 처음에 위치한 통나무의 제일 끝 부분

for i in range(1, N):
    s = arr[i][0]
    e = arr[i][1]
    # 이전 통나무의 제일 끝부분 x좌표보다 현재 통나무의 제일 첫부분 x좌표가 작으면 점프로 이동 가능
    # 이동할 수 있다 -> connected 값이 같다
    # 현재 본 통나무의 제일 끝부분과 이전 통나무 제일 끝부분 중 더 긴 것으로 갱신
    if end >= s:
        end = max(end, e)
        connected[arr[i][3]] = idx
    # 아니라면 이동 불가능, 서로 다른 부모
    else:
        idx = arr[i][3]
        end = e

for _ in range(Q):
    x, y = map(int, input().split())
    if connected[x-1] == connected[y-1]: # 부모가 같음 == 점프 가능
        print(1)
    else:
        print(0)
"""


"""
# GPT사용

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

# 입력 처리
N, Q = map(int, input().split())
trees = [list(map(int, input().split())) for _ in range(N)]
quests = [list(map(int, input().split())) for _ in range(Q)]

# Union-Find 초기화
uf = UnionFind(N)

# 통나무 연결 처리
for i in range(N):
    x1_i, x2_i, y_i = trees[i]
    for j in range(i + 1, N):
        x1_j, x2_j, y_j = trees[j]
        if (x1_j <= x2_i and x2_j >= x1_i):  # i와 j가 겹친다면
            uf.union(i, j)

# 질의 처리
for a, b in quests:
    if uf.find(a - 1) == uf.find(b - 1):  # 1-indexed에서 0-indexed로 변환
        print(1)
    else:
        print(0)



# 통나무 N개가 가로 (수평) 방향
# A에서 다른 통나무 B로 정확히 수직 방향으로 점프할 수 있습니다.

# 개구리가 한 통나무에서 다른 통나무로 한번 이상의 점프로
# 이동이 가능한지 판단하는 프로그램을 작성해 주세요.
"""
"""
N, Q = map(int,input().split())
trees = [list(map(int,input().split())) for _ in range(N)]
quest = [list(map(int,input().split())) for _ in range(Q)]

connected = [[0,0]]* N # 연결되어 있는대로
check_idx = trees[0][1]
now_h = trees[0][2]
connected[0][1] = now_h

for i in range(1,N):
    s, e, h = trees[i][0], trees[i][1], trees[i][2]
    if e >= check_idx >= s: # 두 개 사이에 있으면
        check_idx = e
        if
    else:
        connected[i] += 1
        check_idx = e

for j in range(Q):
    if connected[quest[j][0]-1] == connected[quest[j][1]-1]:
        print(1)
    else:
        print(0)

# 겹치면 => 무조건 점프
# 시작점이 끝 점보다 작으면 -> 무조건 실패
"""