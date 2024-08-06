
# 괄호 검사 첫 번째 풀이
'''
T = int(input())
for tc in range(1, T + 1):
    code = input()
    stack = []
    for i in code:
        # 여는 괄호면 스택에 추가
        if i == '{' or i == '(':
            stack.append(i)
        # 닫는 괄호가 중괄호면 짝이 맞는지 확인 후 제거
        elif stack and i == '}' and stack[-1] == '{':
            stack.pop()
        # 닫는 괄호가 소괄호면 짝이 맞는지 확인 후 제거
        elif stack and i == ')' and stack[-1] == '(':
            stack.pop()
        # 근데 짝이 맞지 않아 ---> 스택에 추가
        elif i == '}' or i == ')':
            stack.append(i)

    # if stack:
    #     result = 0
    # else:
    #     result = 1
    result = 0 if stack else 1
    print(f'#{tc} {result}')
'''

# 괄호 검사 두 번째 풀이
'''
def check(code):
    stack = []
    opening = "{("
    closing = "})"
    pairs = {"}" : "{", ")" : "("}

    for char in code:
        # 열린 괄호를 만나면 ---> 스택에 추가
        if char in opening:
            stack.append(char)
        # 닫는 괄호를 만나면 ---> 1. 빈스택 return 0
        #                      2. 스택의 마지막 원소와 현재 괄호의 짝이 맞지 않으면 return 0
        #                      3. 짝이 맞으면 스택에서 제거 pop()
        elif char in closing:
            if not stack or stack.pop() != pairs[char]:
                return 0
        # 스택이 비어있으면(모든 괄호의 짝이 맞는다) return 1
        # 스택에 괄호가 남아있으면(닫히지 않는 괄호가 있다) return 0
        # if not stack:
        #     return 1
        # else:
        #     return 0
    return 1 if not stack else 0

T = int(input())
for tc in range(1, T + 1):
    code = input()
    result = check(code)
    print(f'#{tc} {result}')
'''


T = int(input())
for tc in range(1, T+1):
    code = input()
    stack = []
    for i in code:
        # 여는 괄호면 스택에 추가
        if i == "{" or i == "(":
            stack.append(i)
        # 닫는 괄호가 중괄호면 짝이 맞는지 확인 후
        elif stack and i == '}' and stack[-1] == '{':
            stack.pop()
        elif stack and i == ')' and stack[-1] == '(':
            stack.pop()
        # 짝이 맞지 않는다면? stack에 추가
        elif i == "}" or i == ")":
            stack.append()
    if stack:
        result = 0
    else:
        result = 1
    print(f'#{tc} {result}')


def check(code):
    stack = []
    opening = "{("
    closing = "})"
    pairs = {
        "}":"{",
        ")":"("
    }
    for char in code:
        # 열린 괄호 --> 스택에 추가
        if char in opening:
            stack.append(char)
        # 닫는 괄호 --> 1. 빈스택: return 0
        #               2. 스택이 마지막 원소와 현재 괄호 짝이 맞지 않으면 return 0
        #               3. 스택이 마지막 원소와 현재 괄호 짝이 맞으면 pop()
        elif char in closing:
            if not stack or stack.pop() != pairs[char]:
                return 0
            else:                # stack.pop()가 조건에 있으면 할 필요 없나...?
                stack.pop()
        # 스택이 비어있으면(모든 괄호의 짝이 맞는다) return 1
        # 스택에 괄호가 남아있으면(닫히지 않는 괄호가 있다) return 0
    return 1 if not stack else 0
    # if not stack:
    #     return 1
    # else:
    # return 0

T = int(input())
for tc in range(1, T+1):
    code = input()
    result = check(code)
    print(f'#{tc} {result}')



'''

T = int(input())
for tc in range(1, T + 1):
    st = input()
    stack = []
    result = 1
    for i in st:
        if i == '{' or i == '(':
            stack.append(i)
        elif i == '}':
            if not stack or stack[-1] != '{':
                result = 0
                break
            stack.pop()
        elif i == ')':
            if not stack or stack[-1] != '(':
                result = 0
                break
            stack.pop()

    if result == 1 and not stack:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
'''

'''


T = int(input())
for tc in range(1, T+1):
    st = input()
    s = [] # '{'
    t = [] # '('
    cnt = 0
    result = 0
    for i in st:
        if i == '{':
            s.append(i)
            cnt += 1
        elif i == '(':
            t.append(i)
            cnt += 1
        elif i == '}':
            if len(s) == 0:
                result = 3
                break
            s.pop()
        elif i == ')':
            if len(t) == 0:
                result = 3
                break
            t.pop()
    if len(s) == 0 and len(t) == 0 and result != 3 and cnt != 0:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
'''



'''
T = int(input())
for tc in range(1, T+1):
    st = input()
    g = ['{', '(', '}', ')']
    sum_lst = [0, 0, 0, 0]
    for i in st:
        for j in range(len(g)):
            if g[j] == i:
                sum_lst[j] += 1
    if sum_lst[0] == sum_lst[1] and sum_lst[2] == sum_lst[3]:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
'''