card_list = []


def show_menu():
    """显示菜单"""
    print("*" * 100)
    print(
        """
    欢迎使用[名片管理系统] V1.0\n
    1.新建名片\n
    2.显示全部\n
    3.查询名片\n

    0.退出系统
    """
    )
    print("*" * 100)


def add_menu():
    """新增名片"""
    print("新增名片")

    # 1.提示用户输入名片的详细信息
    name = input("请添加名片姓名:")
    QQ = input("请添加名片QQ:")
    iphone = input("请添加名片电话:")
    email = input("请添加名片邮箱:")

    # 2.使用用户输入的信息建立一个名片字典
    card_dict = {"name": name, "QQ": QQ, "iphone": iphone, "email": email}

    # 3.将名片字典添加到列表中
    card_list.append(card_dict)
    print(card_list)

    # 4.提示用户添加成功
    print("名片添加成功")


def show_all():
    """显示全部名片"""
    print("_" * 50)
    print("显示全部名片")
    if len(card_list) == 0:
        print("当前没有任何名片记录，请使用新增功能添加名片")
        # return 可以返回一个函数的执行结果
        # 下方的代码不会被执行
        # 如果 return 后面没有任何的内容，表示会返回到调用函数的位置继续执行
        # 并且不返回任何的结果
        return
    # 打印表头
    for name in ["姓名", "QQ", "手机号", "邮箱"]:
        print(name, end="\t\t")
    print("")
    # 循环遍历输出字典信息
    for card_dict in card_list:
        print(
            "%s\t\t%s\t\t%s\t\t%s"
            % (
                card_dict["name"],
                card_dict["QQ"],
                card_dict["iphone"],
                card_dict["email"],
            )
        )


def search_card():
    """搜索名片"""
    search_key = input("请输入要搜索的关键字:")
    for card_dict in card_list:
        for key in card_dict:
            if card_dict[key] == search_key:
                print("找到 %s 的相关信息了" % search_key)
                for name in ["姓名", "QQ", "手机号", "邮箱"]:
                    print(name, end="\t\t")
                print("")
                # 循环遍历输出字典信息

                print(
                    "%s\t\t%s\t\t%s\t\t%s"
                    % (
                        card_dict["name"],
                        card_dict["QQ"],
                        card_dict["iphone"],
                        card_dict["email"],
                    )
                )
                deal_card(card_dict)
                break
    else:
        print("没有找到 %s" % search_key)

    print("搜索名片")


def deal_card(find_dict):
    # while True:
    num_card = int(input("请选择功能序号：1.修改 2.删除 0.返回上级菜单 :"))
    if num_card == 1:
        find_dict["name"] = input_card_info(find_dict["name"], "修改名片姓名:")
        find_dict["QQ"] = input_card_info(find_dict["QQ"], "修改名片QQ:")
        find_dict["iphone"] = input_card_info(find_dict["iphone"], "修改名片电话:")
        find_dict["email"] = input_card_info(find_dict["email"], "修改名片邮箱:")
        # break
    elif num_card == 2:
        card_list.remove(find_dict)
        # break
    elif num_card == 0:
        # break
        pass
    else:
        print("输入有误，请重新输入")
        # break


def input_card_info(dict_value, tip):
    result_str = input(tip)
    if len(dict_value) > 0:
        return result_str
    else:
        return dict_value
