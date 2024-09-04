# 풍선이 터지면, 좌우로 이웃한 풍선에 적힌 두 숫자들의 곱으로 점수를 얻는다.
# 좌우로 한쪽만 이웃하는 풍선이 있는 경우, 이웃한 풍선에 적힌 숫자 만큼 점수를 얻는다.
# 좌우로 이웃하는 풍선이 없는 경우, 터진 풍선에 적힌 숫자 만큼 점수를 얻는다.
# 어떤 풍선도 터트리지 못한 경우, 점수를 얻지 못한다.
# 최대 점수
def balloon_bam(balloons,score):
    global max_score

    # 종료조건: 남은 풍선 하나일 때
    if len(balloons) == 1:
        score += balloons[0]
        # 최대 점수 갱신
        if max_score < score:
            max_score = score
            return

    for i in range(len(balloons)):
        if i == 0:
            now_score = balloons[i+1]
        elif i == len(balloons) - 1:
            now_score = balloons[i-1]
        else:
            now_score = balloons[i-1] * balloons[i+1]
        # 해당자리 터뜨림
        pos = balloons.pop(i)
        balloon_bam(balloons, score+now_score)
        balloons.insert(i, pos)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    balloons = list(map(int,input().split()))
    path = []
    # 풍선 값에 맞게 배열 초기화
    visited = [0] * max(balloons)
    max_score = 0
    balloon_bam(balloons,0)
    print(f'#{tc} {max_score}')