import sys
sys.stdin = open('18565_input.txt','r')

# 풍선이 터지면, 좌우로 이웃한 풍선에 적힌 두 숫자들의 곱으로 점수를 얻는다.
# 좌우로 한쪽만 이웃하는 풍선이 있는 경우, 이웃한 풍선에 적힌 숫자 만큼 점수를 얻는다.
# 좌우로 이웃하는 풍선이 없는 경우, 터진 풍선에 적힌 숫자 만큼 점수를 얻는다.
# 어떤 풍선도 터트리지 못한 경우, 점수를 얻지 못한다.
# 최대 점수

def shoot(remains, score):
    global max_v


    # 남은 풍선 1개면
    if len(remains) == 1:
        score += remains[0]
        max_v = max(score, max_v)
        return

    # 남은 풍선들이 후보
    for i in range(len(remains)):
        # 쐈을 때 마다 경우
        if i == 0: # 처음일 때
            now_score = remains[i+1]
        elif i == len(remains) - 1: # 끝일 때
            now_score = remains[i-1]
        else: # 사이일 때
            now_score = remains[i-1] * remains[i+1]

        # 해당 자리 터뜨림
        pos = remains.pop(i)
        # 다음 회차 진행
        shoot(remains, score + now_score)
        # 백트래킹 ->  다시 넣음
        remains.insert(i, pos)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    balloons = list(map(int,input().split()))

    max_v = 0

    # 완탐
    shoot(balloons, 0)

    print(f'#{tc} {max_v}')



"""
def balloon_bam(balloons, score):  # DFS
    global max_score

    # 종료조건: 남은 풍선 하나일 때
    if len(balloons) == 1:
        score += balloons[0]
        # 최대 점수 갱신
        if max_score < score:
            max_score = score
        return

    # 풍선 터뜨릴 때 점수 구하기
    for i in range(len(balloons)):

        # 풍선을 터뜨리기 전에 점수 계산
        if i == 0:  # 시작점일때
            now_score = balloons[i+1]
        elif i == len(balloons) - 1:  # 끝점일때
            now_score = balloons[i-1]
        else:  # 사이일 때
            now_score = balloons[i-1] * balloons[i+1]

        # 해당자리 터뜨림
        pos = balloons.pop(i)

        # 터뜨린 풍선들로 재귀호출
        balloon_bam(balloons, score+now_score)

        # 백트래킹
        balloons.insert(i, pos)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    balloons = list(map(int,input().split()))
    max_score = 0
    balloon_bam(balloons,0)
    print(f'#{tc} {max_score}')
"""