# 코딩선은  N개의 지하철 역을 순환하는 순환선
# 노선의 타당도는 (A + B)^2 + (C+D)^2

# A, B, C, D는 각각 한 역의 이용객 숫자를 의미한다.

# 인접한 두 역에서 출발하거나, 인접한 두 역으로 도착하는 직통 노선은 건설할 수 없다.

# 1개의 역에 2개의 직통 노선이 있어서는 안 된다.

# 수환님 풀이
"""
T = int(input())
for test_case in range(1,1+T):
    N = int(input())
    # 최대 한 바퀴를 더 도므로 두 번 만듦
    lst = list(map(int,input().split())) * 2
    ans = 0
    for a in range(N): # 모든 후보를 a로 둘 때
        # b는 a와 인접하지 않은(시작과 끝) 위치에 모두 가능
        for b in range(a + 2,N + a - 1):
            # c는 b와 인접하지 않은(시작과 끝 모두) 위치에 모두 가능
            for c in range(b + 2, N + a - 1):
                # 기존에 있는 조건이 모두 충족된 것이기 때문에 어려운 점 없음
                # d는 c와 인접하지 않은(시작과 끝 모두) 위치에 모두 가능
                for d in range(c + 2, N + a - 1):
                    ans = max(ans, (lst[a]+lst[b])**2 + (lst[c]+lst[d])**2)

    # 근데 각 조건이 어떻게 만족되는 거지...? 그냥 최대값으로 박은 건가?
    # 한 바퀴를 돌아선 중복이 될 수 있을 거 같은데
    print(f'#{test_case} {ans}')
"""

# dfs로 가보자

def cal_tadang(path, stations):
    return (stations[path[0]] + stations[path[1]]) ** 2\
           + (stations[path[2]] + stations[path[3]]) ** 2


def dfs(lev): # 10개 중 4개 고르는 선택지
    global max_v

    if lev == 4:
        # 교차조건 확인 -> 둘 다 크거나, 둘 다 작음
        A, B = path[0], path[1]
        if A > B:
            A, B = B, A
        C, D = path[2], path[3]
        if A < C < B or A < D < B: # 둘 중 하나라도 사이에 있으면
            # 단축 떄문에 둘 다 안에 있는 경우를 컷 하는 건 없음
            return

        max_v = max(max_v,cal_tadang(path, stations))
        return

    for i in range(N): # 모든 후보군 N개
        if visited[i]: continue # 방문지 제외

        # 양 옆 체크
        # 원형 인덱스 반영
        if visited[(i-1) % N] or visited[(i + 1) % N]: continue

        path.append(i)
        visited[i] = 1
        dfs(lev+1)
        visited[i] = 0
        path.pop()


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    stations = list(map(int,input().split()))

    visited = [0] * N
    path = []
    max_v = 0
    dfs(0)

    print(f'#{tc} {max_v}')



"""


def make_permutation(v, c_idx, lst2):
    global ans
    if len(lst2) == 2:
        a, b = lst2[0]
        if a > b:
            a, b = b, a
        c, d = lst2[1]
        if a < c < b or a < d < b:
            return
        cnt = (lst[a] + lst[b]) ** 2 + (lst[c] + lst[d]) ** 2
        ans = max(cnt, ans)
        return
    if c_idx != -1:
        for idx in range(N):
            if not v[idx]:
                n_v = v[:]
                n_v[idx], n_v[(idx + 1) % N], n_v[(idx - 1)] = True, True, True
                make_permutation(n_v, -1, lst2 + [(c_idx, idx)])
    else:
        for idx in range(N):
            if not v[idx]:
                n_v = v[:]
                n_v[idx], n_v[(idx + 1) % N], n_v[(idx - 1)] = True, True, True
                make_permutation(n_v, idx, lst2)


T = int(input())
for test_case in range(1, 1 + T):
    N = int(input())
    lst = list(map(int, input().split()))
    v_lst = [False] * N
    pick = []
    ans = 0
    make_permutation(v_lst, -1, [])
    print(f'#{test_case} {ans}')
"""