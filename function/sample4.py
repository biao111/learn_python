#函数使用技巧-1
#1.为参数设置默认值，只需要在形参后面增加 "= 具体值" 即可
def calc_exchange_rate(amt,source = 'CNY',target = 'USD'):#target = 'USD'设置默认值
    print(target)
    if source == "CNY" and target == "USD":
        #6.7516 : 1
        result = amt / 6.7516
        #print(result)
        print("汇率换算成功")
        return result
    elif source == 'NCY' and target == "EUR":
        result = amt / 7.7512
        return  result
calc_exchange_rate(100,"CNY","USD")

#2，形参形式传参(关键字传参)
def health_check(name,age,height,weight,hr,hbp,lbp,glbu):
    print("您的健康状况良好")

health_check(name = "张三",age = 32,height = 178,weight = 85.5,hr = 70,hbp = 120,lbp = 80,glbu =  4.3)

#混合形式传参
#*代表之后的所有参数必须使用关键字传参
#如果三个以上的参数建议用字典传参
def health_check1(name,age,*,height,weight,hr,hbp,lbp,glbu):
    print("您的健康状况良好")

health_check1( "张三",32,height = 178,weight = 85.5,hr = 70,hbp = 120,lbp = 80,glbu =  4.3)

#2.字典传参
def health_check(name,age,*,height,weight,hr,hbp,lbp,glbu):
    print(name)
    print(height)
    print(hr)
    print("您的健康状况良好")

param = {"name":"张三","age":32,'height' : 178,'weight' : 85.5,'hr' : 70,'hbp': 120,'lbp' : 80,'glbu': 4.3}
health_check(**param)