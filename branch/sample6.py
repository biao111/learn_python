high = input("请您输入测量的高压值：")
low = input("请您输入测量的低压值：")
high = int(high)
low = int(low)

if (low > 60 and low < 90) and (high > 90 and high < 120):
    print("您的血压正常，请继续保持健康的生活习惯")
else:
    if low <= 60:
        print("您的血压过低，请注意补充营养。")
    elif high <= 90:
        print("您的高压过低，请务必加强锻炼，提高心肺功能")
    else:
        print("您的血压出现异常，请尽快就医！！！")

