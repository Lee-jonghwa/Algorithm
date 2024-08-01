DATA = [0, 4, 1, 3, 1, 2, 4, 1]
COUNTS = [0] * 5                # DATA가 0~4까지의 정수

N = len(DATA)                   # DATA의 크기
TEMP = [0] * N                  # 정렬 결과 저장

# 1단계 : DATA 원소 별 개수 세기
# DATA의 원소 x를 가져와서 COUNTS[x]에 개수 기록
for x in DATA:
    COUNTS[x] += 1

# 2단계 : 각 숫자까지의 누적 개수 구하기
for i in range(1, 5):           # COUNTS[1] ~ COUNTS[4]까지의 누적 개수
    COUNTS[i] = COUNTS[i-1] + COUNTS[i]

# 3단계 : DATA의 맨 뒤부터 앞으로 순회하여 TEMP에 정렬
for i in range(N-1, -1, -1):    # n-1 ~ 0까지
    COUNTS[DATA[i]] -= 1 # COUNTS에서 i의 누적 개수 하나 감소
    TEMP[COUNTS[DATA[i]]] = DATA[i]

print(*TEMP) # 언패킹 하여 결과 확인
