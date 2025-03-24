# coding=utf-8

# 以下是Python的关键字
import keyword
def print_keyword():
    print(keyword.kwlist)
# 加密
def print_encode():
    str = "Hello, 你好!"
    encoded_str = str.encode()  # 默认使用UTF-8编码
    print(encoded_str) 
    # 输出：b'Hello, \xe4\xbd\xa0\xe5\xa5\xbd!'

# 解密
def print_encode():
    str = b'Hello, \xe4\xbd\xa0\xe5\xa5\xbd!'
    decoded_str = str.decode()  # 默认使用UTF-8解码
    print(decoded_str)


