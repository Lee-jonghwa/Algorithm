def comb(x):
    global cnt, sum_v, sum_vs
    if x == N:
        if sum_v == 10:
            cnt += 1
            sum_v = 0
            return
        else:
            sum_v = 0
            return
    for i in range(1, 9):
        sum_v += i
        comb(x+1)




N = int(input())
cnt = 0
sum_v = 0
path = []

comb(0)

print(cnt)