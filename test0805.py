'''

# KMP

def Kmp(t, p):
    N = len(t)
    M = len(p)

    # preprocessing
    lps = [0] * (M+1)
    j = 0 # 일치한 개수, 비교할 패턴 위치
    for i in range(1, M):
        lps[i] = j  #p[i]이전에 일치한 개수
        if p[i] == p[j]:
            j += 1
        else:
            j = 0
    lps[M] = j

    # search
    i = 0
    j = 0
    while i < N and j <= M:
        if j == -1 or t[i] == p[j]:
            i += 1
            j += 1
        else:
            j = lps[j]

'''

# 회문(palindrome)
# 단어를 입력받아 회문이면 1, 아니면 0을 출력하는 프로그램
# or 길이가 5인 회문 찾기
# or 긴 문자열 중 회문을 찾았을 때, 그 중 가장 긴 회문의 길이? 등 다양한 문제 가능

# 비교횟수: N // 2
# i : 0 ~ N//2 -1  ==> 인덱

T = int(input())
for tc in range(1, T+1):
    s = input()
    N = len(s)
    ans = 1 # for 문을 다 돌았을 경우
    for i in range(N//2): # i : 0 ~ N // 2 - 1
        if s[i] != s[N-1-i]: # 비교횟수 총 N // 2
            ans = 0
            break
    print(f'#{tc} {ans}')