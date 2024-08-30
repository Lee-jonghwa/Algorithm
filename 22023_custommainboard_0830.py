"""
이 문제는 최소 스패닝 트리(Minimum Spanning Tree, MST)를 구하는 문제로 볼 수 있습니다. 주어진 메인보드에서 부품들을 최소 길이의 케이블로 연결해야 하며, 이 과정에서 주어진 조건들을 만족시켜야 합니다.

문제를 해결하기 위해 다음 단계를 따릅니다:

각 부품 그룹을 식별: 서로 인접한 1들은 하나의 부품으로 간주됩니다.
부품 간의 연결 가능한 경로 찾기: 각 부품 간에 직선으로 연결할 수 있는 최단 경로를 찾습니다. 이때 조건에 맞는 경로만을 찾습니다.
최소 스패닝 트리(MST) 찾기: 크루스칼(Kruskal) 알고리즘 등을 이용해 부품들 간의 최소 연결 길이를 구합니다.
결과 출력: MST가 모든 부품을 연결할 수 있다면 그 길이를 출력하고, 그렇지 않으면 -1을 출력합니다.

"""

from collections import deque

# 방향 벡터 (상, 하, 좌, 우)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(board, start, label, N, M):
    """ 같은 부품을 탐색하며 그룹화 """
    queue = deque([start])
    board[start[0]][start[1]] = label
    positions = [start]

    while queue:
        x, y = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 1:
                board[nx][ny] = label
                queue.append((nx, ny))
                positions.append((nx, ny))

    return positions


def find_connections(board, positions, label, N, M):
    """ 다른 부품들과 연결 가능한 경로 찾기 """
    connections = []

    for x, y in positions:
        for dx, dy in directions:
            length = 0
            nx, ny = x + dx, y + dy

            while 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == label:
                    break
                elif board[nx][ny] > 0:
                    if length > 1:  # 길이 1인 케이블은 제외
                        connections.append((length, label, board[nx][ny]))
                    break
                nx += dx
                ny += dy
                length += 1

    return connections


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, rank, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)

    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX] += 1


def kruskal(edges, num_labels):
    edges.sort()
    parent = [i for i in range(num_labels + 1)]
    rank = [0] * (num_labels + 1)
    mst_cost = 0
    edges_used = 0

    for cost, u, v in edges:
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            mst_cost += cost
            edges_used += 1
            if edges_used == num_labels - 1:
                return mst_cost

    return -1


def main():
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    label = 2
    positions_by_label = {}

    # 각 부품 그룹에 대해 BFS를 사용하여 그룹화
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                positions = bfs(board, (i, j), label, N, M)
                positions_by_label[label] = positions
                label += 1

    edges = []
    # 그룹 간의 연결 가능한 모든 경로 찾기
    for lbl1 in range(2, label):
        connections = find_connections(board, positions_by_label[lbl1], lbl1, N, M)
        edges.extend(connections)

    # 최소 스패닝 트리를 Kruskal 알고리즘으로 찾기
    result = kruskal(edges, label - 2)
    print(result)


if __name__ == "__main__":
    main()

# 모든 부품이 모든 다른 부품과 연결해주어야 합니다.
# 다른 부품을 통해서라도 경로만 생성된다면, 모든 부품이 모든 부품에 연결
# 케이블의 양 끝이 직선으로 연결되어야만 두 부품이 연결된 것입니다.
# 케이블을 꺾지 못합니다.
# 교차하여 연결할 수는 있습니다.
# 두 부품을 연결하는 케이블의 길이는 최소 2 이상
# 총 사용한 케이블의 길이를 최소
