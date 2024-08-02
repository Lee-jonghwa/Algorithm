'''
구몽학습을 하는 딸. 레이첼은 덧셈, 뺄셈을 어려워합니다.
와이프 몰래, 레이첼을 위한 프로그램을 제작해주려고 합니다.

'+' 와 '-' 기호가 들어있는 수식을 입력받고
자동으로 계산해주는 프로그램을 작성 해 주세요.

[힌트]

Parsing을 하기 위한 메서드가 불충분하다면
필요한 함수를 직접 구현하는 것이 좋습니다.

[세부조건]

1. 괄호는 없습니다.
2. 첫 번째 수는 양수 또는 음수가 될 수 있습니다.
3. + 와 - 이외 문자는 입력되지 않습니다.
4. 띄어쓰기 없이 입력이 됩니다.
5. 문자열 길이 최대값 : 1000
6. 최종 결과는 음수가 될 수 있습니다.
7. 첫번째 수가 양수라면 '+' 기호가 생략됩니다.
'''
def calculation(s):
    # 초기값 설정
    sum_v = 0
    number = ""
    sign = 1  # 1 for positive, -1 for negative

    # 수식을 한 글자씩 처리
    for char in s:
        if char.isdigit():
            number += char
        else:
            sum_v += sign * int(number)
            number = ""
            if char == '+':
                sign = 1
            else:
                sign = -1
    # 마지막 남은 숫자 추가
    if number:
        sum_v += sign * int(number)
    return sum_v

s = input()

result = calculation(s)
print(result)


'''
def calculate_expression(expression):
    # 초기값 설정
    total = 0
    current_number = ""
    t = 1  # 1 for positive, -1 for negative
    
    # 수식을 한 글자씩 처리
    for char in expression:
        if char.isdigit():
            current_number += char
        else:
            total += sign * int(current_number)
            current_number = ""
            sign = 1 if char == '+' else -1

    # 마지막 남은 숫자 추가
    if current_number:
        total += sign * int(current_number)

    return total

# 입력 값
expression = input("수식을 입력하세요: ")

# 결과 계산 및 출력
result = calculate_expression(expression)
print(result)'''