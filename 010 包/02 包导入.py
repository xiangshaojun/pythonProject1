# 方法一
# import myPackage.my_module1
#
# myPackage.my_module1.info_print1()

# 方法二
# from 包名 import * ，使用这种方式导入时，必须在__init__.py 文件中设置 __all__列表

from myPackage import *

my_module1.info_print1()
