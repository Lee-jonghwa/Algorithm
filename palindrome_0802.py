## 함수 만들어 푸는 습관 들이기 -> 디버깅할 때 편함

# for i : 0 -> N-1
# for j : 0 -> N-M+1 # j열부터 길이가 M인 회문인가?


# 비교횟수 방법
# 회문인지 확인하는 인덱스: k
# for k : 0 -> M//2-1
# A[i][j+K] == A[i][j+M-1-k]


def find_p(N, M, arr):
    for i in range(N):
        for j in range(N-M+1):
            # 가로 회문 : 시작점 j 에서 j + M (행 고정)
            h = arr[i][j:j+M]
            # 세로 회문 : 시작점 i 에서 j + M (열 고정)
            v = [arr[k][i] for k in range(j, j+M)]
            if h == h[::-1]:
                return h
            if v == v[::-1]:
                return v


T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    result = find_p(N, M, arr)
    print(f'#{tc} ', *result, sep="")

'''

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input().strip() for _ in range(N)]
    result = ''

    # 가로로 된 회문 찾기
    for i in range(N):
        for j in range(N - M + 1):
            # 가로 회문
            h = arr[i][j:j+M]
            if h == h[::-1]:
                result = h
                break
            # 세로 회문
            v = [arr[k][j] for k in range(j, j+M)]
            if v == v[::-1]:
                result = v
                break
        if result:
            break
    print(f'#{tc} {result}')

'''

'''
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input().strip() for _ in range(N)]
    result = ''

    # 가로로 된 회문 찾기
    for i in range(N):
        for j in range(N - M + 1):
            ans = arr[i][j:j+M]
            if ans == ans[::-1]:
                result = ans
                break
        if result:
            break

    # 세로로 된 회문 찾기
    if not result:
        for j in range(N):
            for i in range(N - M + 1):
                ans = ''.join([arr[k][j] for k in range(i, i + M)])
                if ans == ans[::-1]:
                    result = ans
                    break
            if result:
                break

    print(f'#{tc} {result}')
'''


'''
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(N)]
    result = []
    for i in range(N):
        for j in range(N):
            ans = arr[i][j:j+M]
            if ans == ans[::-1]:
                result = ans
                break
        if result:
            break
    if not result:
        for j in range(N):
            for i in range(N-M+1):
                ans = ''.join([arr[k][j] for k in range(i, i + M)])
                if ans == ans[::-1]:
                    result = ans
                    break
            if result:
                break

    print(f'#{tc}', "".join(result))
'''

'''
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(N)]
    result = []
    for i in range(N):
        for j in range(N):
            if j + M <= N:
                ans = arr[i][j:j+M]
                if ans == ans[::-1]:
                    result = arr[i][j:j+M]
                else:
                    continue
    for j in range(N):
        wrd_lst = []
        for i in range(N):
            wrd_lst.append(arr[i][j])
        if len(wrd_lst) == M and wrd_lst == wrd_lst[::-1]:
            result = wrd_lst
            break
    print(f'#{tc}', "".join(result))
'''



'''
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(N)]
    result = []
    for i in range(N):
        for j in range(N):
            if j + M <= N:
                if j - 1 < 0:
                    if arr[i][j:j+M] == arr[i][j+M-1::-1]:
                        result = arr[i][j:j+M]
                        # print(f'#{tc}', "".join(arr[i][j:j+M]))
                elif arr[i][j:j+M] == arr[i][j+M-1:j-1:-1]:
                    result = arr[i][j:j + M]
                    # print(f'#{tc}', "".join(arr[i][j:j+M]))
                else:
                    continue
    for j in range(N):
        wrd_lst = []
        for i in range(N):
            wrd_lst.append(arr[i][j])
        if wrd_lst == wrd_lst[::-1]:
            result = wrd_lst
            break
    print(f'#{tc}', "".join(result))
'''