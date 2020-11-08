#字典创建
#1.使用{}
dict1 = {}#空的字典
print(type(dict1))
dict2 = {'name':'王峰','sex':'男',
         'hirdate':'1997-10-20','grade':'A',
         'job':'销售','salary':1000,
         'welfare':100
         }
print(dict2)

#利用dict函数创建字典
dict3 = dict(name = '王峰',sex = '男',
         hirdate = '1997-10-20',grade = 'A',
         job = '销售',salary = 1000,
         welfare = 100)
print(dict3)
dict4 = dict.fromkeys(['name','sex','hirdate','grade'],'N/A')#创建新的字典,并初始默认值
print(dict4)