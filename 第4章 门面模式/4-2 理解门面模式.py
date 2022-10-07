"""
  -*- encoding: utf-8 -*-
  @Author: zhaojingtong
  @Time  : 2022/10/06 22:52
  @Email: 2665109868@qq.com
  @function
        内容：为子系统的一组接口提供一个一致的界面，门面模式定义了一个高层接
            口，这个接口使得这一子系统更加容易使用
            -促进了实现与多个客户端的解耦
        角色：
            -外观
            -子系统类
            -客户端
"""


# 外观
class EventManager(object):
    def __init__(self):
        print("Event Manager:: Let me talk to the folks\n")

    def arrange(self):
        # 预定酒店
        self.hotelier = Hotelier()
        self.hotelier.bookHotel()
        # 花卉装饰
        self.florist = Florist()
        self.florist.setFlowerRequirements()
        # 备办宴席者打交道，负责安排餐饮
        self.caterer = Caterer()
        self.caterer.setCuisine()
        # 安排婚礼音乐
        self.musician = Musician()
        self.musician.setMusicType()


# 子系统类
class Hotelier(object):
    def __init__(self):
        print("Arranging the Hotel for Marriage?? -- ")

    def _isAvailable(self):
        print("Is the Hotel free for the event on given day?")

    def bookHotel(self):
        if self._isAvailable():
            print("Registered the Booking\n\n")


class Florist(object):
    def __init__(self):
        print("Flower Decorations for the Event? --")

    def setFlowerRequirements(self):
        print("Carnations, Roses and Lilies would be used for Decorations\n\n")


class Caterer(object):
    def __init__(self):
        print("Food Arrangements for the Event -- ")

    def setCuisine(self):
        print("Chinese & Continental Cuisine to be served\n\n")


class Musician(object):
    def __init__(self):
        print("Musical Arrangements for the Marriage --")

    def setMusicType(self):
        print("Jazz and Classical will be played\n\n")


# 客户端
class You(object):
    def __init__(self):
        print("You:: Whoa! Marriage Arrangements??!!!")

    def askEventManager(self):
        print("You : Let's Contacy the Event Manager\n\n")
        em = EventManager()
        em.arrange()

    def __del__(self):
        print("You :: Thanks to Event Manager, all preparations done！Phew!")


you = You()
you.askEventManager()
