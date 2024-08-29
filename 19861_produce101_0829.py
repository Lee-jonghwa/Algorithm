def calculate(idx, result, ex):
    # idx: 현재 처리중인 숫자의 인덱스, result: 현재까지 계산 결과, ex: 수식 문자열
    if idx == N - 1: # 모든 숫자를 다 사용했을 때(마지막 숫자까지 처리)
        if result == 0:
            return
        # 배수라면 현재 수식 출력 후 return
        elif result % 101 == 0:
            print(ex)
            return
        # 101 배수가 아닐 경우
        return
    # 곱하기 연산 수행 재귀
    calculate(idx+1, result * nums[idx + 1], ex + "*" + str(nums[idx+1]))
    # 더하기 연산 수행 재귀
    calculate(idx+1, result + nums[idx + 1], ex + "+" + str(nums[idx+1]))
    # 빼기 연산 수행 재귀
    calculate(idx+1, result - nums[idx + 1], ex + "-" + str(nums[idx+1]))

N = int(input())
nums = list(map(int, input().split()))
calculate(0, nums[0], str(nums[0]))