
# 연속으로 정답을 맞출 경우, 이 전 점수에서 보너스 1점이 가산
# 가장 높은 점수를 받은 학생과, 가장 낮은 점수를 받은 학생의 점수차
# 다음 각 줄에 공백으로 구분되어 주어진다

def std_ev(M, answers, std_answers):

    min_v = float('inf')
    max_v = 0

    for std_answer in std_answers: # 각 학생이 제출한 문제지를 순회하며
        sum_v = 0  # 총점
        cnt = 0  # 가산점
        for i in range(M): # 각 문제 채점
            if std_answer[i] == answers[i]: # 정답 맞으면
                cnt += 1  # 가산점 1 추가
                sum_v += cnt
            else: # 틀리면
                cnt = 0 # 가산점 초기화
        if min_v > sum_v:
            min_v = sum_v
        elif max_v < sum_v:
            max_v = sum_v

    return max_v - min_v


T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split()) # 학생의 수 N, 문제의 수 M
    # M개의 문제 정답
    answers = list(map(int, input().split()))
    #  N줄에 걸쳐, N명의 학생이 제출한 M개의 문제에 대한 답안지의 wjdqh
    std_answers = [list(map(int, input().split())) for _ in range(N)]

    result = std_ev(M, answers, std_answers)
    print(f'#{tc} {result}')



"""

T = int(input())
for tc in range(1, T+1):
    NM = list(map(int, input().split()))
    N = NM[0]
    M = NM[1]
    answer_arr = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = float('-inf')
    min_v = float('inf')
    for n in range(N):
        cnt = 1
        score = 0
        for m in range(M):
            if answer_arr[m] == arr[n][m]:
                score += cnt
                cnt += 1
            else:
                cnt = 1

        max_v = max(max_v, score)
        min_v = min(min_v, score)

    result = max_v - min_v
    print(f'#{tc} {result}')
"""


"""

def answer_ev(N, M, ans, arr):
    max_v = 0
    min_v = 100
    for i in range(N):
        cnt = 0
        for j in range(M):
            if arr[i][j] == ans[j]:
                cnt += 1  # 맟출 때 점수 부여
                # 연속할 때 가산 점
                for k in range(1, j):
                    if arr[i][j-k] == ans[j-k]:
                        cnt += 1
                    else:
                        break
        max_v = max(cnt, max_v)
        min_v = min(cnt, min_v)
    return max_v - min_v



T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    ans = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for i in range(N)]
    result = answer_ev(N, M, ans, arr)
    print(f'#{tc} {result}')

"""