#定义reason为外层列表，里面有[3,4,5]春季，[6,7,8]夏季，[9,10,11]秋季，[12，1，2]冬季
reason = [[3,4,5],[6,7,8],[9,10,11],[12,1,2]]

while True:
    month = int(input('请输入您要输入的月份，结束程序请按0：'))
    if month == 0:
        print("结束程序！")
        break
    elif month in reason[0]:
        print("{}月份是春季".format(month))
    elif month in reason[1]:
        print("{}月份是夏季".format(month))
    elif month in reason[2]:
        print("{}月份是秋季".format(month))
    elif month in reason[3]:
        print("{}月份是冬季".format(month))
    else:
        print("您输入的有误")
