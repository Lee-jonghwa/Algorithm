'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''


def preorder(node):
    if node == 0:  # 0인 값은 넘김
        return

    print(node, end=" ") # 본인을 먼저 확인
    preorder(left[node])
    # print(node, end=" ")  # 왼쪽을 보고나서 본인을 확인
    preorder(right[node])
    # print(node, end=" ")  # 왼쪽 오른쪽을 보고 나서 본인을 확인


N = int(input()) # 정점의 개수(정점 : 1~ N번)
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


