'''

N x N 사각형의 전투장에는 각 칸마다 몇 마리의 몬스터가 있는지 적혀 있다.
광대한 영역에 마법을 시전할 수 있는 마법사 Mort 는 전투장에서 최대한 많은 몬스터를 잡으려한다.

마법사 Mort는 대각선 방향으로 각 방향마다 K 칸 만큼 마법을 시전할 수 있다.

마법은 마법사가 있는 지점에서 마법을 시전한 위치를 제외하고
대각선 방향으로 방향 변화 없이 시전된다.


예를들어 [그림1]와 같은 5 x 5 인 전투장에서

노란색으로 표시된 2번 행 2번 열에서 K = 2 인 마법을 시전하게되면
각 방향마다 2칸씩 , [그림2] 와 같이 몬스터를 공격하게 되며

총 1 + 10 + 7 + 2 + 2 + 2 + 1 + 1 = 26 마리를 처치하게 된다.

반면에 [그림3]와 같이 0번 행 2번 열에서 K = 2인 마법을 시전하면 [그림4] 와 같이 아래 대각선 방향 K칸에 해당되는몬스터를 공격하게 되며

총 7 + 2 + 0 + 7 = 16 마리 몬스터를 처치할 수 있다.

 마법사 Mort 씨가마법을 한번 시전하여처치할수 있는 몬스터의 최대 수를 출력하시오.

[입력]
첫째줄에 전투장의 가로세로크기인 N 이 입력된다. (1 <= N <= 100)
다음 줄부터는 N 줄에 걸쳐 각줄마다 N개의 정수가 공백으로 구분되어 입력된다. ( 0<= 정수 <= 100,000)
마지막 줄에는 마법의 시전범위 K 가 입력된다. (1 <= K <= 100)

[출력]
마법사가 잡을 수 있는 몬스터의 최대 수를 출력하시오.
'''

'''
#내 풀이
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
K = int(input())

# 벡터 : 우상 좌상 좌하 우하
di = [-1, -1, 1, 1]
dj = [1, -1, -1, 1]

# 모든 원소 순회하여
max_v = 0
for i in range(N): # 모든 행 순회
    for j in range(N): # 모든 열 순회
        sum_v = 0
        for k in range(4): # 모든 방향
            for m in range(1, K+1):
                ni = i + m * di[k]
                nj = j + m * dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    sum_v += arr[ni][nj]
        if max_v < sum_v:
            max_v = sum_v
print(max_v)
'''

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
K = int(input())

def magic(y, x):
    dy = [-1, 1, -1, 1]
    dx = [1, 1, -1, -1]
    sum_v = 0
    for i in range(4): # 마법의 방향
        # 마법의 파워(자신의 위치를 제외-> 1부터 시작)
        for j in range(1, K+1):
            ny = y + dy[i] * j # 방향에 파워만큼 곱함
            nx = x + dx[i] * j
            if 0 <= ny < N and 0 <= nx < N:
                sum_v += arr[ny][nx]
    return sum_v

result_list = [magic(i,j) for i in range(N) for j in range(N)]
print(max(result_list))
