#函数返回值
#参数是函数的输入数据，而返回值是函数的输出结果
#return不是必须的，return语句执行后，将函数执行中断
def calc_exchange_rate(amt,source,target):
    if source == "CNY" and target == "USD":
        #6.7516 : 1
        result = amt / 6.7516
        #print(result)
        return result
        print("汇率计算成功")

r = calc_exchange_rate(100,"CNY","USD")
print(r)
r = calc_exchange_rate(100,"EUR","USD")#None代表不存在的含义
print(r)