class ShortInputException(Exception):
    '''用户定义的异常对象'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    text = input('Enter something --> ')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
    # 其他程序可以在这里正常执行
except EOFError:
    print('Why did you do an EOF on me?')
except ShortInputException as ex:
    print(('ShortInputException: The input was ' +
            '{0} long, expected at least {1}')
            .format(ex.length, ex.atleast))
else:
    print('No exception was raised.')