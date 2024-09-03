target = int(input())
coins = [10, 50, 100, 500]
coins.sort(reverse=True)

cnt = 0

for coin in coins:
    possible_cnt = target // coin

    cnt += possible_cnt
    target -= possible_cnt * coin

print(cnt)
