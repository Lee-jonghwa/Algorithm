# N x N 배열 안의 숫자
# M x M 크기의 파리채

def die_paris(arr, N, M):
    max_v = 0
    # 배열 안에서
    for y in range(N):
        for x in range(N):
            #한 점을 찍어서
            sum_v = 0 # 한 번당 잡는 파리 수
            # 파리채 크기 만큼
            for i in range(y, y + M): # 행으로 순회
                for j in range(x, x + M): # 열로 순회
                    # 배열을 벗어나지 않으면
                    if 0 <= i < N and 0 <= j < N:
                        # 그 자리값 더하기
                        sum_v += arr[i][j]
            if max_v < sum_v:
                max_v = sum_v
    return max_v


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = die_paris(arr, N, M)
    print(f'#{tc} {result}')