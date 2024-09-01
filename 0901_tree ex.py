"""
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
"""
# 부모 - 자식 순


# 전위 순회 함수
def preorder(node):
    if node == 0:  # 트리에 해당하는 값이 아니면
        return  # 넘김

    # 순서 가운데 - 왼쪽 - 오른쪽
    print(node, end=" ")  # 현재 위치 print
    preorder(left[node])
    preorder(right[node])


V = int(input())  # 노드 개수
E = list(map(int, input().split())) # 간선 수

left = [0] * (V + 1) # 노드 전체 담음, 인덱스 맞추기
right = [0] * (V + 1) # 노드 전체 담음, 인덱스 맞추기


for i in range(0, len(E), 2): # 주어진 길이에서 step을 2만큼 이동
    par = E[i]  # 부모
    chi = E[i+1]  # 자식

    # 트리 채우기(왼쪽부터)
    if left[par] == 0: # 왼쪽에 값이 없으면
        left[par] = chi

    else: # 이미 차있으면
        right[par] = chi

root = 1
preorder(1)