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
        self.__init__()  # 再次调用子类的__init__
        print(f'运用{self.kongfu}制作煎饼果子')

    def make_master_cake(self):
        Master.__init__(self)  # 再次调用初始化的原因：调用父类的同名属性和方法，需要再次调用__init__方法
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)


# 定义徒孙类
class TuSun(Prentice):
    pass


xiaoqiu = TuSun()
xiaoqiu.make_cake()
xiaoqiu.make_master_cake()
xiaoqiu.make_school_cake()
