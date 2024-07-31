# 방법 2 continue
arr = [['_'] * 5 for _ in range(4)]
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