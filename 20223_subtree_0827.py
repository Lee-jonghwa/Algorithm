def subtree(N):
    global cnt

    # for를 해야 꼭 다음 것까지 도니까 for 꼭 필요!
    for i in range(2): # 양쪽을 보면서
        if tree[i][N]: # 값이 있으면
            cnt +=1
            subtree(tree[i][N])


T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split()) # E: 간선의 개수, N: subtree를 구하는 root node
    arr = list(map(int, input().split()))

    # 트리 초기화 (총 원소 개수는 E+1, 인덱스 맞춤
    # 1행은 왼쪽, 2행은 오른쪽
    tree = [[0] * (E + 2) for _ in range(2)]

    for i in range(0, len(arr), 2):
        p = arr[i]
        c = arr[i+1]

        if tree[0][p] == 0:
            tree[0][p] = c

        else:
            tree[1][p] = c

    cnt = 1 # 시작 노드는 항상 해당 됨

    subtree(N)
    print(f'#{tc} {cnt}')





"""
# subtree 구하기
def subtree(N):
    global cnt
    for i in range(2):  # 양쪽을 순회하면서
        if tree[i][N]: # 자식이 있으면
            cnt += 1 # 같은 레벨이라도 상관 없음
            n = tree[i][N] # 자식 노드로 이동
            subtree(n)


T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    temp = list(map(int,input().split()))
    # tree 초기화, 노드 번호가 1 ~ E+1까지 있음
    tree = [[0] * (E+2) for _ in range(2)]
    # 자기 자신도 count
    cnt = 1

    # tree 완성
    for i in range(E): # 5 번 부여됨
        # 부모 - 자식 순서
        p, c = temp[i*2], temp[i*2+1]
        # tree의 p번째 자리의 왼쪽 노드
        if tree[0][p] == 0:  # 왼쪽 노드에 아무것도 없으면
            tree[0][p] = c  # 값 넣기
        else:
            tree[1][p] = c

    subtree(N)
    print(f'#{tc} {cnt}')

"""
"""
# subtree

def sub_tree(node):
    global cnt
    for i in range(2): # 왼쪽자식, 오른쪽자식
        if tree[i][node]: # 해당 노드의 자식이 있다면
            cnt += 1
            n = tree[i][node] # 자식 노드
            sub_tree(n) # 자식 노드에 대해 재귀 호출

T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())
    temp = input().split()
    # 노드번호가 1번부터 E+1번까지 있어서, 2 ---> 왼쪽, 오른쪽
    tree = [[0 for _ in range(E + 2)] for _ in range(2)]
    # tree[0][node] ---> 왼쪽 자식
    # tree[1][node] ---> 오른쪽 자식
    for i in range(E):
        p_node = int(temp[2 * i]) # 짝수 번째 ---> 부모 노드 번호
        c_node = int(temp[2 * i + 1]) # 홀수 번째 ---> 자식 노드 번호
        if tree[0][p_node] == 0: # 왼쪽에 자식이 없으면 왼쪽에 할당, 왼쪽에 자식 있으면 오른쪽에 할당
            tree[0][p_node] = c_node
        else:
            tree[1][p_node] = c_node

    cnt = 1
    sub_tree(N)
    print(f'#{tc} {cnt}')
"""
"""
def binarytree(node):
    global cnt
    cnt += 1
    if node == 0:
        return

    binarytree(left[node])
    binarytree(right[node])

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split()) # E: 간선의 수,  N: 시작 루트
    arr = list(map(int, input().split()))

    # 노드의 수 E + 1
    left = [0] * (E + 2)
    right = [0] * (E + 2)

    for i in range(0, len(arr), 2): # 전체를 순회하며
        parent, child = arr[i], arr[i+1]

        # 왼쪽 자식이 없다면, 왼쪽에 우선 삽입
        if left[parent] == 0:
            left[parent] = child

        else: # 오른쪽 자식이 없다면
            right[parent] = child

    cnt = 0
    # print(left)
    # print(right)
    #
    binarytree(N)
    print(f'#{tc} {cnt//2}')

"""