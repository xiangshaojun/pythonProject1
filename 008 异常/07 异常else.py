# else 没有异常执行的代码
try:
    print(1)
except Exception as result:
    print(result)
else:
    print('else,表示没有异常时执行的代码！')