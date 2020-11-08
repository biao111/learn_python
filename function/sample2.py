#函数的形参与实参
#参数救赎函数的输入的数据，在程序运行时根据参数不同执行代码
def print_verse(verse_name,is_show_title,is_show_dynasty):#形参：约束
    #函数体
    if verse_name == "悯农":#实参：传值，格式必须按照形参所规定的
        if is_show_title == True:
            print("静夜思-李白")
        if is_show_dynasty == True:
            print("唐朝")
        print("锄禾日当午")
        print("汗滴禾下土")
        print("谁之盘中餐")
        print("粒粒皆辛苦")
    elif verse_name == "再别康桥":
        if is_show_title == True:
            print("再别康桥-徐志摩")
        if is_show_dynasty == True:
            print("民国")
        print("轻轻的我走了")
        print("正如我轻轻地来")
        print("挥一挥手")
        print("不带走一片云彩")

print_verse('悯农',True,False)
print(",,,")

print_verse('再别康桥',True,True)
