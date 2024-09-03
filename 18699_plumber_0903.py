# 물이 새는 곳은 신기하게도 가장 왼쪽에서 정수만큼 떨어진 거리만 물이 샌다.
# 길이가 L인 테이프를 무한 개 가지고 있고, 이 테이프를 이용해서 물이 새는 것을 막으려고 한다.

# 테이프를 겹쳐서 붙이는 것은 가능하다. --> L이 거리를 넘어도 됨

N, L = map(int, input().split())
locations = list(map(int, input().split()))

# 가까운 곳부터 붙이는 것이 이득
locations.sort()

cnt = 0
i = 0

while i < N:
    # 현재 위치 붙이기
    cnt += 1
    end = locations[i] + L - 1 # 테이프 길이에 따른 종료
    # 배열 안에서 있으면서 테이프의 끝보다 먼저 있으면
    while i < N and locations[i] <= end:
        i += 1 # 뛰어 넘기

print(cnt)