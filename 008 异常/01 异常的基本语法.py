# 基本语法
# try:
#     可能发生错误的代码
# except:
#     如果出现错误执行的代码

# 实例
try:
    f = open('test.txt', 'r')
except:
    f = open('test.txt', 'w')
