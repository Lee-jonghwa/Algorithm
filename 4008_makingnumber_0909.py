import sys
sys.stdin = open('4008_input.txt', 'r')

def cal_v(nums,now_opers):
    result_v = nums[0]
    for i in range(N-1):
        if now_opers[i] == 0:
           result_v += nums[i+1]
        if now_opers[i] == 1:
           result_v -= nums[i+1]
        if now_opers[i] == 2:
           result_v *= nums[i+1]
        # 나눗셈
        if now_opers[i] == 3:
            if result_v < 0: # 음수처리
                result_v = -(abs(result_v) // nums[i+1])
            else:
                result_v //= nums[i+1]

    return result_v

def dfs(lev,now_opers):
    global min_v, max_v

    if lev == N-1:
        result_v = cal_v(nums,now_opers)
        min_v = min(result_v, min_v)
        max_v = max(result_v, max_v)
        return

    for i in range(4): # 연산자 개수만큼 확인
        if opers[i] == 0: continue # 연산자 없으면 넘어감

        opers[i] -= 1
        now_opers.append(i)
        dfs(lev + 1,now_opers)
        opers[i] += 1
        now_opers.pop()


T = int(input())
for tc in range(1, T+1):
    N = int(input())

    # opers 개수는 N-1개
    "+ - * /"
    opers = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    now_opers = []

    # dfs로 하면서 최대 최소 구하기
    min_v = 1e10
    max_v = -1e10

    dfs(0, now_opers)

    print(f'#{tc} {max_v - min_v}')

