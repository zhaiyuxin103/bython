def print_max(a, b):
    if a > b:
        print(a, 'is maximum')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is maxmum')

# 直接传递字面量
print_max(3, 4)

x = 5
y = 7

# 传递变量作为实参
print_max(x, y)