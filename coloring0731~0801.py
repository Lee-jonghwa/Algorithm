T = int(input())
color = [1, 2, 3] # 빨강, 파랑, 보라

for tc in range(1, T+1):
    arr = [[0] * 10 for _ in range(10)] # arr 초기화
    N = int(input())
    count = 0
    for _ in range(N): # N 번 정보 받기
        x1, y1, x2, y2, c = map(int, input().split())
        #dy = y1 ~ y2 -> idx : y1 ~ y2+1 -> dif : y2+1 - y1
        #dx = x1 ~ x2 -> idx : x1 ~ x2+1 -> dif : x2+1 - x1
        for i in range(y1, y2 + 1):
            for j in range(x1, x2 + 1):
                if 0 <= i < 10 and 0 <= j < 10:  # 범위 체크 수정
                    if arr[i][j] != 0 and arr[i][j] != c:
                        if arr[i][j] != 3:  # 이미 보라색이 아닌 경우에만 카운트
                            count += 1
                        arr[i][j] = 3
                    else:
                        arr[i][j] = c
    print(f'#{tc} {count}')




'''
# 강사님 해답
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    red_lst = []
    blue_lst = []
    result = 0
    for _ in range(N):
        y1, x1, y2, x2, color = map(int, input().split)
        
        for i in range(y1, y2 + 1):
            for j in range(x1, x2 + 1):
                if color == 1:
                    red_lst.append([i, j])
                if color == 2:
                    blue_lst.append([i, j])
    for common in red_lst:
        result += blue_lst.count(common)
        
    print(f'#{tc} {result}')
'''