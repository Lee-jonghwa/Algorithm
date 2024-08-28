'''
7
3 5 1 2 7 4 -5
'''

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        # root 노드 자리
        self.root = None

    def insert(self, key):
        # root가 없다면
        if self.root is None:
            # 키 삽입
            self.root = Node(key)
        else: # root가 있다면
            # 자리 찾아서 가능
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key: # 새로운 노드가 작다면
            # 왼쪽에 삽입 가능하면
            if node.left is None:
                # 왼쪽에 삽입
                node.left = Node(key)
            else: # 삽입 불가(데이터가 있다면)
                # 한 번 더 내려감
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key): # key: target / node: 현재 바라보고 있는 노드
        if node is None or node.key == key:
            return node
        if key < node.key: # 작다면 왼쪽으로 가야하므로 node left
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    # 중위 순회
    def inorder_traversal(self):
        self._inorder_traversal(self.root)

    def _inorder_traversal(self, node):
        if node:
            self._inorder_traversal(node.left)
            print(node.key, end=' ')
            self._inorder_traversal(node.right)

N = int(input())
arr = list(map(int, input().split()))

bst = BinarySearchTree()

for num in arr:
    bst.insert(num)

print("중위 순회 결과:", end=' ')
bst.inorder_traversal()  # 중위 순회: -5 1 2 3 4 5 7

# 탐색 예제
key = 5
result = bst.search(key)
if result:
    print(f"\n키 {key} 찾음.")
else:
    print(f"\n키 {key} 못 찾음.")
