#4.2项目作业
'''
根据业务需求，现要求慕友们开发一个货币兑换的服务系统，具体要求如下：

   1、实现人民币兑换美元的功能

   2、实现美元兑换人民币的功能

   3、实现人民币兑换欧元的功能

   4、1美元=6.72人民币，1人民币=0.13欧元
'''
service_menu = {1:'人民币兑换美元',2:'美元兑换人民币',
                3:'人民币兑换欧元',0:'结束程序'
                }
while True:
    print("*"*10 + "欢迎使用货币系统" + "*"*10)
    for k,v in service_menu.items():
        print('{}.{}'.format(k,v))
    Your_Choice = int(input( "请您选择需要的服务："))

    if Your_Choice == 0:
        print('推出货币转换系统')
        break

    elif Your_Choice == 1:
        print('~' * 36)
        print('欢迎来到人民币转换美元服务')
        your_money = float(input('请输入您要输入的人民币金额：'))
        RMB_to_US = your_money / 6.72
        print('兑换的美元为：{:0,.2f}$'.format(RMB_to_US))
        print("=" * 36)

    elif Your_Choice == 2:
        print('~' * 36)
        print('欢迎来到美元转换人民币服务：')
        your_money = float(input('请输入您要输入的美元金额：'))
        US_to_RMB = your_money * 6.72
        print('兑换的美元为：{:0,.2f}$'.format(US_to_RMB))
        print('=' * 36)

    elif Your_Choice == 3:
        print('~' * 36)
        print('欢迎来到人民币转换欧元服务')
        your_money = float(input('请输入您要输入的人民币金额：'))
        RMB_to_EUR = your_money * 0.13
        print('兑换的欧元为：{:0,.2f}欧元'.format(RMB_to_EUR))
        print("=" * 36)

    else:
        print(' 当你的选择为其他值时，输出信息有误,请重新输入！')
