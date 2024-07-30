# run : i가 결정되면 -> i+1, i+2가 1 이상
# triplet : i가 결정되면 -> i가 3이상


# run/triplet 조사 후 run data 완전 삭제
# 하지만 그렇게 했을 때 최적이 안 될 수도 있음
# triplet을 먼저 조사 -> run 조사


num = 456789 # baby-gin을 확인할 6자리 수
c = [0] * 12 # 6자리 수로부터 각 자리수를 추출하여 개수를 누적할 리스트
# 10, 11은 더미로 둠

for i in range(len(num)):
    c[num % 10] += 1
    num //= 10

# int(input()) => 자릿수가 정해진 경우 입력하는 것은 도움됨
# but 모르는 경우는 애매

i = 0
tri = run = 0
while i < 10:
    if c[i] >= 3: #triplet 조사 및 데이터 삭제
        c[i] -= 3
        tri += 1
        continue;
    if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1: # run 조사 및 데이터 삭제
        c[i] -= 1
        c[i+1] -= 1
        c[i+2] -= 1
        run +=1
        continue
    i += 1

if run + tri == 2:
    print("Baby Gin")
else:
    print("Lose")