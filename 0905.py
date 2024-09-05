
nums = [1,2,3,4,5,6,7,8,9,10]
N = len(nums)


"""
# 재귀로 풀기(dfs)
path = []
visited = [0] * (N+1)

def powerset(lev, sum_v, now):
    if sum_v == 10:
        print(path)
        return

    if sum_v > 10:
        return

    for i in range(now, 10):
        if visited[i] == 1: continue
        visited[i] = 1
        path.append(nums[i])
        powerset(lev+1, sum_v + nums[i], i)
        path.pop()
        visited[i] = 0

powerset(0,0,0)

print('-' * 30)
"""
"""
# 트리구조로 풀기(dfs)
path2 = []
visited2 = [0] * (N+1)

def powerset2(lev, sum_v):
    if sum_v == 10:
        print(path2)
        return

    if sum_v > 10:
        return

    if lev == N:
        return


    # 현재 숫자를 선택하는 경우
    visited2[lev] = 1
    path2.append(nums[lev])
    powerset2(lev+1, sum_v + nums[lev])
    path2.pop()
    visited2[lev] = 0

    # 재귀 후 현재 숫자를 선택하지 않는 경우
    powerset2(lev + 1, sum_v)

powerset2(0,0)
"""