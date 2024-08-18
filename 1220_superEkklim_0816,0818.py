
# 한 열에 N-S 순서로 있으면 교착
# 1은 N극 성질 2는 S극 성질

def magnetic():
    cnt = 0
    for x in range(N): # 매 열 순회
        ismag = False # 교착 확인
        for y in range(N):
            if mag[y][x] == 1: # N 이면
                ismag = True
            elif mag[y][x] == 2:
                if ismag == True:
                    cnt += 1
                    ismag = False

    return cnt

for tc in range(1, 11):
    N = int(input())
    mag = [list(map(int, input().split())) for _ in range(N)]
    result = magnetic()
    print(f'#{tc} {result}')




"""
# 시간이 흐른 뒤에 자성체들이 서로 충돌하여 테이블 위에 남아있는 교착 상태의 개수를 구하라.

# 반대 방향으로 움직이는 자성체가 하나라도 있으면 교착 상태에 빠져 움직이지 않는다.


# 자성체는 테이블 앞뒤 쪽에 있는 N극 또는 S극에만 반응하며 자성체끼리는 전혀 반응하지 않는다.

# 테이블의 크기는 100x100

# 1은 N극 성질을 가지는 자성체를 2는 S극 성질을 가지는 자성체

# 윗부분에 N극이 아래부분에 S극이 위치한다고 가정한다.


# S -> y 값이 0으로, N은 y 값이 N으로
# 위에서 부터 1,2 순서대로 있으면 cnt + 1
# 아닌 상황은 신경쓸 필요 없음

def uuuuuuuu_magneetic(arr):
    cnt = 0
    for x in range(N):
        # 각 열에 대해서
        isNS = 0
        for y in range(N):
            # N을 만났을 때
            if arr[y][x] == 1:
                isNS = 1
            # S를 만났을 때
            elif arr[y][x] == 2:
                # 이전에 N을 만났으면
                if isNS == 1:
                    # cnt 추가
                    cnt += 1
                    # 상태 초기화
                    isNS = 0
    return cnt


for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = uuuuuuuu_magneetic(arr)
    print(f'#{tc} {result}')
"""