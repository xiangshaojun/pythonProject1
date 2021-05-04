# __init__()在创建一个对象时默认被调用，不需要手动调用
# __init__(self) self参数不需要开发者传递参数，python解释器会自动把当前的对象引用传递过去

class Washer():
    def __init__(self):  # 魔法方法,在创建一个对象时默认被调用，不需要手动调用
        self.height = 800
        self.width = 500

    def washer(self):
        print('洗衣服')
        print(f'洗衣机的高度是{self.height}')
        print(f'洗衣机的宽度是{self.width}')


haier = Washer()
haier.washer()