# 类属性就是类对象的所有拥有的属性，它被该类的所有实例对象所共有
# 类属性可以使用类对象或实例对象引用

# 类属性的优点，
# 记录的某项数据始终保持一致时，则定义类属性
# 实例属性要求每个对象为其单独开辟一份内存空间来记录数据，而类 属性为全类所共有，仅占用一份内存，更节省内存空间
class Dog(object):
    tooth = 10


xiaohei = Dog()
wangcai = Dog()
print(Dog.tooth)  # 通过类对象引用
print(xiaohei.tooth)  # 通过实例对象引用
print(wangcai.tooth)
