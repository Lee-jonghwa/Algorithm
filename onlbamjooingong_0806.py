N = int(input())
nums = list(map(int, input().split()))

cal = ['*', '+', '-']
found = False # 수식을 찾았는지 여부

def calculate(op, a, b): # 연산 값 저장
    if op == '*':
        return a * b
    elif op == '+':
        return a + b
    elif op == '-':
        return a - b


def pd101(N, idx, result_v, result_st):
    global found
    if found: # 찾았으면
        return # 정지

    if idx == N: # N 까지 다 돌았을 때
        if result_v % 101 == 0 and result_v != 0: #완료 되었으면
            print(result_st) # 지금까지 계산값 저장
            found = True # 찾았음 표시
        return

    for op in cal: # 연산에 대해서
        result_v2 = calculate(op, result_v, nums[idx])
        result_st2 = f"{result_st}{op}{nums[idx]}"
        pd101(N, idx + 1, result_v2, result_st2) # 모든 경우에 대해서


# 초기 호출
pd101(N, 1, nums[0], str(nums[0]))


'''
N = int(input())
nums = list(map(int, input().split()))

cal = ['*', '+', '-']
found = False

def calculate(op, a, b):
    if op == '*':
        return a * b
    elif op == '+':
        return a + b
    elif op == '-':
        return a - b


def pd101(N, idx, current_result, current_expression):
    global found
    if found:
        return

    if idx == N:
        if current_result % 101 == 0 and current_result != 0:
            print(current_expression)
            found = True
        return

    for op in cal:
        next_result = calculate(op, current_result, nums[idx])
        next_expression = f"{current_expression}{op}{nums[idx]}"
        pd101(N, idx + 1, next_result, next_expression)


# 초기 호출
pd101(N, 1, nums[0], str(nums[0]))
'''

'''
N = int(input())
nums = list(map(int, input().split()))
result = nums[0]
result_cal = f'{nums[0]}'
cal = ['*', '+', '-']

def pd101(N, nums):
    global result
    global result_cal
    if N == 0 and result % 101 == 0:
        return result_cal
    elif N == 0 and result % 101 != 0:
        result = 0
        result_cal = ''
    else:
        for i in cal:
            if i == '*':
                result *= pd101(N-1, nums[1:])
                result_cal += f"{nums[0]}*{pd101(N-1, nums[1:])}"
            if i == '+':
                result += pd101(N-1, nums[1:])
                result_cal += f"{nums[0]}+{pd101(N-1, nums[1:])}"
            if i == '-':
                result -= pd101(N-1, nums[1:])
                result_cal += f"{nums[0]}-{pd101(N-1, nums[1:])}"


print(pd101(N,nums))
'''