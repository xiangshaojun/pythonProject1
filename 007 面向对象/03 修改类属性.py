class Dog(object):
    tooth = 10


# 修改类属性  类.属性=值
# Dog.tooth = 20
# print(Dog.tooth)
# wangcai = Dog()
# xiaohei = Dog()
# print(wangcai.tooth)
# print(xiaohei.tooth)

# 测试通过对象修改值

wangcai = Dog()
xiaohei = Dog()
print(Dog)
wangcai.tooth = 200
print(wangcai.tooth)
print(xiaohei.tooth)
