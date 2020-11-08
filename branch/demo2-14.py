num = int(input("请输入一个三位数："))
# 分别求出三位数的个位，十位，百位
bw = num // 100
sw = (num // 10) % 10
gw = num % 10
# 定义变量total，保存各位数字立方和
total = gw ** 3 + sw ** 3 + bw ** 3
# 用if语句判断条件是否成立，并做出相应的输出
if total == num :
    print("这是水仙花数")
else:
    print("这不是水仙花数")
    # 补全代码