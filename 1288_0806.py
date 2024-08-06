# T = int(input())
# for tc in range(1, T+1):
#     arr = [0] * 10
#     N = int(input())
#
#     while sum(arr) == 10:
#         for i in len(N):
#             N % 10
#     for k in range(N)
#         for j in range(N):
#             cnt += 1
#             arr[j % 10] = 1
#
#     print(arr)
#     print(cnt)


T = int(input())

ans = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for tc in range(1, T+1):
    N = int(input())

    lst = []
    cnt = 0
    while 1: # 무한루프 -> 될때까지
        cnt += 1 # 돈 횟수
        change_N = list(str(N*cnt))
        lst.extend(change_N)
        a = list(map(int, list(set(lst))))
        a.sort()
        if ans == a:
            print(f"#{tc} {N*cnt}")
            break