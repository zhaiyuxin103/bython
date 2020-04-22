number = 23
guess = int(input('Enter an integer : '))

if guess == number:
    # 新程序块的开始处
    print('Congratulations, you guessed it.')
    print('(but you do not win any prizes!)')
    # 新程序块的结尾处
elif guess < number:
    # 另一个程序块
    print('No, it is a little higher than that')
    # 你可以在程序块中“为所欲为”--做任何你想做的事
else:
    print('No, it is a little lower than that')
    # 只有当猜测数大于给定数的时候，才会执行次数

print('Done')
# 在 if 语句执行结束后，最后的这句语句总是会被执行