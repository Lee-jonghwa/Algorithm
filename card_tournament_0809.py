def card(arr, N, i, win_g): # i 는 레벨, N은 branch, win_g는 승자 그룹
    if i == N:
        return w

    win_g =[] # 승자 새로 추가
    # 두 그룹 나누기
    # 1 ~ N//2   N//2+1 ~ N
    for j in range(1, N//2): # 횟수는 인원 -1
        if not used[i]:
            if arr[j] > arr[j+1] or (arr[j]== 1 and arr[j+1] ==3)
                arr[j].append(win_g)
                used[j+1] = 1
            elif arr[j+N//2] > arr[j+N//2+1] or (arr[j+N//2]== 1 and arr[j+N//2+1] ==3)
                arr[j+N//2].append(win_g)
                used[j+N//2+1] = 1



T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 인원수
    arr = list(map(int, input().split()))
    used = [0] * N # 탈락자 체크
