arr = [[0] * 7 for _ in range(2)]
K = 7
N = 5
for i in range(4):
    arr[0][i] = N + i
    arr[1][7-1-i] = N - i
print(arr)


# 2진수 문제
 # 진수표(하드코딩)