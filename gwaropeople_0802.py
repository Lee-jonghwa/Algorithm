s = input()

def calculation(s):
    sum_v = 0
    number = ""


    for char in s:
        if char == '[' or char == '{':
            number = ""
        elif char.isdigit():
            number += char
        else:
            if char == ']':
                sum_v += int(number)
                number = ""
            elif char == '}':
                sum_v *= int(number)
                number =""
    return sum_v

result = calculation(s)
print(result)