print("欢迎使用收银台程序")
goods = input("请输入商品名称： ")
price = input("请输入商品价格： ")
num = input("请输入商品的数量： ")
total = float(price) *int(num) * 0.9
alipay_total = total * 0.95
print("您购买的商品为： ")
print(goods)
print("商品的价格为： ")
print(total)
print("您需要使用支付宝支付：")
print(alipay_total)