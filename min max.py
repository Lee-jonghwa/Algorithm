'''
3
5
477162 658880 751280 927930 297191
5
565469 851600 460874 148692 111090
10
784386 279993 982220 996285 614710 992232 195265 359810 919192 158175

'''

'''
T = int(input())    # 테스트케이스 개수

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_v = arr[0]
    min_v = arr[0]

    for i in range(1, N):
        if max_v < arr[i]:
            max_v = arr[i]

    for j in range(1, N):
        if min_v > arr[j]:
            min_v = arr[j]

    print(f'#{tc} {max_v - min_v}')
'''

'''
T = int(input())
for tc in range(1, T+1):
    numbers = list(map(int, input().split()))
    print(f'#{tc} {max(numbers) - min(numbers)}')
'''

'''
가장 큰 값  = max_v
모든 값과 max_v를 비교해서 항상 큰 값
-> 가장 앞 값으로 초기화 후 비교
가장 작은 값 = min_v

max_v <- arr[0]
for i : 1 -> N - 1
    if max_v < arr[i]
        max_v <- arr[i]
print(max_v);

min_v <- arr[0]
for i : 1 -> N - 1
    if min_v > arr[i]
        min_v <- arr[i]
print(min_v);
'''
