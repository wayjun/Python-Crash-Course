# 定义变量
first_number = input("\n请输入一个数： ")
second_number = input("请输入另一个数： ")

try:
     # ValueError异常处理
    numbers_sum = int(first_number) + int(second_number)
    print("您输入的两个数字之和为： " + str(numbers_sum))
except ValueError:
    print("抱歉，您输入的不是两个数字！")