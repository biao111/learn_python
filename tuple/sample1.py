#元组的创建
#创建
t = ('a','b','c')
print(t)
print(type(t))
t = 'a','b','c',1,2,3
print(t)
print(type(t))

#获取数据，再获取数据时与列表完全相同
print(t[5])#正序索引，获取6个元素
print(t[-1])#倒序索引
print(t[1:4])#范围取值
print("b" in t)#成员运算符

#元组在创建后，内容不可变
#t[0] = 2
#写入数据的函数同样不会变
#t.append('f')
#t.insert('f')

#如果软组内有列表，那么列表内容允许被改变
t2 = (['张三',38,5000],['李四',28,2000])
item = t2[0]
print(item)
print(type(item))
item = 40
print(item)
#t2.pop(0)

#元组运算符
#元组运算符同样适用于列表，切记不好混合使用 
t3 = (11,2,3) + (4,5,6)
print(t3)
t4 = ('see','you') * 2
print(t4)
#如果元组只有一个元素时，必须在这个元素后增加逗号说明这是一个元组
#如果没有逗号，那么按算数运算符计算
t5 = ("seee",) * 5
print(t5)
