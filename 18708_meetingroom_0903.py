N = int(input())
meetings = [tuple(map(int,input().split())) for _ in range(N)]

meetings.sort(key= lambda x:x[1])

now_time = 0
cnt = 0
for i in range(N):
    s, e = meetings[i][0], meetings[i][1]

    if s >= now_time:
        cnt += 1
        now_time = e

print(cnt)