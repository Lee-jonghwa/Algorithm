"""
def find_words(N, K):
    cnt = 0
    for y in range(N):
        for x in range(N):
            h = arr[y][x:N]
            v = []
            for k in range(N-y+1):
                v.append([y+k][x])
            if sum(h) == K or sum(v) ==K :
                cnt += 1
    return cnt

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(find_words(N, K))
"""

def find_words(N, K, arr):
    cnt = 0

    # 가로 방향 체크
    for y in range(N):
        length = 0
        for x in range(N):
            if arr[y][x] == 1:
                length += 1
            else:
                if length == K:  # K가 5 미만일 때
                    cnt += 1
                length = 0
        if length == K:  # K가 5일 때
            cnt += 1

    # 세로 방향 체크
    for x in range(N):
        length = 0
        for y in range(N):
            if arr[y][x] == 1:
                length += 1
            else:
                if length == K:
                    cnt += 1
                length = 0
        if length == K:
            cnt += 1

    return cnt


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = find_words(N, K, arr)
    print(f"#{tc} {result}")
