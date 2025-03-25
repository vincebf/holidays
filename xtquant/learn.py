# coding=utf-8

import keyword


# 以下是Python的关键字
def print_keyword():
    print(keyword.kwlist)


# 加密
def print_encode():
    str = "Hello, 你好!"
    encoded_str = str.encode()  # 默认使用UTF-8编码
    print(encoded_str)
    # 输出：b'Hello, \xe4\xbd\xa0\xe5\xa5\xbd!'
    print_decode(encoded_str)


# 解密
def print_decode(str):
    if str == "":
        str = b"Hello, \xe4\xbd\xa0\xe5\xa5\xbd!"
    decoded_str = str.decode()
    print(decoded_str)


# type查看数据类型
def print_type():
    vname = input("请输入用户名")
    print("Your name is", (vname))
    vname = "abc"
    print(type(vname))


# 格式化数据
def print_format():
    price = float(input("请输入苹果的价格"))
    weight = float(input("请输入苹果的重量"))
    money = price * weight
    print(money)
    # %.2f表示字符串保留小数点后两位  同理%6d表示整数位数保持6位 %06d表示位数不够用0填充
    print(
        "苹果单价是 %.2f 元/斤，%.2f 斤的苹果需要支付 %.2f元" % (price, weight, money)
    )


# for else 循环
def print_for():
    for num in range(10, 20):  # 迭代 10 到 20 (不包含) 之间的数字
        for i in range(2, num):  # 根据因子迭代
            if num % i == 0:  # 确定第一个因子
                j = num / i  # 计算第二个因子
                print("%d 等于 %d * %d" % (num, i, j))
                break  # 跳出当前循环
        else:  # 循环的 else 部分
            print("%d 是一个质数" % num)


if __name__ == "__main__":
    print_for()

    # str = b"Hello, \xe4\xbd\xa0\xe5\xa5\xbd!"
    # print_decode(str)
