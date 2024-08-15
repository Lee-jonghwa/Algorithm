def fivestone(N, arr):
    for y in range(N):
        for x in range(N):
            if arr[y][x] == 'o':  # 돌이 있는 위치에서만 시작
                for dy, dx in [(0, 1), (1, 0), (1, 1), (1, -1)]: # 찍는 점이 무조건 시작점이라고 가정하면
                    cnt = 0
                    for k in range(5):
                        ny, nx = y + dy * k, x + dx * k # 한 방향에 해서 5번 전진, 제자리 포함되도 상관 없음
                        if 0 <= ny < N and 0 <= nx < N and arr[ny][nx] == 'o': # 해당 방향이 o 면
                            cnt += 1
                        else:
                            break  # 5개 연속되지 않으면 break
                    if cnt == 5:  # 5개 연속된 경우
                        return "YES"
    return "NO"  # 5개 연속된 돌이 없는 경우


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [input().strip() for _ in range(N)]  # 입력을 리스트로 받아 처리
    result = fivestone(N, arr)
    print(f'#{tc} {result}')


# 배열로 접근해보기

"""
def fivestone(N, arr):
    cnt = 0
    for y in range(N):
        for x in range(N):
            if arr[y][x] == 'o': # o인 곳을 하나 찍어서
                slash1 = 0  # 정방향 대각선 / 시작점이 이미 o 기 때문에 1로 시작
                slash2 = 0  # 역방향 대각선
                v = 0       # 세로
                h = 0       # 가로
                for dy, dx in [(-1, -1), (1, 1), (1,-1), (-1,1),(-1, 0), (1, 0),(0, -1), (0, 1)]:
                    for k in range(5): # 5칸 이상이기만 하면 됨 # 자리 포함 값
                        ny, nx = y + dy * k, x + dx * k
                        if 0 <= ny < N and 0 <= nx < N and arr[ny][nx] == 'o': # 배열을 넘지 않는 선에서 o 추가
                            if (dy, dx) == (-1, -1) or (dy, dx) == (1, 1): # 정방향으로 펴지면
                                slash1 += 1
                            elif (dy, dx) == (-1, 1) or (dy, dx) == (1, -1): # 역방향으로 펴지면
                                slash2 += 1
                            elif (dy, dx) == (-1, 0) or (dy, dx) == (1, 0): # 세로로 퍼지면
                                v += 1
                            else: # 가로로 펴지면
                                h += 1
                if slash1 >= 5 or slash2 >= 5 or v >= 5 or h >= 5:  # 어느 방향이라도 5개 이상이 있으면
                    cnt += 1
    if cnt: # 하나라도 있으면
        return "YES"
    else:
        return "NO"



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    result = fivestone(N, arr)
    print(f'#{tc} {result}')
"""