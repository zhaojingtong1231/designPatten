"""
  -*- encoding: utf-8 -*-
  @Author: zhaojingtong
  @Time  : 2022/10/07 16:38
  @Email: 2665109868@qq.com
  @function 属于行为型模式
    内容：定义对象间的一种一对多的依赖关系，当一个对象的状态发生改变时，所有依赖于它的对象
        都得到通知并被自动更新。观察者模式又称“发布-订阅”模式

    角色：
        -抽象主题（subject）
        -具体主题（ConcreteSubject）--发布者
        -抽象观察者（Observer）
        -具体观察者（ConcreteObserver）--订阅者

"""


# 发布者
class Subject:
    def __init__(self):
        self.__observers = []

    def register(self, observer):
        self.__observers.append(observer)

    def notifyAll(self, *args, **kwargs):
        for observer in self.__observers:
            observer.notify(self, *args, **kwargs)


# 订阅者
class Observer1():
    def __init__(self, subject):
        subject.register(self)

    def notify(self, subject, *args):
        print(type(self).__name__, ':: Got ', args, "From ", subject)


class Observer2:
    def __init__(self, subject):
        subject.register(self)

    def notify(self, subject, *args):
        print(type(self).__name__, ':: Got ', args, "From ", subject)


subject = Subject()
observer1 = Observer1(subject)
observer2 = Observer2(subject)
subject.notifyAll('notification')