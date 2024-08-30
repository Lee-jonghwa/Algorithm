print(7 & 5)
print(7 | 5)


print(bin(10))  # 0b1010
print(hex(10))  # 0xa

print(int('1011', 2))  # 11
print(int('b', 16))  # 11

print(0b11011110 & 0b11011)  # 26
print(bin(0x4A3 | 25))  # 0b10010111011
print(0x4A3 | 25)  # 1211

print(7070^1004)  # 6258
print(6258^1004)  # 7070

print("-"*20)

print(1)  # 1
print(1 << 1)  # 2
print(1 << 2)  # 4
print(4 >> 1)  # 2
print(4 >> 2)  # 1
print(4 >> 3)  # 0

print("-"*20)

# 각 자리를 쓴다/ 안쓴다 -> 나올 수 있는 경우의 수 2가지
# 각 자리마다 2가지 경우의 수 -> 길이가 N이라면 -> 2^N 만큼의 경우의 수가 나올 수 있다

arr = [1, 2, 3, 4]

print(f'부분집합의 수 : {1 << len(arr)}')

for i in range(1 << len(arr)):
    print(i, end =" ")
print()

"""
부분집합의 수 : 16
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 
"""


# i & (1 << N): N번째 비트가 1인지 0인지 확인

for i in range(1 << len(arr)):  # i 번째 부분집합
    for idx in range(len(arr)):
        # i & (1 << idx)
        # i번째 부분집합에 idx 요소가 포함되어 있나요?
        if i & (1 << idx):
            print(arr[idx], end=" ")
    print()

"""
1 
2 
1 2 
3 
1 3 
2 3 
1 2 3 
4 
1 4 
2 4 
1 2 4 
3 4 
1 3 4 
2 3 4 
1 2 3 4 
"""

print("-"*20)

print(bin(4))  # 0b100
print(bin(~4))  # -0b101
print(~4)  # 5


t = 0.1
print(f'{t:.2f}')  # 0.10
print(f'{t:.3f}')  # 0.100
print(f'{t:.4f}')  # 0.1000
print(f'{t:.25f}')  # 0.1000000000000000055511151
