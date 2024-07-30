'''
[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
다음 줄부터 테스트케이스의 첫 줄에 정수의 개수 N과 구간의 개수 M 주어진다. ( 10 ≤ N ≤ 100,  2 ≤ M ＜ N )
다음 줄에 N개의 정수 ai가 주어진다. ( 1 ≤ a ≤ 10000 )

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

[Test]
3
10 3
1 2 3 4 5 6 7 8 9 10
10 5
6262 6004 1801 7660 7919 1280 525 9798 5134 1821
20 19
3266 9419 3087 9001 9321 1341 7379 6236 5795 8910 2990 2152 2249 4059 1394 6871 4911 3648 1969 2176

'''


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    V = list(map(int, input().split()))
    if (10 <= N <= 100) and (2 <= M < N) and min(V) >= 1 and max(V) <= 10000:
        lst = [] # 이웃한 M개의 합을 저장할 리스트 초기화
        for i in range(N - M + 1): # 마지막 그룹을 N - M + 1에서 시작해야 함
            temp = 0 # 이웃한 N개의 숫자의 합
            for j in range(i, i + M): # 현재의 위치에서 M개의 숫자 더하기
                temp += V[j] # 계산된 M개의 숫자의 합
            lst.append(temp)

            # for j in range(M):
            #     temp = temp + V[i+j]
            # lst.append(temp)

        # max_v = result_lst[0]
        # min_v = result_lst[0]
        # for k in range(len(result_lst)):
        #     if max_v < result_lst[k]:
        #         max_v = result_lst[k]
        #
        # for j in range(len(result_lst)):
        #     if min_v > result_lst[k]:
        #         min_v = result_lst[k]

        print(f'#{tc} {max(result_lst) - min(result_lst)}')