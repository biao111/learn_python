def login(username,password):
    if username == "imooc" and password == "123456":
        return  "登录成功"
    else:
        return "请重新输入"

login1 = login('imooc','123456')
print(login1)
login2 = login('imoo','123456')
print(login2)