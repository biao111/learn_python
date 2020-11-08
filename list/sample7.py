#多维列表
#[姓名,年龄,工资],[姓名,年龄,工资],[姓名,年龄,工资],[姓名,年龄,工资],[姓名,年龄,工资]
#字符串："姓名,年龄,工资"例如："张三,30,2000"
#str = "张三,30,2000"
#l = str.split( ",")  split()函数分割列表
#print(l)
emp_list = []
while True:
    info = input("请输入员工信息：")
    if info == "":
        print("结束程序！")
        break
    info_list = info.split(",")
    if len(info_list) != 3:
        print("输入的格式不正确，请重新输入！")
        continue
    #print(info_list)
    emp_list.append(info_list)
    #print(emp_list)

    for emp in emp_list:
        print("姓名：{name},年龄：{age},工资：{salary}".format(name = emp[0] ,age = emp[1], salary = emp[2]))