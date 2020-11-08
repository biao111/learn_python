#集合的遍历
college1 = {"哲学","经济学","法学","教育学"}
for c in college1:
    print(c)

#判断元素存在
print("哲学" in college1)
print("计算机" in college1)

#集合不支持按索引提取数据
#print(college1[3])

#新增数据，一次只能添加一个元素
college1.add("计算机学")
college1.add("法学")#因为被重复，所以被忽略掉
print(college1)

#update方法一次添加多个元素
college1.update(["生物学","工程学"])
print(college1)

#更新操作，需要先删除原有元素，在创建新元素
#remove如果删除不存在的元素时，会报错
college1.remove("生物学")
#discard如果遇到元素不存在，则会忽略删除操作
college1.discard("生物学")
college1.add("医学")
print(college1)