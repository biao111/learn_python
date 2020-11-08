# 定义变量x接收输入的第一个数
x = input("请输入一个数")
# 定义变量y接收输入的第二个数
y = input("请输入二个数")
# 判断x是否等与y
if x == y:
    print ("两数相同")
# 判断x是否大于y，条件成立输出 x，反之输出y
else:
    if x > y:
        print ("较大数为第一个数:", x)
    else:
        print ("较大数为第二个数:", y)
