# 输入需要备份的文件名
filename = input('请输入文件名：')

# 生成新的文件名：filename_backup

index = filename.rfind('.')
if index > 0:
    new_filename = filename[:index] + '_backup' + filename[index:]
    # 拷贝文件
    oldf = open('1.txt', 'rb')
    newf = open(new_filename, 'wb')
    while True:
        con = oldf.read(1024)
        if len(con) == 0:
            break
        else:
            newf.write(con)
    oldf.close()
    newf.close()
else:
    print('输入的文件名无效！')
