#成员运算符
sheet = ['张三' , '李四' , '王五']
if '张三' in sheet :
    print("张三在听课")
else:
    print("张三已旷课")


#身份验证运算符
a = 5
b = a
c = 5.0
print(b is a )
print(c == a )#数值比较
print(c is a )#内存地址比较

str1 = 2020
str2 = '2020'
print(str1 == str2)
print(str1 is str2)