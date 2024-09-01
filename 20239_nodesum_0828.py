T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0]*(N+1) # 트리 초기화

    for _ in range(M):
        idx, value = map(int, input().split()) # 주어지는 값들에서
        tree[idx] = value

    for i in range(N, 0, -1):
        if i//2 >= 0: # 트리를 벗어나지 않는 선에서
            tree[i//2] += tree[i]

    print(f'#{tc} {tree[L]}')





"""
T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)  # 트리 초기화
    for i in range(M):
        node, value = map(int, input().split())
        tree[node] = value

    for i in range(N, 0, -1): #끝에서 돌아오면서 진행
        if i // 2 > 0: # tree를 벗어나지 않는 선에서
            tree[i//2] += tree[i]

    result = tree[L]

    print(f'#{tc} {result}')
"""


"""
T = int(input())
for tc in range(1, T+1):
    # N: 총 노드 개수, M: 리프노드 개수, L: 값을 출력할 노드번호
    N, M, L = map(int, input().split())
    tree = [0] * (N + 1)  # 노드 번호는 1부터 N까지

    # 리프 노드 값 저장
    for _ in range(M):
        node, value = map(int, input().split())
        tree[node] = value

    # 부모 노드 계산
    for i in range(N, 0, -1):  # N부터 1까지 역순으로 진행

        # tree[i] = tree[i*2] + tree[i*2+1]
        if i // 2 > 0: # 부모 노드가 유효할 때
            tree[i // 2] += tree[i]

    result = tree[L]

    print(f"#{tc} {result}")
"""