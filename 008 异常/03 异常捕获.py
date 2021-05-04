# try:
#   可能发生错误的代码
# except 异常类型:
#   如果捕获到该异常类型则执行代码

try:
    print(num)
except NameError:
    print('有错误')

# 如果尝试执行代码的异常类型和捕获的异常类型不一致，则无法捕获异常
# 一般try下面只放一行尝试执行的代码
try:
    print(1/0)
except NameError:
    print('有错误')