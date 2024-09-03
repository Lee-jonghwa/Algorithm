
"""
arr = ['O', 'X']
path = []
name = ['MIN', 'CO', 'TIM']

def print_name():
    print('{ ', end= "")
    for i in range(3):
        if path[i] == 'O':
            print(name[i], end=" ")
    print('}')

def run(lev):
    if lev == 3:
        print_name()
        return

    for i in range(2):
        path.append(arr[i])
        run(lev+1)
        path.pop()

run(0)
"""

"""
arr = ['A', 'B', 'C']
n = len(arr)

def get_sub(tar):
    for i in range(n):
        # 마지막 한 자리가 1인지를 확인하는 비트 연산
        if tar & 0x1:
            print(arr[i], end='')
        # 검사한 자리를 제거
        tar >>= 1

for tar in range(0, 1<<n): # 1부터 2^n까지 ==> 모든 부분집합 경우에 대해
    print("{", end="")
    get_sub(tar)
    print('}')
"""

"""
friends = ['A','B','C','D','E']

# 최소 두 명
n = len(friends)
path = []

def get_count(tar):
    global path
    cnt = 0
    path = []

    for i in range(n):
        # 한 명이 포함되어 있는지 확인
        if tar & 0x1:
            cnt += 1
            path.append(friends[i])
        tar >>= 1

    return cnt

result = 0
for tar in range(0,1 << n):
    if get_count(tar) >= 2:
        result +=1
        print(path)
print(result)
"""


"""
# 조합 코드
# 5명 중 3명이 되었을 때
arr = ['A','B','C','D','E']
path = []

n = 3
def run(lev, start):
    if lev == n:
        print(path)
        return

    for i in range(start, len(arr)):
        path.append(arr[i])
        run(lev+1, i + 1)
        path.pop()

run(0,0)
"""


"""
# 주사위 N개일 때 조합

N = int(input())
path = []

def dice(lev, start):
    if lev == 3:
        print(path)
        return

    for i in range(start, 7):
        path.append(i)
        dice(lev+1, i)
        path.pop()

dice(0,1)
"""

"""
# 동전 교환 문제

total = 1730
coins = [10, 50, 100, 500]
coins.sort(reverse=True) # 큰 수부터 시작

# 최소 동전 개수
cnt = 0
for coin in coins:
    # 사용 가능한 동전의 수 (만약 500원이라면 3개 가능)
    possible_cnt = total // coin

    cnt += possible_cnt
    total -= possible_cnt * coin

print(cnt)
"""
"""

# 동전 교환 문제 2

total = 530
coins = [5, 20, 100]
coins.sort(reverse=True)

cnt = 0

for coin in coins:
    possible_cnt = total // coin

    cnt += possible_cnt
    total -= possible_cnt * coin

print(cnt)
"""
"""
# 완전 탐색 접근


total = 530
coins = [5, 20, 100]

min_lev = 100
path = []

def give_change(lev, sum_v):
    global min_lev

    if lev > min_lev:
        return

    if sum_v == total:
        if min_lev > lev:
            min_lev = lev
            return 

    for coin in coins:
        path.append(coin)
        give_change(lev + 1, sum_v + coin)
        path.append(coin)


give_change(0,0)

print(min_lev)
"""


"""
total = 100
coins = [10, 50, 70]

min_lev = 100
path = []

def give_change(lev, sum_v):
    global min_lev

    if lev > min_lev:
        return

    if sum_v == total:
        if min_lev > lev:
            min_lev = lev
            return

    for coin in coins:
        path.append(coin)
        give_change(lev + 1, sum_v + coin)
        path.append(coin)


give_change(0,0)

print(min_lev)
"""
"""
# 화장실 문제

times = [15, 30, 50, 10]
times.sort() # 오름차순으로 준비

min_v = 0 # 최소합

# 가장 짧은 사람부터 하기
for i in range(len(times)):
    min_v += times[i] * (len(times)-(i+1))

print(min_v)

"""


"""

# Knapsack

# 하지만 무게가 30으로 제한, 개수가 물건당 1개밖에 없음


# Fractional Knapsack 문제

total = 30

# 물건의 종류 개수 N, 물건 별 무게 W, 가격 P, 각 물건은 1개밖에 못 가져감
# 최대 30KG의 짐

# 가장 효율이 좋은 -> 무게별 가격이 높은 것이 있는 게 좋음
N = 3
P = [50, 60, 140]
W = [5, 10, 20]

things = []
for i in range(N):
    things.append((W[i], P[i]))

things.sort(key = lambda x : (x[1] / x[0]), reverse=True)

max_v = 0
for kg, price in things:
    per_price = price / kg

    # 가방에 남은 용량이 얼마 안 되면,
    # 물건을 자른다
    if total < kg:
        max_v += total * per_price
        break

    max_v += price
    total -= kg

print(int(max_v))
"""


'''
input

11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14
'''