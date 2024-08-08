'''
## 미로 풀이 - 방문칸 표시

def fstart(N):
    for i in range(N):
        for j in range(N):
            if a[i][j] == 2:
                return i, j
    return -1, -1


def dfs2(i, j , N):
    visited[i][j] = 1
    if a[i][j] == 3:
        return 1
    else:
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and a[ni][nj] != 1 and visited[ni][nj]==0:
                if dfs2(ni, nj, N):
                    return 1
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = [list(map(int, input())) for _ in range(N)] # 배열 생성 - 리스트 컴프리헨션
    visited = [[0]*N for _ in range(N)]
    sti, stj = fstart(N)
    print(f'#{tc} {dfs2(sti, stj, N)}')
'''


'''
# branch == 3
# level == 2
path = []

def KFC(x):
    if x == 2:
        # 정점 노드에 도달했을 때 출력
        print(path)
        return

    for i in range(3):
        # 재귀호출을 하기 "직전" path에 기록
        path.append(i)
        KFC(x+1)
        # 잘못 됐을 때 함수가 리턴되고 돌아오자마자 기록 삭제
        path.pop()

KFC(0)


# 주사위 3개를 던저 나올 수 있는 모든 경우의 수
# branch == 6
# level == 3

path = []

def outback(x):
    if x == 3: # level ==3
        print(*path)
        return

    for i in range(1, 7): # branch 1 ~ 6
        path.append(i) # 재귀 함수를 호출하기 직전 내 위치 기록
        outback(x+1)
        path.pop() # return 한 직후 기록 삭제

outback(0)


# level == 5
# branch == 4

path = []
def BGK(x):
    if x == 5: #level ==5
        print(*path)
        return

    for i in range(1, 5):
        path.append(i)
        BGK(x+1)
        path.pop()
BGK(0)

'''

'''
# 순열 중복 제거 하기

# branch == 3
# level == 2
path = []
used = [0, 0, 0]

def KFC(x):
    if x == 2:
        # 정점 노드에 도달했을 때 출력
        print(path)
        return

    for i in range(3):
        # 이미 사용한 숫자인지 구분 -> 사용하면 재귀 호출 생략
        if used[i] == 1:
            continue
        # 처음 사용하는 숫자(흔적)이라면 used에 기록
        used[i] = 1
        # 재귀호출을 하기 "직전" path에 기록
        path.append(i)
        KFC(x+1)
        # 잘못 됐을 때 함수가 리턴되고 돌아오자마자 기록 삭제
        path.pop()
        # 모든 처리가 끝나고 돌아왔다면, used 배열의 기록 지움 --> 항상 기록을 하면 지워야함!
        used[i] = 0

KFC(0)
'''

'''
path = []
def dice1(x, N):
    if x == N:
        print(*path)
        return

    for i in range(1, 7):
        path.append(i)
        dice1(x+1, N)
        path.pop()
dice1(0, 2)

path = []
used = [False for _ in range(7)]
N = 0
def dice2(x):
    if x == 2:
        print(*path)
        return

    for i in range(1, 7):
        if used[i] == 1:
            continue
        used[i] = 1
        path.append(i)
        dice2(x+1)
        path.pop()
        used[i] = 0
dice2(0)

'''

'''
path = []
N = 0

def type1(x):
    if x== N:
        return

    for i in range(1, 7):
        path.append(i)
        type(x+1)
        path.pop()

def type2(x):
    if x == N:
        print(*path)
        return

    for i in range(1, 7):
        if used[i] == True:
            continue
        used[i] = 1
        path.append(i)
        type2(x+1)
        path.pop()
        used[i] = False


N, type = map(int, input().split())
used = [False for _ in range(7)] # branch 개수 +1 만큼 초기화

if type == 1:
    type1(0)
else:
    type2(0)
'''
'''
path = []
cnt = 0

def dice(x, sum_v):
    global cnt
    # 가지치기
    if sum_v > 10:
        return

    if x == 3:
        cnt += 1
        return

    for i in range(1, 7):
        path.append(i)
        dice(x + 1, sum_v + i)
        path.pop()

dice(0, 0)
print(cnt)
'''

'''

def check(arr):
    stack = []
    for i in arr[:-1]: # 마지막 '.' 제외하고 순회
        if i.isdecimal(): # 숫자일 경우
            stack.append(int(i))

        elif i in {'+', '-', '*', '/'}: # 기호일경우
            if len(stack) < 2: # 스택에 숫자가 2개 미만이면 return 에러
                return 'error'
            b = stack.pop() # 두 번째 숫자
            a = stack.pop() # 첫 번째 숫자
            if i == '+': stack.append(a + b)
            elif i == '-': stack.append(a - b)
            elif i == '*': stack.append(a * b)
            elif i == '/': stack.append(a // b)

    if len(stack) != 1:
        return 'error'

    return stack[0] # 최종 결과 반환

T = int(input())
for tc in range(1, T + 1):
    Forth = input().split()
    result = check(Forth)
    print(f'#{tc} {result}')
'''


'''
def maze(arr, N):
    start = find_start(arr, N)
    stack = [start]
    while stack:
        y, x = stack.pop() # 현재위치
        arr[y][x] = -1 # 지나간 길 표시
        dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        for dy, dx in dir:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N:
                if arr[ny][nx] == 3:
                    return 1 # 도착점을 찾으면 return 1
                elif arr[ny][nx] == 0: # 갈 수 있는 곳이다 ---> stack에 추가
                    stack.append((ny, nx))

    return 0 # 도착점을 찾지못하면 return 0

def find_start(arr, N):
    for y in range(N):
        for x in range(N):
            if arr[y][x] == 2:
                return y, x

T = int(input())
for tc in range(1, T + 1):
    N = int(input()) # 미로의 크기 NxN 행렬
    arr = [list(map(int ,input())) for _ in range(N)] # 미로
    result = maze(arr, N)
    print(f'#{tc} {result}')
'''

test = 'JAEZNNZEAJ'
print(test[0:0+10])
print(test[::-1])