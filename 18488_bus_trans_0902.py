from collections import deque  # deque를 사용하여 BFS를 구현하기 위해 deque 모듈을 임포트


def bfs(start_buses, end_buses, bus_graph):
    # 시작 지점에서 출발하는 버스들을 큐에 초기화하며, 환승 횟수를 1로 설정
    queue = deque([(bus, 1) for bus in start_buses])
    visited = set(start_buses)  # 방문한 버스를 기록하여 중복 방문을 방지

    while queue:
        current_bus, transfers = queue.popleft()  # 큐에서 현재 버스와 환승 횟수를 꺼냄

        if current_bus in end_buses:
            return transfers  # 목적지에 도달하는 버스를 찾으면 환승 횟수를 반환

        # 현재 버스에서 환승할 수 있는 다른 버스들을 탐색
        if current_bus in bus_graph:
            for next_bus in bus_graph[current_bus]:
                if next_bus not in visited:  # 방문하지 않은 버스만 탐색
                    visited.add(next_bus)  # 버스를 방문 처리
                    queue.append((next_bus, transfers + 1))  # 다음 버스를 큐에 추가하고 환승 횟수를 증가

    return -1  # 목적지에 도달할 수 없는 경우(이 문제에서는 발생하지 않음)


def is_overlap(bus1, bus2):
    # 두 버스 노선이 겹치는지 확인하는 함수
    if bus1['x1'] <= bus2['x2'] and bus1['x2'] >= bus2['x1'] and bus1['y1'] <= bus2['y2'] and bus1['y2'] >= bus2['y1']:
        return True  # 겹치면 True를 반환
    return False  # 겹치지 않으면 False를 반환


# 첫 줄 입력: 수직선의 수 m, 수평선의 수 n
m, n = map(int, input().split())

# 두 번째 줄 입력: 버스의 수 k
k = int(input())

# 각 버스의 정보를 저장할 리스트
buses = []
for _ in range(k):
    b, x1, y1, x2, y2 = map(int, input().split())
    # 버스의 시작점과 끝점을 저장하며, x1, x2, y1, y2는 범위로 정렬
    buses.append({'id': b, 'x1': min(x1, x2), 'y1': min(y1, y2), 'x2': max(x1, x2), 'y2': max(y1, y2)})

# 마지막 줄 입력: 출발지 (sx, sy)와 목적지 (dx, dy)
sx, sy, dx, dy = map(int, input().split())

start_buses = set()  # 출발지에서 탈 수 있는 버스를 저장하는 집합
end_buses = set()  # 목적지에 도달할 수 있는 버스를 저장하는 집합
bus_graph = {}  # 버스 간의 연결 정보를 저장하는 딕셔너리

# 모든 버스를 순회하며 시작 버스와 목적지 버스를 찾고, 버스 간 연결을 기록
for i in range(k):
    bus = buses[i]

    # 출발지 (sx, sy)를 포함하는 버스를 찾음
    if bus['x1'] <= sx <= bus['x2'] and bus['y1'] <= sy <= bus['y2']:
        start_buses.add(bus['id'])  # 출발지에서 탈 수 있는 버스 목록에 추가

    # 목적지 (dx, dy)를 포함하는 버스를 찾음
    if bus['x1'] <= dx <= bus['x2'] and bus['y1'] <= dy <= bus['y2']:
        end_buses.add(bus['id'])  # 목적지에 도달할 수 있는 버스 목록에 추가

    # 현재 버스와 다른 버스들의 경로가 겹치는지 확인하고, 겹치면 연결 정보를 기록
    for j in range(i + 1, k):
        other_bus = buses[j]
        if is_overlap(bus, other_bus):  # 경로가 겹치는지 확인
            # bus_graph 딕셔너리에 연결된 버스를 추가
            if bus['id'] not in bus_graph:
                bus_graph[bus['id']] = []  # 키가 없으면 리스트로 초기화
            if other_bus['id'] not in bus_graph:
                bus_graph[other_bus['id']] = []  # 키가 없으면 리스트로 초기화
            bus_graph[bus['id']].append(other_bus['id'])  # 양방향 연결
            bus_graph[other_bus['id']].append(bus['id'])  # 양방향 연결

# BFS를 사용하여 출발지에서 목적지까지의 최소 환승 횟수를 계산
result = bfs(start_buses, end_buses, bus_graph)
print(result)  # 결과 출력
