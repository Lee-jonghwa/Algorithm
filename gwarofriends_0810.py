#[] -> 숫자의 합, {} -> 숫자의 곱

arr = input()

result = 0
num = ''
for char in arr:
    if char.isdecimal(): # 숫자를 만나면
        num += char # num에 추가
    elif char == "[" or char == '{': # 합산의 시작이 되는 수를 만나면
        num = "" # 이때까지 받았던 문자열 초기화
    elif char == "]":
        result += int(num)
    elif char == '}':
        result *= int(num)
    # 만약 합산이 곱셈이면,,,? #그럼 부정확하니 그럴 순 없을 듯

print(result)