arr = [[0] * 10 for _ in range(10)]

T = int(input())
color = [1, 2, 3] # 빨강, 파랑, 보라

for tc in range(1, T+1):
    N = int(input())
    for c in range(N): # N 만큼 정보 받기
        y1, x1, y2, x2, c = map(int, input().split())
        #dy = y1 ~ y2 -> idx : y1 ~ y2+1 -> dif : y2+1 - y1
        #dx = x1 ~ x2 -> idx : x1 ~ x2+1 -> dif : x2+1 - x1
        for i in range(y1, y2 + 1):
            for j in range(x1, x2 + 1):
                arr[i][j] = c
                if arr[i][j] != 0 or arr[i][j] != c:
                    arr[i][j] == 3
    for row in range(len(arr)):
        print(*arr)
