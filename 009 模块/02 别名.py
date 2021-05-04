# 对模块设置别名 import 模块 as 别名
import time as tt

tt.sleep(2)
print('hello')

# 对模块中的功能设置别名 from 模块名 import 功能 as 功能别名

from time import sleep as ss

ss(2)
print('hello')
