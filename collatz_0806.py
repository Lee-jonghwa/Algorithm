def f(num, level):
    # 기저
    if num == 1:
        print(level)
        return
    if num % 2 == 0:
        f(num/2 , level+1)
    else:
        f(num*3+1, level+1)

N = int(input())
f(N, 0)


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