# 多态定义： 多态是一种使用对象方式，子类重写父类方法，调用不同子类对象的相同父类方法，可以产生不同的执行结果
# 创建Dog父类
class Dog(object):
    def work(self):
        print('指哪打哪。。。')


# 创建ArmyDog子类
class ArmyDog(Dog):
    def work(self):
        print('追击敌人')

# 创建DrugDog子类
class DrugDog(Dog):
    def work(self):
        print('追查毒品')


class Person(object):
    def work_with_dog(self, dog):
        dog.work()

# 创建对象，调用不同的功能，传入不同的对象，观察执行结果
A = ArmyDog()
D = DrugDog()
P = Person()
P.work_with_dog(A)
P.work_with_dog(D)
