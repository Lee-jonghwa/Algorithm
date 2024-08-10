# 기본 배열
arr = [["_"] * 5 for _ in range(4)]
# 폭탄 1 좌표
y1, x1 = map(int, input().split())
# 푝탄 2 좌표
y2, x2 = map(int, input().split())

directions = [(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1)] # 8 방향

def bombbomb(arr, y, x, directions): # 터뜨리는 함수
    # 제자리는 안 터뜨리므로 변경 x
    for dy, dx in directions:
        ny, nx = y + dy, x + dx
        if 0 <= ny < 4 and 0 <= nx <5: # 배열을 벗어나지 않는 선에서
            arr[ny][nx] = "#" # 중복되어도 상관 x

bombbomb(arr, y1, x1, directions)
bombbomb(arr, y2, x2, directions)

for i in range(4): # 열의 개수 동안에
    print(*arr[i]) # 각 요소 출력