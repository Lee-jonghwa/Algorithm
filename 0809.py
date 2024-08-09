
'''# 부분집합

# 1. 완전탐색(중복순열)
# branch -> 2 (뽑거나 안 뽑거나), level -> n(집합의 원소와 갯수


# 2. binary counting
# n개의 원소를 뽑는 방법 -> 2**n
# 1 << n == 2 ** n

# 문제 : A, B, C로 만들 수 있는 부분집합을 바이너리 카운팅으로 풀기
arr = ['A', 'B', 'C']
n = len(arr)

def get_sub(tar): # tar: 출력하고자 하는 십진수(부분집합의 경우의 수)
    for i in range(n): #집합 원소 갯수만큼
        if tar & 0x1: # 0x1 --> 16진수, 고정(001)
            print(arr[i], end="")
        tar >>= 1 # target을 오른쪽으로 한 번씩 밀기, 검사를 마친 한 자리 제거

for tar in range(0, 1 << n):
    print('{', end="")
    get_sub(tar)
    print('}')

# 도전문제
arr = ['A','B','C','D','E']
n = len(arr)

# 총 몇 개의 bit가 1로 되어있는지 확인하는 함수
def get_sub(tar):
    cnt = 0
    for i in range(5):
        if tar & 0x1:
            cnt += 1
            # print(arr[i], end="")
        tar >>= 1 # 검사를 마친 후 자리 제거
    return cnt

result = 0
for tar in range(0, 1 <<n):
    if get_sub(tar) >=2 : #bit가 2개 이상 1일이라면
        result += 1
print(result)
'''

'''
## 조합

arr = ['A','B','C','D','E']

# level: n, branch: 최대 5개

for a in range(5):
    start1 = a+1
    for b in range(start1, 5):
        start2 = b + 1
        for c in range(start2, 5):
            print(arr[a], arr[b], arr[c])


# 다섯 명 중 n 명 뽑는다 -> branch = 5, level = n

path = []
n = 3
def run(lev, start):
    if lev == n:
        return

    for i in range(start, 5):
        path.append(arr[i])
        run(lev + 1, i + 1) # 중첩 for 문 느낌
        path.pop()

run(0,0)
'''

# 주사위 던지기
# 주사위 N 개를 던져서 나올 수 있는 모든 조합 출력
# level: n개, branch: 6


arr = [1, 2, 3, 4, 5, 6]
n = 3
path = []

def run(lev, start):
    if lev == n:
        print(path)
        return

    for i in range(start, 6):
        path.append(arr[i])
        run(lev+1, i)
        path.pop()

run(0, 0)

## arr 없는 버전
n = 3
path = []

def run(lev, start):
    if lev == n:
        print(path)
        return

    for i in range(start, 7):
        path.append(i)
        run(lev+1, i)
        path.pop()

run(0, 1)
