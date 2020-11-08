def info(*, desc,birth, name='imooc'):
    # 使用format格式化字符串向控制台输出——imooc-程序员的梦工厂出生于2013年8月
     print("{name}-{desc}出生于{birth}".format(desc = desc,birth = birth,name =name))
# 调用函数，向函数内传入（"程序员的梦工厂"，"2013年8月"）
i = info(desc = "程序员梦工厂" , birth = "2013年8月", name = "imooc")
