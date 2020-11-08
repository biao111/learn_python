#函数的使用技巧-2
#1.序列传参
def calc(a,b,c):
    return (a + b) * c
l = [1,5,10]
print(calc(*l))

#2.字典传参
def health_check(name,age,height,weight,hr,hbp,lbp,glbu):
    print(name)
    print(height)
    print(age)
    print("您的健康状况良好")
param = {"name" : "张三","age" : 32,"height" : 178,"weight" : 85.5,"hr" : 70,"hbp" : 120,"lbp" : 80,"glbu" : " 4.3"}
health_check(**param)#注意；两个**

#3.返回值包含多个数据
#在大字典中通过key包含了不同类型的数据
#如果包含了多个子数据，用列表进行囊括。在列表中，用字典表示单个数据
def get_datil_info():
    dict1 = {
        "employee":[
            {"name":"张三","salary":18000},
            {"name":"李四","salary":2000}
        ],
        "device":[
            {"id":"8837120","title":"xxxx笔记本"},
            {"id":"3839011","title":"xxxx台式机"}
        ],
        "asset":[{},{}],
        "porject":[{},{}]
        }
    return dict1
print(get_datil_info())
#获取员工的工资
#1.获取字典信息，并赋值
#2.获取第n位员工的个人信息（列表信息），再获取这个人的“工资”（列表内的字典信息）
d = get_datil_info()
sal = d.get("employee")[0].get("salary")
print(sal)