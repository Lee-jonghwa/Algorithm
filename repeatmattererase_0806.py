'''

T = int(input())
for tc in range(1, T+1):
    st = input()
    s = [st[0]]
    for i in range(1, len(st)):
        s.append(st[i])
        if len(s) > 1 and s[-1] == s[-2]:
            s.pop()
            s.pop()
    print(f'#{tc} {len(s)}')



'''
T = int(input())
for tc in range(1, T+1):
    str_lst = list(input())
    stack = []
    for char in str_lst:
        # 만약 반복문자 라면 --> 반복문자 스택에서 제거 후 반환
        if stack and char == stack[-1]:  #if stack -> 빈 스택이 아닌지 확인 # 현재 문자가 스택의 마지막 요소가 같다면
            stack.pop()
        # 반복문자 아니라면 스택에 추가
        else:
            stack.append(char)
    print(f'#{tc} {len(stack)}')