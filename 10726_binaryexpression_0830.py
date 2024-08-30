def bit(N, M):
    power_of = 1 << N
    if (M + 1) % power_of == 0:
        return "ON"
    else:
        return "OFF"

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    result = bit(N, M)
    print(f'#{tc} {result}')

"""
def bin_find(N, M):
    # 마지막 N개의 비트가 모두 1인지 확인하기 위해 마스크를 생성
    mask = (1 << N) - 1  # N 길이 만큼의 1 생성
    # M의 마지막 N개의 비트를 추출하여 마스크와 비교
    if (M & mask) == mask:
        return "ON"
    return "OFF"

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    result = bin_find(N, M)
    print(f'#{tc} {result}')

"""
"""

# right shift쓰기
def bin_find(N,M):
    cnt = 0
    for i in range(N): # N번만 시행
        if M & 1:
            cnt += 1
        M = M >> 1
    if cnt == N:
        return "ON"
    return "OFF"

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # M: 조사 대상 수, N: bit개수
    result = bin_find(N, M)
    print(f'#{tc} {result}')

"""


"""
def bin_find(N, M):
    find_v = str(bin(M))
    cnt = 0
    if 2 + N > len(find_v):
        return "OFF"
    for i in range(len(find_v)-1, len(find_v)-N-1,-1): # 끝부터 N자리 순회
        if find_v[i] == "1":
            cnt +=1
    if cnt == N:
        return "ON"
    return "OFF"


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # M: 조사 대상 수, N: bit개수
    result = bin_find(N, M)
    print(f'#{tc} {result}')
"""