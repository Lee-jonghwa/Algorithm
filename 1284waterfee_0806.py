def goodcomp(P, Q, R, S, W):
    A = P * W
    if W <= R:
        B = Q
    else:
        B = Q + (W - R) * S
    if A > B:
        return B
    else:
        return A

T = int(input())
for tc in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())
    print(f'#{tc} {goodcomp(P, Q, R, S, W)}')
'''
    P # 리터당 요금
    Q # 기본요금
    R # 초과 리터 기준
    S # 리터당 요금
'''
