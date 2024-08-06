cnt = 0

def f(N):
    global cnt
    if N % 2 == 0:
        cnt += 1
        return f(N // 2)
    else:
        if N == 1:
            return
        cnt += 1
        return f(N * 3 + 1)

N = int(input())
f(N)
print(cnt)