def print_max(x, y):
    '''Prints the maximum of two numbers.

    The two values must be integers.'''
    # 如果有必要，将参数转为整数
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')

print_max(3, 5)
print(print_max.__doc__)

help(print_max)