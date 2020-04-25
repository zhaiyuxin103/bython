import pickle

# 这里是将存储对象的文件的名称
shoplistfile = 'shoplist.data'
# 要买的东西的清单
shoplist = ['apple', 'mango', 'carrot']

# 写入文件
f = open(shoplistfile, 'wb')
# 将对象存储到文件
pickle.dump(shoplist, f)
f.close()