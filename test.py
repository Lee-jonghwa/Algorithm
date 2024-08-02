'''
s1 = 'abc'
s2 = 'abc'
s3 = 'def'
s4 = s1
s5 = s1[:2] + 'c'


print(s1 == s2) # 내용 비교(동일)
l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1 == l2)

print(s1 == s5)
print(s2 is s5) # 내용은 같으나 레퍼런스는 다르다
print(s1 is s2)
'''


# s1 = "A"
# print(ord('A'))
# print(ord(s1))
#
# print(chr(65))



# #str() 쓰지 않고 itoa() 구현???
#
# def my_itoa(num):
#     i = 0
#     for x in num:
#         i = i*10 + chr(ord('0') + x)
#
# my_itoa(123)


a = 'abcdefghij'

b = a[2:2+4] # a[i,i+M]
c = a[2+4-1:2-1:-1] #a[i+M-1:i-1:-1]

print(b)
print(c)