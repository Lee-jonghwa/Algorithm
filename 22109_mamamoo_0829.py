# 데칼코마니의 길이는 항상 홀수

T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 단어의 길이
    words = input()

    max_v = 0
    for i in range(N): #모든 요소를 순회하면서
        cnt = 0 # 데칼코마니 횟수
        for j in range(i+1): #현재 위치 길이 만큼만 순회
            if i+j < N and words[i-j] == words[i+j]:
                cnt += 2
            elif i+j < N and words[i-j] != words[i+j]: # 다르면
                break
        if max_v < cnt - 1:
            max_v = cnt - 1

    print(f'#{tc} {max_v}')
