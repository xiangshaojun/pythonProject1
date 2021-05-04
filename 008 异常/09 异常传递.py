# 通过Ctrl+C终止程序执行，传递异常
import time
try:
    f = open('test.txt')
    try:
        while True:
            con = f.readline()
            if len(con) == 0:
                break
            print(con, end='')
            time.sleep(1)
    except:
        # 当按下Ctrl+C时，抛出异常
        print('程序被终止')
except Exception as e:
    print(e)