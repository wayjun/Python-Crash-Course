# 编写函数
def make_shirt(size = "large", typeface = "I love Python"):
    print("\nThe size of the T-shirt is: " + size + " and the words of the T-shirt are: " + typeface.title() + ".")

# 调用函数
make_shirt()
make_shirt("medium")
make_shirt(size = "arbitrary", typeface = "I love you")