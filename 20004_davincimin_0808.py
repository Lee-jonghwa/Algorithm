'''
N, M = map(int, input().split()) # 패의 개수 N, 뽑아야하는 개수 M
a = list(input().split())
path = []

# 최솟값을 찾기 위한 설정
min_mul = float('inf')
min_path = []
used = [0 for _ in range(N)] # used 사용


# 곱이 최솟값이 되면 내 승리
mul_v = 1
def davinci(x):
    global mul_v, min_mul, min_path
    if x == M:
        for i in range(M):
            mul_v *= int(path[i])
        if mul_v < min_mul:
            min_path = path
            min_mul = mul_v
        mul_v = 1
        min_path = []
        return

    for i in range(7):
        if used[i] == True:
            continue
        used[i] = 1
        path.append(a[i])
        min_path.append(a[i])
        davinci(x+1)
        path.pop()
        used[i] = False

davinci(0)
print(min_path)
'''


'''
# 입력 받기
N, M = map(int, input().split())  # 패의 개수 N, 뽑아야 하는 개수 M
a = list(map(int, input().split()))  # 패에 적혀있는 수들


# 최소값 초기 설정
min_mul = float('inf')
min_vs = []

path = []

# 조합을 생성하고 곱을 계산하는 재귀 함수
def davinci(i, x, nums):
    global min_mul, min_vs

    # M개의 패를 선택한 경우
    if x == M:
        mul_v = 1
        for num in nums:
            mul_v *= num
        if mul_v < min_mul:
            min_mul = mul_v
            min_vs = nums[:]
        return

    # 현재 패를 선택하는 경우
    davinci(i + 1, x + 1, nums + [a[i]])

    # 현재 패를 선택하지 않는 경우
    davinci(i + 1, x, nums)


davinci(0, 0, [])

# 결과 출력 (오름차순 정렬)
min_vs.sort()
print(*min_vs)

'''
'''
# 입력 받기
N, M = map(int, input().split())  # 패의 개수 N, 뽑아야 하는 개수 M
a = list(map(int, input().split()))  # 패에 적혀있는 수들

# 최소값 초기 설정
min_mul = float('inf')
min_comb = []


# 조합을 생성하고 곱을 계산하는 재귀 함수
def davinci(i, x, nums):
    global min_mul, min_comb

    # M개의 패를 선택한 경우
    if x == M:
        mul_v = 1
        for num in nums:
            mul_v *= num
        if mul_v < min_mul:
            min_mul = mul_v
            min_comb = nums[:]
        return

    # 패의 개수를 넘어서는 경우
    if i >= N:
        return



# 초기 호출
davinci(0, 0, [])

# 결과 출력 (오름차순 정렬)
min_comb.sort()
print(*min_comb)

'''

# 입력 받기
N, M = map(int, input().split())  # 패의 개수 N, 뽑아야 하는 개수 M
a = list(map(int, input().split()))  # 패에 적혀있는 수들

min_mul = float('inf')  # 최소 곱을 저장할 변수
min_comb = []  # 최소 곱을 가진 조합을 저장할 리스트
stack = []  # 스택을 이용한 조합 생성

def find_min_comb(index):
    global min_mul, min_comb

    # M개의 패를 선택한 경우
    if len(stack) == M:
        current_mul = 1
        for num in stack:
            current_mul *= num
        if current_mul < min_mul:
            min_mul = current_mul
            min_comb = stack[:]
        return

    # 모든 패를 다 사용한 경우 종료
    if index >= N:
        return

    # 현재 패를 스택에 추가하는 경우
    stack.append(a[index])
    find_min_comb(index + 1)
    stack.pop()  # 백트래킹

    # 현재 패를 스택에 추가하지 않는 경우
    find_min_comb(index + 1)

# 초기 호출
find_min_comb(0)

# 결과 출력 (오름차순 정렬)
min_comb.sort()
print(*min_comb)

