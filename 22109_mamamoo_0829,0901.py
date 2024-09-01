### 1과 0으로 이루어진 "단어"
### 특정 원소를 기준으로 양옆이 같다.


T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 단어의 길이
    word = input()
    max_v = 0
    for i in range(N): # 단어를 순회하면서
        cnt = 1  # 무조건 해당 문자는 데칼코마니에 포함
        for j in range(1,i+1): # i만큼의 길이를 왔다갔다하며, i까지는 전진
            if i-j >= 0 and i+j < N:
                if word[i-j] == word[i+j] : # 단어의 길이를 넘지 않는 선에서 서로 같다면
                    cnt += 2
                else:
                    break # 아니면 바로 벗어나기
        if max_v < cnt:
            max_v = cnt
    print(f'#{tc} {max_v}')

"""
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
"""