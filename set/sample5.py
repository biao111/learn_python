#生成式
#语法: [被追加的数据 循环语句 循环或判断语句]|{}
#生成式循环|条件多余两个最好用展开式
lst1 = []
for i in range(10,20):
    lst1.append(i * 10)
print(lst1)

lst2 = [ i * 10 for i in range(10,20)]
print(lst2)

lst3 = [ i * 10 for i in range(10,20) if i % 2 == 0]
print(lst3)

lst4 = [ i * j for i in range(1,10) for j in range(1,10)]
print(lst4)

#字典的生成式
lst5 = ['张三','李四','王五']
dict1 = {i+1:lst5[i] for i in range(0,len(lst5))}
print(dict1)

#集合生成式
set1 = {i*j for i in range(1,4) for j in range(1,4) if i == j}
print(set1)