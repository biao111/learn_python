#集合创建
college1 = {'哲学','经济学','法学','教育学'}
print(college1)#hash()散列值的不同，存放的位置不同。散列值快速存取设置数据

#set（）内置函数从其他数据结构转换
college2 = set(['金融学','哲学','经济学','历史学','文学'])
print(college2)

#使用set创建字符串集合
college3 = set("中华人民共和国")
print(college3)

#空集合创建
college4 = set()
print(type(college4))