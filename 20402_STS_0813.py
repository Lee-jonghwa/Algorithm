arr = ['B', 'T', 'S', 'K', 'R']
N = int(input())

cnt = 0
used = [0] * (len(arr)+1)
path = []  # 명단에 포함
# N 명을 뽑는다 level == N
# 5 명 중 뽑는다 branch == 5

def BTS(lev):
    global cnt
    if lev == N:  # 3명 뽑으면, S가 포함되어 있는 팀에
        if 2 in path:
            cnt += 1  # 횟수 리턴
        return

    for i in range(5):  # branch 동안
        if used[i] == 1:  # 사용한 것 체크
            continue
        used[i] = 1 # 사용한 것 아니면 체크
        path.append(i) # 지금 위치 path 기록
        BTS(lev + 1)
        path.pop()  # 잘못됐을 때 돌아오면 다시 다른 곳으로 갈 수 있게 열어둠
        used[i] = 0  # 다 다녀오면 다시 사용할 수 있게 열어둠

BTS(0)
print(cnt)