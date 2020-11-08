#序列类型转换
l1 = ['a','b','c']
t1 = ('d','e','f')
s1 = 'abc123'
s2 = 'abc,123'
r1 = range(1,4)
#list()-转换为列表
l2 = list(t1)
print(t1)
print(list(s1))
print(s2.split(","))
print(list(r1))

#tuple()-转换为元组
print(tuple(l1))
print(tuple(s1))
print(tuple(s2.split(",")))#含特殊符号，将其转为列表，再转为元组
print(tuple(r1))

#str函数将单个数据转为字符串 join对列表进行连接
print(str(l1))
print("".join(l1))#”"引号内要打印的连字符
print("|".join(t1))#join必须是要求所有元素都是字符串
#print("".join(r1))
s3 = ""
for i in r1:
    s3 += str(i)
print(s3)