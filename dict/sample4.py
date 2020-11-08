#为字典设置默认值
#字典的视图
#字典格式化输出字符串

emp1 = {'name':'Jacky' , 'grade':'B'}
emp2 = {'name':'Lily'}
#setfault为字典设置默认值，如果某个key已存在呢忽略，如果不存在则设置
emp1.setdefault('grade' , 'C')
emp2.setdefault('grade' , 'C')
print(emp1)
print(emp2)

#2.获取字典的视图
#（1）keys代表获取的键
ks = emp1.keys()
print(ks)
print(type(ks))
#（2）values代表获取所有的值
vs = emp1.values()
print(vs)
print(type(vs))
#（3）items代表获取所有的键值对
its = emp1.items()
print(its)
print(type(its))
#随着原始数据的变化，产生相应的变化
emp1['hiredate'] = '1984-05-30'
print(ks)
print(vs)
print(its)

#3.字符串格式化
#老版本的字符串格式化
emp_str = "姓名:%(name)s,评级:%(grade)s,入职时间:%(hiredate)s"%emp1
print(emp_str)

#新版本的字符串的格式化
emp_str1 = "姓名:{name},评级:{grade},入职时间:{hiredate}".format_map(emp1)
print(emp_str1)