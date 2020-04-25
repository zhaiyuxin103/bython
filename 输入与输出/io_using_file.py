poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!
'''

# 打开文件进行 'w'riting 写操作
f = open('poem.txt', 'w')
# 将文本写入到文件
f.write(poem)
# 关闭文件
f.close()

# 如果没有指定文件打开方式
# 默认使用 'r'ead 读模式
f = open('poem.txt')
while True:
    line = f.readline()
    # 零行意味着 EOF 文件结尾
    if len(line) == 0:
        break
    # `line` 中已经自带换行了
    # 因为它是从文件中读取出来的
    print(line, end='')
# 关闭文件
f.close()