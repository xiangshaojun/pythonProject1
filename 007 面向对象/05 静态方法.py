# 静态方法
# 需要通过装饰器@staticmethod来进行修饰，静态方法既不需要传递类对象也不需要传递实例对象（形参没有self/cls）
# 静态方法也可以通过实例对象和类对象访问
# 当方法既不需要使用实例对象（如实例对象，实例属性），也不需要使用类对象（如类属性、类方法、创建实例时）定义静态方法
# 取消不必要的参数传递，有减少不必要的内存占有和性能消耗
class Dog(object):
    @staticmethod
    def info_print():
        print('111')


# 通过类对象访问
Dog.info_print()
# 通过实例对象访问
xiaohei = Dog()
xiaohei.info_print()
