text = [4,9]
context = text.copy()
text.append(13)
context.append([5,10])
print(context)

text = "Tomorrow"
print(text.find("m",3))

text = "one three "
print(text.find("e",3,8))

str = " http;//www.imooc.com/ "
print(str.find("im,14"))

print(" imooc ".strip()=='Imooc')

s2 = 'love,imooc'
print(s2.split(','))

'''num1 = input("请输入一个数：")
num2 = input("请输入一个数：")
sum1 = num1 + num2
print("两个数的和为",sum1)
'''
s1 = {1,2,3}
print(type(s1))