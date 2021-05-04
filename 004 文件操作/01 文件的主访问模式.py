# read
# file = open('1.txt', 'r')   # 以只读的方式打开1.txt文件，如果文件不存在报错
# print(file.read())    # 读取1.txt文件中的内容

# write
# file = open('1.txt', 'w')  # 以写的方式打开1.txt文件，如果文件不存在则新建1.txt文件；覆盖源文件中的内容
# con = file.write('dafadfadf')  # 写入数据，原有数据覆盖
# print(con)


file=open('1.txt', 'a')   # 以写的方式打开1.txt文件，如果文件不存在则新建；不覆盖文件中的内容
con = file.write('dsfasdadasdf232fad')
print(con)
file.close()

