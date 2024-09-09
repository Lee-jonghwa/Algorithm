import sys
sys.stdin = open('5656_input.txt','r')
# 구슬은 N번만 쏠 수 있고, 벽돌들은 W x H 배열

# 구슬은 좌, 우로만 움직일 수 있어서 항상 맨 위에 있는 벽돌만 깨트릴 수 있다.
# ② 벽돌은 숫자 1 ~ 9 로 표현되며,
# 구술이 명중한 벽돌은 상하좌우로 (벽돌에 적힌 숫자 - 1) 칸 만큼 같이 제거된다.


# 최대한 많은 벽돌을 제거 -> 남은 벽돌의 개수
# 빈 공간이 있을 경우 벽돌은 밑으로 떨어지게

directions = [(0,1),(0,-1),(1,0),(-1,0)]


def shoot(shots, remains, now_arr):
    global min_v

    # 종료 shot을 다 쓰거나, 남은 shot 없을 때
    if shots == N or remains == 0:
        # 최소값 갱신
        min_v = min(min_v, remains)
        return

    # 폭파 대상이 되는 곳에 대해서 다 터뜨리기
    # 모든 열에 대해서 순회
    for col in range(W):
        # 터뜨릴 row 찾기
        # 매 케이스마다 arr 초기화

        # 시간 단축을 위해 받은 것에 복사본 만들기
        copy_arr = [row[:] for row in now_arr]
        row = -1
        for r in range(H):
            if copy_arr[r][col]:
                row = r
                break
        # 터뜨릴 자리가 없으면 넘어감
        if row == -1: continue

        # 만나는 곳마다 터뜨리기
        # 터뜨릴 자리의 y, x, 파워
        stack = [(row, col, copy_arr[row][col])]
        # 시작 자리 터뜨리기
        now_remains = remains - 1
        copy_arr[row][col] = 0

        # 남은 자리 터뜨리기
        while stack:
            y, x, p = stack.pop()
            for dy, dx in directions:
                for k in range(1, p):
                    ny, nx = y + dy * k, x + dx * k
                    # 배열을 벗어나지 않는 선에서
                    if ny >= H or ny < 0 or nx >= W or nx < 0: continue
                    # 터뜨릴 자리가 아무것도 없으면
                    if copy_arr[ny][nx] == 0: continue
                    # 터뜨릴 수 있는 자리 다시 스택 삽입
                    stack.append((ny, nx, copy_arr[ny][nx]))
                    # 터뜨린 자리 반영
                    copy_arr[ny][nx] = 0
                    # 블록 개수 반영
                    now_remains -= 1

        # 빈자리 바꿔주기
        for c in range(W):
            idx = H - 1  # 밑부터 올려주기
            for r in range(H-1, -1, -1):
                if copy_arr[r][c]: # 1이 있으면
                    # 밑으로 내림
                    copy_arr[r][c], copy_arr[idx][c] = copy_arr[idx][c], copy_arr[r][c]
                    idx -= 1

        shoot(shots + 1, now_remains, copy_arr)


T = int(input())
for tc in range(1, T+1):

    # N: 구슬개수, W: 너비, H: 높이
    N, W, H = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(H)]

    # dfs 접근
    min_v = 1e9

    # 총 벽돌 개수 구하기
    bricks = 0
    for row in range(H):
        for col in range(W):
            if arr[row][col]:
                bricks += 1

    shoot(0, bricks, arr)

    print(f'#{tc} {min_v}')


"""
dy = [-1,1,0,0]
dx = [0,0,-1,1]

def shoot(level, remains, now_arr):
    global min_bricks

    # 기저조건
    # 구슬을 모두 쏘거나, 남는 갯수 없을 때
    if level == N or remains == 0:
        # 최소값 갱신
        min_bricks = min(min_bricks, remains)
        return

    # 한 줄씩 쏘기 -> 벽돌 깨뜨리기, 중력
    for col in range(W):
        # 방법 1.
        # col 위치에 쏘기 전 상태를 복사
        # 원본 리스트의 col 위치에 구슬 쏜다
        # level + 1 이동(다음 재귀 호출)
        # col 위치에 쏘기 전 상태로 복구

        # 방법 2. (복구 시간 개선)
        # col 위치에 쏘기 전 상태를 복사
        # 복사한 리스트에 구슬 쏜다
        # level + 1 이동 + col 위치에 쏜 상태를 함께 전달
        copy_arr = [row[:] for row in now_arr]

        # 구슬을 쏘자
        # 열 순회 하면서 가장 먼저 나오는 0이 아닌 값
        row = -1 # 벽돌이 없다고 가정
        for r in range(H):
            if copy_arr[r][col]: # 벽돌이 있다면
                row = r # 가장 위 행값
                break

        if row == -1: # 벽돌이 없으면
            continue # 다음 열로 진행


        # 연쇄적으로 벽돌 깨뜨림 -> stack / queue 사용
        stack = [(row, col, copy_arr[row][col])]  # 깨져야 할 벽돌 리스트 저장
        now_remains = remains - 1  # 해당 위치 벽돌 개수 반영
        copy_arr[row][col] = 0  # 해당 위치 벽돌 깨짐 처리

        while stack:
            r, c, p = stack.pop()
            for k in range(1,p):  # 파워만큼 가면서 깨짐
                for i in range(4): # 상하좌우
                    nr = r + (dy[i] * k)
                    nc = c + (dx[i] * k)

                    if nr < 0 or nr >= H or nc < 0 or nc >= W:
                        continue

                    if copy_arr[nr][nc] ==0:
                        continue

                    # 다음 벽돌 추가
                    stack.append((nr, nc, copy_arr[nr][nc]))  # 다음 벽돌 추가
                    copy_arr[nr][nc] = 0                      # 벽돌 깨짐
                    now_remains -= 1                          # 숫자 감소

        for c in range(W) :  # 전체 열들을 확인
            idx = H - 1  # 벽돌이 위치할 index
            for r in range(H - 1, -1, -1):
                if copy_arr[r][c]: # 가는 자리에 벽돌 있으면
                    # idx와 r이 같아도 바꿈 --> 의미없는 교환
                    # 가독성을 위함
                    copy_arr[r][c], copy_arr[idx][c] = copy_arr[idx][c], copy_arr[r][c]
                    idx -= 1

        shoot(level + 1, now_remains, copy_arr)

T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(H)]

    # BruteForce -> dfs

    # visited는 필요 없음
    # 2차원 리스트 정보는 가지고 있어야 함
    # 복사본을 수정 후 다음으로 전달하기


    # 1. 최소 벽돌 개수

    # 2. 현재 벽돌이 다 깨지면 더이상 진행할 필요 없음
    # -> 현재 남은 벽돌 수도 같이 저장 필요
    # -> 몇 개 남았는지 매번 순회하면 너무 느림

    # 3. 구슬 쏘는 순회
    # - 시작점: 0번, 하나도 안 깨진 벽돌 수
    # - 끝점: N번 / 벽돌이 다 깨지면



    min_bricks = 12*15
    blocks = 0
    for row in arr:
        for el in row:
            if el: # 0보다 크면
                blocks += 1

    shoot(0, blocks, arr)

    print(f'#{tc} {min_bricks}')

"""