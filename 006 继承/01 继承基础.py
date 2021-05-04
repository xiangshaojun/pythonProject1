# 继承：继承父类的属性和方法
class A(object):
    def __init__(self):
        self.num = 1

    def info_print(self):
        print(self.num)


class B(A):
    pass


test = B()
test.info_print()