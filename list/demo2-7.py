#已知一个列表，存储1到10的元素遍历循环列表中的所有偶数
list = [1, 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]
i = 0
for list1 in list:
    if list1 % 2 == 0:
        i += 1
        print("第{}个偶数{}".format(i , list1) )
