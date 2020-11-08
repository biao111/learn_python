name = "小明"
age = 25
height = 180.5
str1 = "我叫" + name +  "，今年" + str(age) + "岁，身高" + str(height)
print(str1)
str2 = "我叫{0}，今年{1}岁，身高{2}".format(name, age, height)
print(str2)
str3 = "我叫{p1}，今年{p2}岁，身高{p3}".format(p1=name, p2=age, p3=height)
print(str3)
#数字的格式化
num = 1234567.89555
str4 = format(num , "0.2f")
print(type(str4))
print(str4)

account = "8810381"
amt = 123456789
str5 = format(amt , "0,.3f")
#print(str5)
str6 = "请您向" + account + "账户转账￥" + str5 + "元"#传统格式
print(str6)
#在字符串格式化输出时，如果遇到格式化输出数字，则需要在{}内增加：的前缀，之后写上数字格式化的语句
str7 = "请您向{}用户转账￥{:0,.3f}元".format(account , amt)
print(str7)