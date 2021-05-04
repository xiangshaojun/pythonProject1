# 属性：表示类的特征
class Washer():
    def washer(self):
        print('洗衣服')


haier = Washer()
# 添加属性： 对象.属性=值
haier.height = 500
haier.width = 300

# 获取属性
print(f'洗衣机的高度是{haier.hight}')
print(f'洗衣机的宽度是{haier.width}')