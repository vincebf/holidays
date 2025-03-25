class Person:
    def __init__(self, news_name, weight):
        # self.属性 = 形参
        self.name = news_name
        self.weight = weight
        print("%s 爱跑步" % news_name)

    def __del__(self):
        print("%s 走了" % self.name)

    def __str__(self):
        return "我是学生 %s" % self.name

    def eat(self):
        self.weight += 1
        print("%s 胖了,现在是 %0.2f 公斤" % (self.name, self.weight))
        return self.weight

    def run(self):
        self.weight -= 0.5
        print("%s 瘦了,现在是 %0.2f 公斤" % (self.name, self.weight))


student = Person(news_name="小明", weight=70)
student.eat()
student.run()


class Cat1:
    def __init__(self, news_name):
        self.name = news_name
        print("%s 爱吃鱼" % news_name)

    def __del__(self):
        print("%s 我去了" % self.name)

    def __str__(self):
        return "我是小猫 %s" % self.name


# tom = Cat1("tom")
# print(tom)
# print("*" * 50, "\n")


class Cat:
    """
    这是一个猫类
    """

    def __init__(self, new_name):
        print("初始化方法")
        self.name = new_name

    def eat(self):
        print("%s 爱吃🐟" % self.name)

    def drink(self):
        print("%s 爱喝水" % self.name)


# tom = Cat("Tom")
# print(tom.name)
# tom.eat()
# tom.drink()
# lazy_cat = Cat("大懒猫")
# lazy_cat.eat()
# lazy_cat.drink()
