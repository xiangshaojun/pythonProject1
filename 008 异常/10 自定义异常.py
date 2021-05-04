class ShortInputError(Exception):
    def __init__(self, length, min_len):
        self.length = length
        self.min_len = min_len

    def __str__(self):
        return f'您输入的长度是{self.length},最小长度不能少于{self.min_len}'


def main():
    try:
        password = input('请输入密码；')

        if len(password) < 5:
            raise ShortInputError(len(password), 5)
    except Exception as e:
        print(e)
    else:
        print('输入成功')


main()
