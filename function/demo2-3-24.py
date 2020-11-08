def fun_dict(name, hiredate, tel, dept):
# 使用format格式化字符串，使得向控制台输出结果——小葫芦隶属于技术部，电话:18795642135, 入职日期：2017-9-23,并向控制台输出结果
        print("{name}属于{dept}，电话{tel},入职日期{hiredate}".format(name = name,tel = tel, hiredate = hiredate,dept = dept))

# 创建字典dict1为{'name':'小葫芦','hiredate':'2017-9-23','tel':18795642135,'dept':'技术部'}
dict1 = {'name':'小葫芦','hiredate':'2017-9-23','tel':18795642135,'dept':'技术部'}



# 使用字典dict1作为参数传入函数fun_dict
fun_dict(**dict1)