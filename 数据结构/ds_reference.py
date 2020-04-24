print('Simple Assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']
# mylist 只是指向同一个对象的另一个别名！
mylist = shoplist

# 我买下了第一件商品，所以把它从列表中移除
del shoplist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)
# 注意到 shoplist 和 mylist 产生了同样的输出
# 输出的都是没有 'apple' 的相同列表
# 这验证了它们都指向着同一个副本

print('Copy by making a full slice')
# 通过全切片来获得一个副本
mylist = shoplist[:]
# 移除第一个元素
del mylist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)
# 注意到现在这两个列表有差异了