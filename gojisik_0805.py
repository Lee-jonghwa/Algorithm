
# 고지식 upgrade

def f(t, p): # 패턴 p와 일치하는 구간의 시작 인덱스 return, 일치하는 경우가 없으면 -1
    N = len(t)
    M = len(p)

    for i in range(N-M+1):
        for j in range(M):
            if t[i+j] != p[j]:
                break
        else:
            return i
    return -1

t = 'ABCDEFGHAEDHB'
p = 'TTA'
print(f(t, p))