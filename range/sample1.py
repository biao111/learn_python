#创建数字序列
r1 = range(10,20)#10到19的整数，左闭右开
print(r1)
print(type(r1))
print(r1[9])
print(r1[3:5])

#增加步长
r2 = range(10,20,2)
print(r2)#10,12,,14,16,18
print(r2[4])
print(r2[0:2])

#成员运算符
print(12 in range(10,20))#序列数据通用的
print(22 not in range(10,20))