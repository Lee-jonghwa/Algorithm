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