T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split()) # 컨테이너 수, 트럭 수
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))
    # 내림차순 정렬
    w.sort(reverse = True)
    t.sort(reverse = True)

    result = 0

    j = -1
    for i in range(M):
        # 각 트럭이 옮길수 있는 화물 찾기
        while j < N - 1:
            j += 1
            # 현재 트럭의 적재용량 보다 무게가 작거나 같은 컨테이너면
            if t[i] >= w[j]:
                result += w[j]
                # 다음 트럭으로 넘어가기
                break
    print(f'#{tc} {result}')



# N개의 컨테이너를 M대의 트럭으로 A도시에서 B도시로 운반하려고 한다.

# 트럭당 한 개의 컨테이너를 운반, 적재용량을 초과하는 컨테이너는 운반할 수 없다.
# A도시에서 B도시로 최대 M대의 트럭이 편도로 한번 만 운행한다고 한다.


# 화물을 싣지 못한 트럭이 있을 수도 있고, 남는 화물이 있을 수도 있다
# 컨테이너를 한 개도 옮길 수 없는 경우 0을 출력한다.

# 화물의 총 중량이 최대가 되도록

"""
T = int(input())
for tc in range(1, T+1):
    # N: 화물 개수, M: 트럭 대수
    N, M = map(int, input().split())
    # 화물 무게
    W = list(map(int,input().split()))
    # 적재용량
    T = list(map(int,input().split()))

    # 적재 용량이 큰 트럭이 무거운 화물을 들 수 있도록
    W.sort(reverse=True)
    T.sort(reverse=True)

    max_w = 0  # 총 중량

    cargo_idx = 0

    for truck in range(M): # 용량이 큰 트럭 부터
        if truck < N: # 주어진 개수에서만
            for cargo in range(cargo_idx,N):
                # 못 들면 넘기기, 큰 순이므로 얘가 못 들면 다음도 못 듦
                if T[truck] < W[cargo]: continue
                max_w += W[cargo]
                cargo_idx= cargo + 1
                break

    # 화물이 더 많을 때

    print(f'#{tc} {max_w}')
"""