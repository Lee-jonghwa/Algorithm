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

davinci(0, 0, [])

# 결과 출력 (오름차순 정렬)
min_vs.sort()
print(*min_vs)
