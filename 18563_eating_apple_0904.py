import sys
sys.stdin = open('18563_input.txt', 'r')

# 오 - 아래 - 왼 - 위
directions = [(0,1),(1,0),(0,-1),(-1,0)]


def find_apples(arr):
    apples = []
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                apples.append((arr[i][j], i, j))
    apples.sort()
    apples = [(y, x) for _, y, x in apples]
    return apples

def turn_right(now_dir):
    return (now_dir + 1) % 4

# 방향배열 따지기
def eating_apples(arr):
    apples = find_apples(arr)
    now_pos = (0, 0)  # 시작

    now_dir = 0 # 지금 보는 방향
    turn_cnt = 0

    # 1번부터 찾으러 가기
    for apple_y, apple_x in apples:
        while now_pos != (apple_y, apple_x): # 찾을 때까지
            ny, nx = now_pos[0] + directions[now_dir][0], now_pos[1] + directions[now_dir][1]

            # 배열을 벗어나지 않는 선에서
            if ny < 0 or ny >= N or nx < 0 or nx >= N: continue
            # 현재 방향 유지 조건
            if (now_dir == 0 and nx <= apple_x) or \
                (now_dir == 1 and ny <= apple_y) or \
                (now_dir == 2 and nx >= apple_x) or \
                (now_dir == 3 and ny >= apple_y):
                now_pos = (ny, nx)

            # 우회전 조건
            else:
                now_dir = turn_right(now_dir)
                turn_cnt += 1

    return turn_cnt


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    result = eating_apples(arr)
    print(f'#{tc} {result}')


"""BFS
from collections import deque

# 오른쪽으로 순서대로 돌기
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def finding_apples(arr):
    apples = []
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                apples.append((arr[i][j], i, j))

    apples.sort()
    # 사과 번호 순으로 정리
    return [(y, x) for _, y, x in apples]

def bfs(N, start, target, go_dir):
    # 시작 y, 시작 x, 방향, 우회전 횟수
    queue = deque([(start[0], start[1], go_dir, 0)])
    visited = set()
    # 방향까지 고려해서 visited 해야함
    visited.add((start[0],start[1],go_dir))

    while queue:
        y, x, go_dir, turns = queue.popleft()

        # 목표 위치에 도달했으면
        if (y,x) == target:
            return turns

        # 다음 자리 찾기
        # 현재 방향으로 전진
        ny, nx = y + directions[go_dir][0], x + directions[go_dir][1]
        if ny < 0 or ny >= N or nx < 0 or nx >= N: continue
        if (ny, nx, go_dir) not in visited:
            visited.add((ny,nx,go_dir))
            queue.append((ny,nx,go_dir,turns))

        # 우회전 하기
        new_dir = (go_dir + 1) % 4  # 방향 순회 반영
        if (y, x, new_dir) not in visited:
            visited.add((y, x, new_dir))
            queue.append((y, x, new_dir, turns + 1))

    return float('inf') # 디버깅


def eating_apples(arr, N):
    apples = finding_apples(arr)
    start = (0, 0)
    direction = 0 # 처음엔 오른쪽 방향
    total_turns = 0

    for target in apples:
        # BFS를 통해 현재 위치에서 다음사과 위치로 이동
        turns = bfs(N, start,target,direction)
        total_turns += turns

        # 사과를 먹고 나서 다시 bfs 시작, 방향 유지
        start = target
        direction = (direction + turns) % 4

    return total_turns

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    result = eating_apples(arr, N)
    print(f'#{tc} {result}')

"""


"""
from collections import deque

# 방향: 동(0, 1), 남(1, 0), 서(0, -1), 북(-1, 0)
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def find_apples(arr, N):
    apples = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] > 0:
                apples.append((arr[i][j], i, j))
    apples.sort()  # 사과 번호 순서대로 정렬
    return [(y, x) for _, y, x in apples]

def bfs(N, start, target, initial_dir):
    queue = deque([(start[0], start[1], initial_dir, 0)])
    visited = set()
    visited.add((start[0], start[1], initial_dir))

    while queue:
        y, x, dir_index, turns = queue.popleft()

        # 목표 위치에 도달한 경우
        if (y, x) == target:
            return turns

        # 현재 방향으로 전진
        ny, nx = y + directions[dir_index][0], x + directions[dir_index][1]

        # 맵 범위 내에 있고 방문하지 않은 위치
        if 0 <= ny < N and 0 <= nx < N and (ny, nx, dir_index) not in visited:
            visited.add((ny, nx, dir_index))
            queue.append((ny, nx, dir_index, turns))

        # 우회전
        new_dir_index = (dir_index + 1) % 4
        if (y, x, new_dir_index) not in visited:
            visited.add((y, x, new_dir_index))
            queue.append((y, x, new_dir_index, turns + 1))

    return float('inf')  # 도달할 수 없는 경우 큰 값 반환

def eating_apples(arr, N):
    apples = find_apples(arr, N)
    start = (0, 0)
    direction = 0  # 처음엔 오른쪽(0, 1) 방향
    total_turns = 0

    for target in apples:
        # BFS를 통해 현재 위치에서 다음 사과 위치로 이동
        turns = bfs(N, start, target, direction)
        total_turns += turns
        # 사과를 먹고 나면 그 위치에서 다시 시작, 방향 유지
        start = target
        direction = (direction + turns) % 4

    return total_turns

# 입력 및 실행
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = eating_apples(arr, N)
    print(f"#{tc} {result}")
"""



# direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#
# def find_apples(arr):
#     res_apples = []
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j]:
#                 res_apples.append((arr[i][j], i, j))
#     res_apples.sort()
#     return [(y, x) for _, y, x in res_apples]
#
# def turn_right(dir_index):
#     return (dir_index + 1) % 4
#
# def eating_apples(arr):
#     apples = find_apples(arr)
#     now_pos = (0, 0)
#     dir_index = 0  # 처음엔 오른쪽(0, 1)을 향함
#     turn_count = 0
#
#     for apple_y, apple_x in apples:
#         while now_pos != (apple_y, apple_x):
#             next_y, next_x = now_pos[0] + direction[dir_index][0], now_pos[1] + direction[dir_index][1]
#
#             if 0 <= next_y < N and 0 <= next_x < N:
#                 if (dir_index == 0 and next_x <= apple_x) or \
#                    (dir_index == 1 and next_y <= apple_y) or \
#                    (dir_index == 2 and next_x >= apple_x) or \
#                    (dir_index == 3 and next_y >= apple_y):
#                     now_pos = (next_y, next_x)
#                 else:
#                     dir_index = turn_right(dir_index)
#                     turn_count += 1
#             else:
#                 dir_index = turn_right(dir_index)
#                 turn_count += 1
#
#     return turn_count
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     result = eating_apples(arr)
#     print(f"#{tc} {result}")


"""

direction = [(0,1),(1,0),(0,-1),(-1,0)]

def find_apples(arr):
    res_apples = []
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                res_apples.append((arr[i][j], i, j))
    res_apples.sort()  # 사과 번호 순서대로 정렬
    # 순서 빼고 리턴
    return [(y,x) for _, y, x in res_apples]

def turn_right(now_dir):
    return (now_dir+1)%4 # 4에서 순환

def eating_apples(arr):
    apples = find_apples(arr)
    now_pos = (0, 0) # 시작점

    now_dir = 0
    turn_cnt = 0

    for apple_y, apple_x in apples:
        while now_pos != (apple_y, apple_x): # 사과를 찾을 때까지
            next_y, next_x = now_pos[0] + direction[now_dir][0], now_pos[1] + direction[now_dir][1]

            if 0 <= next_y < N and 0 <= next_x < N: # 배열 안에서 순회
                # 방향이 맞으면
                if (now_dir == 0 and next_x <= apple_x) or\
                    (now_dir == 1 and next_y <= apple_y) or\
                    (now_dir == 2 and next_x >= apple_x) or\
                    (now_dir == 3 and next_y >= apple_y):
                    now_pos = (next_y, next_x)
                else:
                    now_dir = turn_right(now_dir)
                    turn_cnt += 1

            # 방향을 벗어나면
            else:
                now_dir = turn_right(now_dir)
                turn_cnt += 1

    return turn_cnt

    # 행 순회를 하다가 i 를 발견하면 -> 찾아감
    # 다른 거 순회하다가 2를 발견하면 -> 찾아감...

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    result = eating_apples(arr)
    print(f'#{tc} {result}')
"""
"""
5 <= N <= 10
1 <= M <= 10
사과의 번호는 1~M번까지 중간 값의 누락 없이 주어짐이 보장된다. (예 : M = 3이라면, 1 2 3 이 모두 주어짐이 보장된다.)
사과는 N x N 크기의 맵의 테두리 부분에 주어지지 않는다. (0번 행, 0번 열, N-1번 행, N-1번 열)
i번째 사과와 i+1번째 사과의 위치는 같은 행, 열에 주어지지 않음이 보장된다.
단, i번째 사과와 i+2번째 사과의 위치는 같은 행, 열에 주어질 수 있다. 
"""