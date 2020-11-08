#定义变量year，并接收“请输入正确的年份：”
year = input("请输入正确的年份")
#判断是否是闰年：1、能被4整除,但是不能被100整除的年份 2、能被400整除的年份
if int(year) / 4 and not int(year) / 100 and int(year) / 400:
    print("{0}年是闰年".format(year))
else:
    print("{0}年不是闰年".format(year))