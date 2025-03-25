class Cat:  # 创建一个类
    def eat(self):  # 定义一个eat方法
        print("小猫爱吃饭")

    def drink(self):
        print("小猫爱喝水")


if __name__ == "__main__":
    tmo = Cat()  # 实例化调用一个对象， 可以调用方法
    tmo.eat()
    tmo.drink()
