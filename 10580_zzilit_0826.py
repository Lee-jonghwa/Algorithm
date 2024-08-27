def KFC():
    cnt = 0
    for i in range(len(arr)):
        pass


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []


"""
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ab = [list(map(int, input().split())) for _ in range(N)]

    ab.sort()

    cnt = 0
    for i in range(N):
        for j in range(i): # i 보다 작은 요소 중에서
            if ab[j][1] > ab[i][1]: # 그 연결값이 크면
                cnt += 1

    print(f'#{tc} {cnt}')

"""




"""
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ab = [list(map(int, input().split())) for _ in range(N)]

    ab.sort()
    # 교차하려면 하나가 클 때 하나가 작거나
    # 하나가 작을 때 하나를 큼

    cnt = 0
    for i in range(1, N): # A쪽 순회
        for j in range(i): # A는 더 낮지만 B가 더 높은 경우 교차
            if ab[j][1] > ab[i][1]:
                cnt += 1

    print(f'#{tc} {cnt}')
"""