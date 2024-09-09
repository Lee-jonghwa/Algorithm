import sys
sys.stdin = open('12741_input.txt','r')


T = int(input())
result = []

for tc in range(1, T+1):
    A, B, C, D = map(int, input().split())

    start = max(A, C)
    end = min(B, D)

    time = end - start
    if time < 0:
        time = 0

    result.append(time)

for idx, result in enumerate(result):
    print(f'#{idx+1} {result}')

# 두 개의 전구 X와 Y가 있다.
# 0초에서부터 시작하여 100초간 두 전구가 언제 켜지는지를 관찰

# 전구 X는 A초에서부터 B초까지에만 켜져 있었다.
# 전구 Y는 C초에서부터 D초까지에만 켜져 있었다.
# 100초 중 두 전구가 동시에 켜져 있던 시간은 몇 초일까?


""" 
# 아래처럼 진행 시 시간 초과 발생
# for문 안에서 i/o 번갈아서 발생하기 때문
T = int(input())
result_lst = [] # 결과 저장

for tc in range(1, T+1):
    A, B, C, D = map(int, input().split())

    # 나중에 켜진 전구 시간이 시작점
    start = max(A, C)
    # 먼저 꺼진 전구 시간이 끝점
    end = min(B, D)

    result = end - start
    if result <= 0:
        result = 0 # 음수는 X


    result_lst.append(result)


for index, result in enumerate(result_lst):
    print(f'#{index + 1} {result}')

# 출력이 많으면 --> 몰아서 하자!!
"""