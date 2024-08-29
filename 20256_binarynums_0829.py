T = int(input())
for tc in range(1, T+1):
    N, hex = input().split()
    dec = int('0x' + hex, 16) # int사용하여 16진수를 10진수 변경
    bin = format(dec, 'b') # 10진수를 2진수로 변경

    # 2진수를 4자리로 끊기
    while len(bin) < len(N) * 4:
        bin = '0' + bin
    print(f'#{tc} {bin}')


T = int(input())
for tc in range(1, T + 1):
    N, hex = input().split()
    dec = int('0x' + hex, 16) # int 사용하여 16진수를 10진수로 바꾸기
    bin = format(dec, 'b') # format 사용하여 10진수를 2진수로 바꾸기
    # 2진수를 4자리씩 끊기
    while len(bin) < int(N) * 4:
        bin = '0' + bin
    print(f'#{tc} {bin}')

"""
hex_to_bin = {
    '0' : '0000',
    '1' : '0001',
    '2' : '0010',
    '3' : '0011',
    '4' : '0100',
    '5' : '0101',
    '6' : '0110',
    '7' : '0111',
    '8' : '1000',
    '9' : '1001',
    'A' : '1010',
    'B' : '1011',
    'C' : '1100',
    'D' : '1101',
    'E' : '1110',
    'F' : '1111',
}

T = int(input())
for tc in range(1, T+1):
    N, hexn = input().split()
    N = int(N)
    bin_v = ""  # 2진수 변환
    for i in range(N): # 주어진 수를 순회
        bin_v += hex_to_bin[hexn[i]]
    print(f'#{tc} {bin_v}')
"""