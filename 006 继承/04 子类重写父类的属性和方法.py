# 师傅类
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


class School(object):
    def __init__(self):
        self.kongfu = '[向氏煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 徒弟类
# class Prentice(Master, School):   #
#     pass
class Prentice(School, Master):  # 默认使用第一个父类的属性和方法，重写父类的属性和方法，默认实例化调用的是子类的属性和方法
    def __init__(self):
        self.kongfu = '[自研煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


daqiu = Prentice()
print(daqiu.kongfu)
daqiu.make_cake()

print(Prentice.__mro__)   # __mro__继承的层级关系
