# N개의 연꽃 잎 구역
# 연꽃에 도달하면 오른쪽으로 K칸 만큼 더 이동
# 연못에 빠지면, K번째 칸에 멈추게 된다고 한다.

# 개구리가 최대 몇 번째 칸까지 이동할 수 있는지
# 연꽃이 있으면 1, 없으면 0으로 표시된 N개의 연못 구역
# 이동하는 최대 칸 수 K

# 배열 접근
def frogjump(N,K,pond):
    idx = 0 # 개구리 위치
    while idx < N: # 배열을 벗어나면 정지, 첫째자리 포함
        idx += K # K만큼 뜀
        if idx >= N-1: # 배열을 벗어나면
            return N
        else: # 벗어나지 않으면
            for i in range(idx, idx-K, -1): # K부터 지금 다음 칸까지
                if pond[i] == 1: # 연꽃 있으면
                    idx = i
                    break
            else: # 연꽃 없으면
                return idx + 1 # 가장 많이 뛴 자리
    return -1  # 디버그


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    pond = list(map(int,input().split()))

    result = frogjump(N, K, pond)

    print(f'#{tc} {result}')