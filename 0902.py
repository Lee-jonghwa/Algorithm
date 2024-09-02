# for i in range(1,4):
#     for j in range(1,4):
#         print(i, j)

#
# def KFC(x):
#     if x == 6:
#         return
#
#     else:
#         print(x, end=" ")
#         KFC(x+1)
#         print(x, end=" ")
#
# KFC(0)


"""
path = []

def KFC(x):
    if x == 3:
        print(path)
        return

    for i in range(1, 7):
        path.append(i)
        KFC(x+1)
        path.pop()

KFC(0)

"""



"""
path_rep = []
path = []

def permutation_rep(lev):
    if lev == 2:
        print(path_rep)
        return

    for i in range(1, 7):
        path_rep.append(i)
        permutation_rep(lev + 1)
        path_rep.pop()

used = [0]*7
def permutation(lev):
    if lev == 2:
        print(path)
        return

    for i in range(1, 7):
        if used[i] == 1: continue
        used[i] = 1
        path.append(i)
        permutation(lev + 1)
        path.pop()
        used[i] = 0

permutation_rep(0)
print()
permutation(0)
"""


# 3 번 던졌을 때 눈금의 합이 10 이하일 때만 출력ㄴ

path = []
cnt = 0

def dice(lev, sum_v):
    global cnt

    # 가지치기, 백트래킹
    if sum_v > 10:
        return

    if lev == 3:
        cnt += 1
        return

    for i in range(1,7):
        path.append(i)
        dice(lev + 1, sum_v + i)
        path.pop()

dice(0, 0)
print(cnt)