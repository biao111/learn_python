#等值判断
if 1 == 1:
    print("1等于1")
else:
    print("1不等于1")

b = 1 == 1
print(b)
print(1 == 1.0)#这里不用区分数值的类型
print("abc" == "Abc")#字符串无法比较
print("abc".lower() == "abc".lower())#将字符串都转移小写,进行判断
print(" abc".strip() == "abc".strip())#将返回无空格的字符串
print(str(1) == "1")#将某一类型转化另一类型，两者保持相同的类型
#数字与布尔表达式的等值比较
#数字0表示False，非0表示True

print(0 == False)
print(1 == True)

if 3-2:
    print("成立")
else:
    print("不成立")
