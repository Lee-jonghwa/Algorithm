# N명의 친구들이 참석
# 보드카는 6병 세트, 또는 낱개로 팔고 있다.
# 마트마다 각 제품의 가격은 상이하다.

# 참석 인원 N과 M개의 마트에서 파는 제품의 정보가 주어졌을 때,
# 1인당 최소 하나 이상의 보드카 준비하기 위해서


N, M = map(int,input().split())
vodcas = [tuple(map(int,input().split())) for _ in range(M)]

vodcas_6 = sorted(vodcas, key= lambda x:x[0])
vodcas_1 = sorted(vodcas, key= lambda x:x[1])

min_set_price = vodcas_6[0][0]
min_one_price = vodcas_1[0][1]

# 세트와 비교했을 때, 많이 사더라도 세트가 사면 싼 것임
# 따라서 N 개를 모두 세트로 사는 게 싼지, 섞어서 사는 게 싼지 생각

# 세트로만 살 때
# (N//6+1)*min_set_price
# 낱개도 살 때
# (N//6)*min_set_price + N%6*min_one_price

# 두 개 비교
if N % 6:
    result = min((N//6+1)*min_set_price, (N//6)*min_set_price + N%6*min_one_price)
else:
    result = min((N // 6) * min_set_price, (N // 6) * min_set_price + N % 6 * min_one_price)

print(result)