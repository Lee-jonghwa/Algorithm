choco = ['A', 'B', 'C']

N = int(input())

# lev == N  # N번 뽑음
# branch == 3  # 세 종류 초콜릿
path = []
used = [0] * len(choco) # 중복 순열 문제이므로 사용하진 않음

cnt = 0
def abc(lev):
    global cnt
    if lev == N:
        cnt += 1
        return

    for i in range(len(choco)):
        if lev < 2 or not(path[lev-2] == path[lev-1] == choco[i]):
            used[i] = 1
            path.append(choco[i])
            abc(lev + 1)
            path.pop()
            used[i] = 0


abc(0)
print(cnt)