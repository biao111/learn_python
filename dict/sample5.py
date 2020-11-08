#hash()散列值
h1 = hash("abc")
print(h1)
h2 = hash("bcd")
print(h2)
h3 = hash(8848)
print(h3)
#在同一次调用中，无论调用多少次hash不变，保持稳定性，每次运行调用是不同的
h4 = hash("abc")
h5 = hash("bcd")
print(h4)
print(h5)