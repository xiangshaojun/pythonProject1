class Washer():
    def __init__(self, height, width):  # 魔法方法,在创建一个对象时默认被调用，不需要手动调用
        self.height = height
        self.width = width

    def washer(self):
        print('洗衣服')
        print(f'洗衣机的高度是{self.height}')
        print(f'洗衣机的宽度是{self.width}')


haier = Washer(500, 200)
haier.washer()
haier = Washer(800,300)
haier.washer()