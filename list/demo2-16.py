#定义一个列表list1[23,98,56,55,76,98,55] ,对列表去重后降序排序
list1 = [23,98,56,55,76,98,55]
list2 = []
for p in list1:
    if p not in list2:
        list2.append(p)
print(list2)
list2.sort(reverse=True)
print(list2)