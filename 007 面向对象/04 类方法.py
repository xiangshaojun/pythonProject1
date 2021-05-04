# 类方法： 当方法中需要使用类对象（如访问私有类属性）时，定义类方法
# 类方法一般和类属性配合使用
class Dog(object):
    __tooth = 10

    @classmethod
    def get_tooth(cls):
        return cls.__tooth


xiaohei = Dog()
print(Dog.get_tooth())
