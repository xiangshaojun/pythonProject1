# 需求：洗衣机、功能：洗衣服
# 1. 定义类：
"""
class 类名()
    代码
"""


class Washer():
    def wash(self):  # self 指调用该函数的对象
        print("洗衣服")
        print(self)


# 2. 创建对象
haier = Washer()
# 3. 验证成果
print(haier)

# 4. 使用功能，实例方法/对象方法
haier.wash()
# 5. 一个类创建多个对象，返回的内存地址不一致
meide = Washer()
meide.wash()