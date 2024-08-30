def BST(n):
    global node # 재귀가 필요하므로 global
    if n <= N:  # n이 전체 노드의 N보다 작을때만 수행
        BST(n*2) # 왼쪽
        tree[n] = node  # 해당 자리에 node 넣음
        node += 1
        BST(n*2+1) # 오른쪽

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 기본 인덱스
    tree = [0 for i in range(N+1)]
    node = 1 # 시작 노드 1, 1 ~ N까지의 수 넣음
    BST(1)
    print(f'#{tc} {tree[1]} {tree[N//2]}')


"""

# 왼쪽 자식의 인덱스 : n * 2
# 오른쪽 자식의 인덱스 : n * 2 + 1

def BST(n):
    global node
    if n <= N: # n 이 전체 노드의 수 N보다 작을 때만
        BST(n*2) # 왼쪽 자식으로 이동
        tree[n] = node
        node += 1
        BST(n*2+1) # 오른쪽 자식으로 이동


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0 for i in range(N+1)]
    node = 1
    BST(1)
    print(f'#{tc} {tree[1]} {tree[N//2]}')
"""


"""
# 이진 탐색 트리는 어떤 경우에도 저장된 값이
# 왼쪽 서브트리의 루트 <현재 노드 <오른쪽 서브 트리의 루트인 규칙을 만족한다.

# idx는 현재 노드의 인덱스이고, n은 총 노드 수

def inorder(tree, arr, idx, N):
    if idx <= N:
        inorder(tree, arr, 2 * idx, N)  # Left child
        tree[idx] = arr.pop(0)  # 현재 위치
        inorder(tree, arr, 2 * idx + 1, N)  # Right child


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(range(1, N + 1))  # 1부터 N까지의 숫자 리스트
    tree = [0] * (N + 1)  # 기본 트리 만들기
    inorder(tree, arr, 1, N)

    root_value = tree[1]
    middle_value = tree[N // 2]

    print(f"#{tc} {root_value} {middle_value}")
"""

"""
def inorder(node):
    if node == 0:  # 0인 값은 넘김
        return


    inorder(left[node])
    # print(node, end=" ")  # 왼쪽을 보고나서 본인을 확인
    print(node, end=" ") # 본인을 먼저 확인
    inorder(right[node])
    # print(node, end=" ")  # 왼쪽 오른쪽을 보고 나서 본인을 확인

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 왼쪽 자식 번호를 저장할 리스트
    left = [0] * (N + 1) # 인덱스 맞추기
    # 예 left[3] =2 ==> 3번 부모의 왼쪽 자식은 2다
    # 왼쪽 자식 번호를 저장할 리스트
    right = [0] * (N + 1)

    for i in range(0, len(arr), 2):
        parent, child = arr[i], arr[i+1]

        # 왼쪽 자식이 없다면, 왼쪽에 삽입
        if left[parent] == 0:
            left[parent] = child

        else:
            right[parent] = child

    root = 1 # 시작점을 1이라는 가정
    preoreder(root)
"""