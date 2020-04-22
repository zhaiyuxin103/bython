age = 20
name = 'Swaroop'

print('{0} was {1} years old when he wrote this book'.format(name, age))

print('Why is {0} playing with that python?'.format(name))

# 太难看，而且容易出错
print(name + ' is ' + str(age) + ' years old')

print('{} was {} years old when he write this book'.format(name, age))

print('Why is {} playing with that python?'.format(name))

# 取十进制小数点后的精度为 3 ，得到的浮点数为 '0.333'
print('{0:.3f}'.format(1.0/3))

# 填充下划线(_)，文本居中
# 将 '__hello__' 的宽度扩充为 11
print('{0:_^11}'.format('hello'))

# 用基于关键字的方法打印显示，'Swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))

# 防止换行符被打印输出，指定为空
print('a', end='')
print('b', end='')

print('\n')

print('a', end=' ')
print('b', end=' ')
print('c')