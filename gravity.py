'''
가로 N 세로 100 크기의 방에 상자들이 쌓여있다. 방이 오른쪽으로 90도 회전하여 상자들이 중력의 영향을 받아 낙하한다고 할 때,
가장 큰 낙차를 구하여라

[제약 사항]
중력은 회전이 완료된 후 적용된다.
상자들은 모두 한쪽 벽면에 붙여진 상태로 쌓여 2차원의 형태를 이루며 벽에서 떨어져서 쌓인 상자는 없다.
방의 세로 길이는 항상 100이다. 즉, 상자는 최소 0, 최대 100 높이로 쌓을 수 있다

[입력]
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 줄에는 방의 가로길이가 주어지고 그 다음 줄부터는 쌓여있는 상자의 수가 주어진다.

[출력]
#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스에 대한 답을 출력한다.

[그림설명]
총 26개의 상자가 회전 후, 오른쪽 방 그림의 상태가 된다. A 상자의 낙차가 7로 가장크므로 7을리턴하면 된다.
회전 결과, B상자의 낙차는6, C상자의 낙차는 1이다.
'''

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    val_lst = list(map(int, input().split()))
    max_diff = 0
    for i in range(N):
        fall_diff = 0
        for j in range(i, N):
            if val_lst[i] > val_lst[j]:
                fall_diff += 1
            if max_diff < fall_diff:
                max_diff = fall_diff
    print(f'{tc} {max_diff}')



def gravity(boxes):
    max_v = 0 # 최대 낙차 저장 변수 초기화
    for idx, box in enumerate(boxs): # 각 상자의 인덱스, 높이
        fall = 0 #현재 상자의 낙차 계산 변수 초기화
        for next in range(idx + 1, N): # 현재 상자의 뒤에 있는 상자들과 비교
            if box > boxes[next]: # 현재 상자의 높이가 다음 상자 보다 높으면
                fall += 1 # 낙차 1증가
        max_v = max(max_v, fall)
    return max_v

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    boxes = list(map(int, input().split()))
    result = gravity(boxes)
    print(f'{tc} {result}')