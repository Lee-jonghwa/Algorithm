
# 4가지 상태 -> 1, 2, 3, 4 (겹치는 영역, 겹치는 선, 겹치는 점, 안 겹침)

def ggokjijum(x1, y1, x2, y2, x3, y3, x4, y4):
    # 큰게 작은 것보다 작거나, 작은게 큰 것 보다 클 때
    if x2 < x3 or x4 < x1 or y2 < y3 or y4 < y1: # 오른쪽, 왼쪽, 위쪽, 아래쪽
        return 4
    # x 중 하나, y 중 하나 맞을 때
    elif (x2 == x3 or x4 == x1) and (y2 == y3 or y4 == y1): # x가 하나씩 맞고, y가 하나씩 맞을 때
        return 3
    #  전체에서 하나만 맞아도 종료
    elif (x2 == x3 or x4 == x1) or (y2 == y3 or y4 == y1): # 네 꼭짓점중에 하나씩 맞을때
        return 2
    else: # 겹침
        return 1

T = int(input())
for tc in range(1, T + 1):
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())
    result = ggokjijum(x1, y1, x2, y2, x3, y3, x4, y4)
    print(f'#{tc} {result}')



"""



def ggokjijum(x1, y1, x2, y2, x3, y3, x4, y4):
    if x2 < x3 or x4 < x1 or y2 < y3 or y4 < y1: # 오른쪽, 왼쪽, 위쪽, 아래쪽
        return 4
    elif (x2 == x3 or x4 == x1) and (y2 == y3 or y4 == y1): # 네 꼭짓점중에 하나씩 맞을때
        return 3
    elif (x2 == x3 or x4 == x1) or (y2 == y3 or y4 == y1): # x가 하나씩 맞고, y가 하나씩 맞을 때
        return 2
    else: # 겹침
        return 1

T = int(input())
for tc in range(1, T + 1):
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())
    result = ggokjijum(x1, y1, x2, y2, x3, y3, x4, y4)
    print(f'#{tc} {result}')
"""



'''
T = int(input())
for tc in range(1, T+1):
    st_x1, st_y1, st_x2, st_y2 = map(int, input().split())
    nd_x1, nd_y1, nd_x2, nd_y2 = map(int, input().split())
    directions = st_x1, st_y1
    cmn = [] #시작점 끝점 구하기
    for y in range(st_y2 - st_y1 + 1):
        for x in range(st_x2 - st_x1 + 1): #하나의 범위에 대해서
            for y2 in range(nd_y2 - nd_y1 + 1): # 시작점 구하기
                for x2 in range(nd_x2 - nd_x1 + 1):
                    if y == y2 and x == x2:
                        cmn.append((y, x))# 겹치는 좌표 구함

                        break
            for y2 in range(nd_y2 - nd_y1, -1, -1):  # 끝점 구하기
                for x2 in range(nd_x2 - nd_x1, -1, -1):
                    if y == y2 and x == x2:
                        cmn.append((y, x))
                        break
    # result =[]
    # result.append(cmn[0])
    # result.append(cmn[-1])
    print(cmn)

# 점 네 개를 구해서 directions로 만들기 --> directions 순회하면서 각 점이 한 선을 넘어서면서, 한 선 안에 있으면 -> 면 경우
'''