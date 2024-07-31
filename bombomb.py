arr = [['_'] * 5 for _ in range(4)]


'''
내 풀이
y1, x1 = map(int, input().split())
y2, x2 = map(int, input().split())


# 방향 벡터 : 우 우하 하 좌하 좌 좌상 상 우상
di = [0, 1, 1, 1, 0, -1, -1, -1]
dj = [1, 1, 0 ,-1, -1, -1, 0, 1]

for _ in range(2):
yx, = map
di = [0, 1, 1, 1, 0, -1, -1, -1]
dj = [1, 1, 0 ,-1, -1, -1, 0, 1]
for i in range(8)
ny, nx = y + di[i] , x + dj[j]


for i in range(4): # 모든 행
    for j in range(5): #모든 열
        for k in range(8): # 폭탄이 터지는 모든 방향 지정
            ni = y1 + di[k]
            nj = x1 + dj[k]
            # ni, nj = y1 + di[k], x1 + di[k]
            if 0 <= ni < 4 and 0 <= nj < 5:
                arr[ni][nj] = '#'
        for k in range(8): # 폭탄이 터지는 모든 방향 지정
            ni = y2 + di[k]
            nj = x2 + dj[k]
            if 0 <= ni < 4 and 0 <= nj < 5:
                arr[ni][nj] = '#'

for i in arr:
    print(*i)
'''

'''
# 방법 1
# 한 좌표를 찍었기 때문에 각 행과 열에 대해서 for문이 필요가 없음
for _ in range(2):
    y,x = map(int, input().split())
    di = [0, 1, 1, 1, 0, -1, -1, -1]
    dj = [1, 1, 0 ,-1, -1, -1, 0, 1]
    for i in range(8):
        ni, nj = y + di[i] , x + dj[i]
        if 0 <= ni < 4 and 0 <= nj < 5:
            arr[ni][nj] = '#'

for row in arr:
    print(*row)

'''

'''
# 방법 2 continue
for _ in range(2):
    y, x = map(int, input().split())
    di = [0, 1, 1, 1, 0, -1, -1, -1]
    dj = [1, 1, 0, -1, -1, -1, 0, 1]
    for i in range(8):
        ni, nj = y + di[i], x + dj[i]
        if ni < 0 or nj < 0 or ni > 3 or nj > 4: # 해당 범위동안은 폭탄이 터지지 않음
            continue
        arr[ni][nj] = '#'

for row in arr:
    print(*row)
'''

''''''
# 방법 3 방향 튜플

directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
for _ in range(2): # 폭탄 두 번 터뜨리기
    y, x = map(int, input().split())
    for dy, dx in directions:
        ny, nx = y + dy, x + dx
        if 0 <= ny < 4 and 0 <= nx < 5:
            arr[ny][nx] = '#'

for row in arr:
    print(*row)