N = int(input())

# lev == N   # N 개의 숫자 활용
# branch == 9 # 1~9 까지의 숫자

cnt = 0
path = []
used = [0] * (9 + 1) # 조합 문제로 사용하지 않음
def sum_10(lev):
    global cnt
    if lev == N:
        if sum(path) == 10:
            cnt += 1
        return

    for i in range(1, 10):
        used[i] = 1
        path.append(i)
        sum_10(lev + 1)
        path.pop() # 재귀호출 했을 때 길 제거
        used[i] = 0 # 재귀호출 했을 때 사용 반환

sum_10(0)
print(cnt)