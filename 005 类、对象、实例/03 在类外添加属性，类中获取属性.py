class Washer():
    def washer(self):
        print('洗衣服')
        print(f'洗衣机的高度是{self.height}')
        print(f'洗衣机的宽度是{self.width}')


haier = Washer()
# 添加属性： 对象.属性=值
haier.height = 500
haier.width = 300
haier.washer()
# 获取属性
