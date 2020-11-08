def seq(num, num1, num2):
    # if判断num小于88
    if num < 88:
    # 返回num1与num2的积
        return  (num1 * num2)
    else:
    # 返回num1与num2之和
        return  (num1 + num2)
    # 定义变量tuple1的值为(5,2,1)
tuple1 = (5,2,1)
    # 调用函数，传入参数tuple1，并打印函数返回值
s1 = seq(*tuple1)
print(s1)