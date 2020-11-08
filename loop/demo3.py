n = 1

x = 1

y = 1

m = 10

while n < m:

    n = n + 1

    while x < n:

        print(" "*(m-x), end='')

        x += 1

    while y < n:

        print("*"*(y+n-2),end="")

        y +=1

    print('')

