# print('''
# dwq
# 474
# ''')
#
# print('%2d-%02d' % (3, 1))
# print('%.2f' % 3.1415926)
#
# sum = 0
# for i in range(101):
#     sum += i
# print(sum)
#
n = 100
sum = 0
while n > 0:
    sum += n
    n -= 2
    if n<50:
        break
print(sum)

n1=1000
print(str(hex(n1)))