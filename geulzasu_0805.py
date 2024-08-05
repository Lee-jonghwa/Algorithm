def str_num(s1, s2):
    max_v = 0
    for i in range(len(s1)):
        cnt = [0] * len(s1) # s1의 원소만큼 배열 생성
        for j in range(len(s2)):
            if s1[i] == s2[j]: # 값이 같은 경우
                cnt[i] += 1 # cnt와 원소 값이 같으므로 배열
        for k in range(len(cnt)): # cnt의 값 중 최대값을 max_v로
            if max_v < cnt[k]:
                max_v = cnt[k]
    return max_v

T = int(input())
for tc in range(1, T+1):
    s1 = input()
    s2 = input()
    print(f'#{tc} {str_num(s1, s2)}')