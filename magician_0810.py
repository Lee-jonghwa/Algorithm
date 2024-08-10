N = int(input())
# 배열 생성 -> 2차원 배열이므로 리스트 안의 리스트 만들기
arr = [list(map(int, input().split())) for _ in range(N)]
K = int(input()) # 마법의 세기

# 대각선
directions = [(-1,1),(-1,-1),(1,-1),(1,1)]

max_v = 0 # 몬스터 최대값 저장

# 이 문제는 테케를 받는게 아니므로, 별도 함수 작성하지 않음
for y in range(N): # 행 순회
    for x in range(N): # 열 순회
        sum_v = 0 # 매 지점에서의 공격 범위 설정
        for k in range(1, K+1):
            # 공격 범위, 제자리는 제외하므로 1부터(0부터면 4번이 추가됨), K까지 되어야하므로 K+1
            for dy, dx in directions: # 방향 순회
                ny, nx = y + dy * k, x + dx * k # 범위만큼 곱하기
                if 0 <= ny < N and 0 <= nx < N: # 배열을 벗어나지 않는 범위 안에서
                    sum_v += arr[ny][nx]  # 공격값 저장
        if max_v < sum_v:
            max_v = sum_v

print(max_v)