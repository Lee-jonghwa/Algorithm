# import sys
# sys.stdin = open("./input/txt", "r") ==> 인풋 파일을 받아두고 동작하면, 자동으로 테스트 해줌 -> 연습할 때 유용!


T = int(input())
for tc in range(1, T+1):
    str1 = input() # 문자열 길이 N
    str2 = input() # 문자열 길이 M
    result = int(str1 in str2)
    print(f'#{tc} {result}')
'''
   
T = int(input())
for tc in range(1, T+1):
    str1 = input() # 문자열 길이 N
    str2 = input() # 문자열 길이 M
    result = 0

    # st2 안에서 str1 찾기
    for i in range(len(str2)-len(str1) +1):
        cnt = 0
        # str1은 모든 문자열 검사, str1의 문자만큼 순회
        for j in range(len(str1)):
            # str1의 j 번째, str2의 i + j번째
            if str1[j] == str2[i + j]:
                cnt += 1
        if cnt == str1:
            result = 1
    print(f'#{tc} {result}')
'''


'''
    cnt = 0
    i = 0
    while i <= len(str2) - len(str1):
        i += 1
        if str1 == str2[i:i+len(str1)]:
            cnt += 1
        else:
            continue
    print(f'#{tc} {cnt}')

'''