'''
arr2 = [[0] * 3 for _ in range(2)]


for i in range(2):
  print(arr2[i]) # 행 전체 호출

print(arr2[1])


for i in range(2): # 각 행렬에 대한 값으로 보여줌
    for j in range(3):
        print(arr2[i][j], end=' ')
    print()
'''
'''
arr = [[1, 2, 3],[4, 5, 6]]
print(len(arr)) # 행 개수
print(len(arr[0])) # 열 개수

arr = [[0]*3]*2
print(arr)

arr[0][0] = 1
print(arr)
'''

'''
arr2 = [[0] * 3 for _ in range(2)]

# 행 우선 순회
for i in range(2):
    for j in range(3):
        print(arr2[i][j], end=' ')
    print()


# 열 우선 순회
for j in range(3):
    for i in range(2):
        print(arr2[i][j], end=' ')
    print()


# 모든 요소의 합
s = 0
for i in range(2):
    for j in range(3):
        s += arr2[i][j]
print(s)


# 행의 합 중 최댓값?
max_v = float('-inf') # 문제에 맞는 적절한 작은 값, -inf는 너무 큰 느낌
for i in range(2):
    s = 0 # s값 초기화
    for j in range(3):
        s += arr2[i][j]
        if max_v > s:
            max_v = s
print(max_v)
'''

'''
arr2 = [[1,2,3],[4,5,6]]

# 지그재그 순회

for i in range(2):
    if i % 2 == 0:
        for j in range(3):
            print(arr2[i][j])
    else:
        for j in range(2,-1,-1):
            print(arr2[i][j])


for i in range(2):
    for j in range(3):
        print(arr2[i][j + (3-1-2*j)*(i%2)]) #i가 짝수 -> 0/ 홀수 -> 1
'''

'''
arr = [[1,2,3],[4,5,6],[7,8,9]] # 3*3행렬

for i in range(3) :
    for j in range(3) :
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

print(arr)
'''


# 연습문제 1-1
'''
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

di = [-1, -1, 1, 1]
dj = [1, -1, -1, 1]

for i in range(5):

# 연습문제 1-2
N = int(input()) # 행과 열에 대해 주는 값 확실히 이해하기
arr = [list(map(int, input().split())) for _ in range(N)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

total = 0
for i in range(N):
    for j in range(N): # N*N의 배열의 모든 원소에 대해
        s = 0           # 원소와 주변 인접 원소의 차의 절댓값의 합
        for k in range(4): # i, j 원소의 네 방향 원소에 대해
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N: # 실존 여부 유효성 검사
                s += abs(arr[i][j] - arr[ni][nj]) # 실존하는 인접원소
        total += s # 총합에 반영
print(total)
'''

# 부분집합 합(subset sum) 문제
# 원소가 하나 - 둘 - 세 개의 개수를 순회하며 접근
# 부분집합 갯수 -> 2**N



# 부분집합 생성하기

bit = [0, 0, 0, 0]
for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
                # print_subset(bit)



arr = [3, 6, 7, 1, 5, 4]
n = len(arr) #  n : 원소의 개수

for i in range(1 << n): # 1 << n : 부분집하븨 개수
    for j in range(n): # 원소의 수만큼 비트 비교
        if i & (1 << j): # i의 j번 비트가 1인 경우
            print(arr[j], end=",") # j번 원소 출력
    print()
print()



# 비트 연산자