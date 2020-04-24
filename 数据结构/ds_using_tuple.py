# 尽管圆括号是可选的
# 还是建议使用圆括号
# 来表示元组的开始和结束
# 因为显式总比隐士要好
zoo = ('python', 'elephant', 'penguin')
print('Number of animals in the zoo is', len(zoo))

new_zoo = 'monkey', 'camel', zoo    # parentheses not required but are a good ides
print('Number of cages in the new zoo is', len(new_zoo))
print('All animals in new zoo are', new_zoo)
print('Animals brought from old zoo are', new_zoo[2])
print('Last animal brought from old zoo is', new_zoo[2][2])
print('Number of animals in the new zoo is',
    len(new_zoo)-1+len(new_zoo[2]))