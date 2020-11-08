a_list = [1, 2, 3, 4, 5]
b_list = [1, 4, 7, 9]
# 求两个列表之间的交集
a_list = set(a_list)
b_list = set(b_list)
int_list = a_list.intersection(b_list)
print(int_list)
# 求两个列表之间的并集
uni_list = a_list.union(b_list)
print(uni_list)
# 求两个列表之间的差集（a_list在b_list中不存在的部分）
dif_list = a_list.difference(b_list)
print(dif_list)