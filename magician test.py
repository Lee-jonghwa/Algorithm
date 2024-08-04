N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

K = int(input())

dy = [-1, -1, 1, 1]
dx = [1, -1, -1, 1]

# max_v = 0
# for i in range(N):
#     for j in range(N):
#         sum_v = 0
#         for m in range(4):
#             for k in range(1, K+1):
#                 ny, nx = i + dy[m] * k, j + dx[m] * k
#                 if 0 <= ny < N and 0 <= nx < N:
#                     sum_v += arr[ny][nx]
#         max_v = max(max_v, sum_v)

# print(max_v)


def magic(y,x):
    sum_v = 0
    for i in range(4):
        for k in range(1, K+1):
            ny, nx = y + dy[i] * k, x + dx[i] * k
            if 0 <= ny < N and 0 <= nx < N:
                sum_v += arr[ny][nx]
    return sum_v

result = [magic(i,j) for i in range(N) for j in range(N)] # max를 위한 리스트
print(max(result))