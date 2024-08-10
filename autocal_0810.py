# + 가 있으면 더하고, - 가 있으면 빼기를 하는 계산기

# 스택으로 풀어보자! -> 포기~

# 질문 필요!

arr = input()
result = 0
num = ''
op = '+' # 더하기면 더하고, 빼면 빼고
for char in arr:
    if char.isdecimal(): # 정수면
        num += char # 임시 숫자 문자열 추가
    else: # 현재 연산자를 만났을 때
        if op == '+': # 이전 부호가 더하기면
            result += int(num) # 이때까지 나온 숫자 문자를 결과값에 더하기
        elif op == '-': # 이전 부호가 뺴기면
            result -= int(num) # 이때까지 나온 숫자 문자를 결과값에서 빼기
        op = char
        num = ""

# 마지막 부분에 대한 계산
if num: # 숫자가 있으면
    if op == "+":
        result += int(num)
    elif op == '-':
        result -= int(num)

print(result)
