# def testA(a, b):
#     return a + b

# 当模块中包含__all__时，通过from 模块 import * 导入模块时，只能导入列表中的对应功能
__all__ = ['testA']


def testA():
    print('testA')


def testB():
    print('testB')


# 测试模块
# if __name__ == '__main__':
    # print(testA(1, 2))
