# finally 表示无论是否异常都要执行的代码
try:
    f = open('test100.txt', 'r')
except Exception as e:
    f = open('test100.txt', 'w')
finally:
    f.close()
