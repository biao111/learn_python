a = 4 > 1 #True
b = 5 < 2 #False
c = 8 == 8 #True
d = 9 < 6 #False

print( a and b) #False
print( a and c) #True
print( a or b) #True
print( b or d) #False
print(not a) #False
print(not b) #True
#逻辑运算符优先级 not >and > or
r1 = a and b or c and not d
#解题思路
# a and b or c and True
#False or True
#true
print(r1)

r2 = (a and (not b or c)) and d
#(a and (True or c)) and d
#(a and true) and d
#True and d
#False
print(r2)