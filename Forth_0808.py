def check(arr):
    stack = []
    for i in arr[:-1]: # 마지막 제외하고 순회(".")
        if i.isdecimal(): # 문자열인 i를 확인
            stack.append(int(i))
        elif i in {'+','-','*','/'}: #op set을 만듬
            if len(stack) < 2: #스택에 숫자가 2개 미만이면 에러
                return 'error'
            b = stack.pop() # 두 번째 숫자
            a = stack.pop() # 첫 번째 숫자
            if i == '+': stack.append(a + b)
            elif i == '-': stack.append(a - b)
            elif i == '*': stack.append(a * b)
            elif i == '/': stack.append(a // b) # 정수나눗셈

    if len(stack) != 1:
        return 'error'

    return stack[0]

T = int(input())
for tc in range(1, T+1):
    Forth = input().split()
    result = check(Forth)
    print(f'#{tc} {result}')


'''
T = int(input())
for tc in range(1, T + 1):
    a = list(input().split())
    stack = []  # 피연산자 보관
    op = ['-', "*", '+', '/']
    result = "error"  # 초기 결과값은 "error"로 설정

    for i in a:
        if i == ".":
            if len(stack) == 1:
                result = stack.pop() # 마지막 값을 result로 꺼냄
            break
        elif i not in op:
            stack.append(i)
        elif i in op:  # 연산자를 만나면 -> 뒤 두 요소 꺼냄
            if len(stack) < 2:  # stack에 2개 이하의 요소가 있는데 연산자가 나왔으면
                break
            b = int(stack.pop())
            c = int(stack.pop())
            if i == '-':
                stack.append(c - b)
            elif i == '*':
                stack.append(c * b)
            elif i == "+":
                stack.append(c + b)
            elif i == "/":
                if b == 0:  # 0으로 나누기 방지
                    break
                stack.append(c // b)  # 정수 나눗셈

    if result == "error":
        print(f'#{tc} {result}')
    else:
        print(f'#{tc} {int(result)}')
'''