#用于查找1000以内的质数
#1.判断单个数字为质数
#2.判断多个数值为质数
j = 2
while j <= 1000:
    num = j
    i = 2
    is_prime = True  #标识当前数字是否为质数 True 是，False 不是
    while i < num:
        if num % i == 0:
            is_prime = False
            break
        i = i + 1

    if is_prime == True:
        print("{}是质数".format(num))
    else:
        print("{}不是质数".format(num))
    j = j + 1


