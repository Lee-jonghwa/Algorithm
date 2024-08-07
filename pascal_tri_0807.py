### DP풀이
def pascal(N):
    # dp 테이블 초기화
    dp = [[0 for _ in range(N)] for _ in range(N) ]
    # 첫 번째 열을 모두 1로 초기화
    for i in range(N):
        dp[i][0] =1
    # dp 테이블 채우기
    for i in range(1, N):
        for j in range(1, N):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    # 결과 출력
    for i in range(N):
        for j in range(i + 1):
            print(dp[i][j], end=" ")
        print()
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc}')
    pascal(N)




'''
### stack 풀이
def pascal(N):
    stack = [1] # 스택 첫 요소 1
    for row in range(N):
        print(*stack)

        new_stack = [1] # new stack의 첫 요소도 1
        while len(stack) > 1: #
            a = stack.pop() # stack에서 요소 꺼내기
            b = stack[-1] # 스택의 top 요소(꺼내진 않음) -> 한 번 더하면 다음에도 더해야 하기 때문
            new_stack.append(a + b)
        new_stack.append(1) # new스택의 마지막 요소도 1
        stack = new_stack

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc}')
    pascal(N)

'''

'''
def pascal(N):
    arr = [[] for _ in range(N)]
    for i in range(N): # 층 쌓기
        if i < 2: #1, 2층
            arr[i] = [1]*(i+1)
        else:
            arr[i].append(1)  # 각 행 첫 요소 1
            for j in range(1, i): # 총 시행횟수 층 번호-1 i - 1
                arr[i].append(arr[i-1][j-1] + arr[i-1][j]) # 전 행 + 1
            arr[i].append(1) # 각 행 마지막 요소 1
        print(*arr[i])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc}')
    pascal(N)
'''