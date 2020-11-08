#break
i = 0
while i < 3:
    mobile = input("请输入您要查询的号码： ")
    i = i + 1
    if mobile == "123":
        print("您的话费余额不足！")
        break
print("感谢您的来电")