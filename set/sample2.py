college1 = {'哲学','经济学','法学','教育学'}
college2 = set(['金融学','哲学','经济学','历史学','文学'])

#交集,获取两个集合的重要部分，新建一个集合
c3 = college1.intersection(college2)
print(c3)
college1.intersection_update(college2)
print(college1)

college1 = {'哲学','经济学','法学','教育学'}
college2 = set(['金融学','哲学','经济学','历史学','文学'])
#并集，将两个集合所有元素合并，去重
c4 = college1.union(college2)
print(c4)

college1 = {'哲学','经济学','法学','教育学'}
college2 = set(['金融学','哲学','经济学','历史学','文学'])
#差集，是指两个集合之间的差异部分
c5 = college1.difference(college2)#代表集合中不存在的部分，单向差集1→2
print(c5)
#symmetric_difference双向差集,symmetric均衡
c6 = college1.symmetric_difference(college2)
print(c6)

college1.difference_update(college2)
print(college1)
college1.symmetric_difference_update(college2)
print(college1)