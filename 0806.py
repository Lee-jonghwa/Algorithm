### 스택 실습

'''
def push(item, size):   # item: 넣을 요소, size: stack 사이즈
    global top          # 읽어오는 건 global로 되지만, 기록하려면 global 필요
    top += 1
    if top == size:     # 디버깅용 성격이 강함 => 스택이 모자라다는 걸 알림
        print('overflow!')
    else:
        stack[top] = item


def my_pop():
    global top
    if top == -1:
        print('underflow')
        return 0            # 형식을 맞춰주기 위함
    else:
        top -= 1            # top을 하나 먼저 낮춘 후
        return stack[top+1] # 그 자리에 있는 요소를 리턴
        # 요소를 지울 필요는 없음
        # top을 낮추는 것과 요소 리턴의 자리를 바꿔도 상관 없음


stack = []
stack.append(1) # push(1)
stack.append(2) # push(2)
stack.append(3) # push(3)
print(stack)
print(stack.pop())
print(stack.pop())
print(stack.pop())
'''

'''
##
STACK_SIZE = 10
stack = [0] * 10
top = -1

top += 1 # push(1)
stack[top] = 1
top += 1 # push(2)
stack[top] = 2
top += 1 # push(3)
stack[top] = 3

print(stack)

top -= 1
print(stack[top+1])
print(stack[top])
top -= 1
print(stack[top])
top -= 1

print(stack)

'''

'''
## Function Call 확인

# f2
def f2(c, d):
    return c - d

# f1
def f1(a, b):
    c = a + b
    d = 10
    return f2(c, d)

# main
a = 10
b = 20
print(f1(a, b))



# f2
def f2(d, c):
    return d - c

# f1
def f1(b, a):
    c = a + b
    d = 10
    return f2(c, d)

# main
a = 10
b = 20
print(f1(a, b))

'''


'''
def fibo(n):
    if n < 2:               # 중단 조건 설정하기
        return n
    else:
        return fibo(n-1) + fibo(n-2)

def fact(n):
    if n == 1:              # 중단 조건 설정하기
        return 1
    else:
        return n * fact(n-1)


def f(n):
    global cnt
    cnt += 1
    if n == 0:
        return
    else:
        f(n-1)

cnt = 0

'''
'''
### 모든 배열 원소 접근


def f(i, N):        # i: 접근할 원소 인덱스, N: 크기
    if i == N:      # 배열을 벗어난 경우
        return
    else:           # 그렇지 않은 경우
        print(arr[i])
        f(i+1, N)
        return

arr = [1, 2, 3]
N = 3
f(0, N)
'''

### 배열에 특정값 있는 경우

def f(i, N, v):
    if i == N:
        return 0
    elif arr[i] ==v:
        return i, 1
    else:
        return f(i+1, N, v)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = 10
v = 5

print(f(0, N, v))