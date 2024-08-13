# lev = 4 (4장뽑기)
# branch = N (0 ~ 9까지 중 N장)

arr = list(map(int, input()))
n = len(arr)

path = [] # 경로를 저장할 리스트

# 중복 가능이므로 path 안 함
cnt = 0

def cards(lev):
    global cnt

    # 네 장을 다 뽑으면 경우의 수 증가
    if lev == 4:
        cnt += 1
        return


    for i in range(n):
        # 첫 번째 카드는 조건 없이 제거, 뽑게될 카드와 뽑은 카드를 비교
        if lev == 0 or abs(arr[i] - path[lev-1]) <= 3:
            path.append(arr[i])
            cards(lev + 1)
            path.pop() # 재귀 호출 후 마지막 카드 제거

cards(0)
print(cnt)