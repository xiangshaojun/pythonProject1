# 师傅类
class Master(object):

    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

        self.__num = 2000

    def get_num(self):
        return self.__num

    def set_num(self):
        self.__num = 5000

    # def __test(self):
    #     print('fdafasfdaa')

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


class School(Master):
    def __init__(self):
        self.kongfu = '[向氏煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

    def make_old_cake(self):
        # super(School, self).__init__()
        # super(School, self).make_cake()
        super().__init__()
        super().make_cake()


# 徒弟类
# class Prentice(Master, School):   #
#     pass
class Prentice(School):  # 默认使用第一个父类的属性和方法，重写父类的属性和方法，默认实例化调用的是子类的属性和方法
    def __init__(self):
        self.kongfu = '[自研煎饼果子配方]'

    def make_cake(self):
        self.__init__()  # 再次调用子类的__init__
        print(f'运用{self.kongfu}制作煎饼果子')

    # def make_master_cake(self):
    #     Master.__init__(self)  # 再次调用初始化的原因：调用父类的同名属性和方法，需要再次调用__init__方法
    #     Master.make_cake(self)
    #
    # def make_school_cake(self):
    #     School.__init__(self)
    #     School.make_cake(self)

    def make_old_cake(self):
        # 第一种调用父类同名方法和属性的方式
        # School.__init__(self)
        # School.make_cake(self)
        # 第二种调用父类同名方法和属性的方式
        # 2.1 带参数的调用
        # super(Prentice, self).__init__()
        # super(Prentice, self).make_cake()
        # super(Prentice, self).__init__()
        # super(Prentice, self).make_old_cake()
        # 2.2 不带参数
        super().__init__()
        super().make_cake()
        super().make_old_cake()


# daqiu = Prentice()
# daqiu.make_old_cake()
# daqiu.make_cake()
# daqiu.__num     # 私有属性不能被继承
# daqiu.__test()  # 私有方法不萌被继承
daqiu = Master()
print(daqiu.get_num())
daqiu.set_num()
print(daqiu.get_num())
