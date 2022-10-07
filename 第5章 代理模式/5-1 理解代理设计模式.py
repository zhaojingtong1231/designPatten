"""
  -*- encoding: utf-8 -*-
  @Author: zhaojingtong
  @Time  : 2022/10/07 8:50
  @Email: 2665109868@qq.com
  @function
    内容：为其他对象提供一种代理以控制对这个对象的访问
    应用场景：
        -远程代理：为远程的对象提供代理
        -虚代理：根据需要创建很大的对象
        -保护代理：控制对原始对象的访问，用于对象有不同访问权限时
        -智能代理：在访问对象时插入其他操作
    角色：
        -抽象实体（Subject)
        -实体(RealSubject)
        -代理（Proxy）：
    代理设计模式主要完成以下工作：
        -为其他对象提供了一个代理，从而实现了对原始对象的访问控制
        -可以用作一个层或接口，以支持分布式访问
        -通过增加代理，保护真正的组件不受意外的影响
"""


# 代理
class Actor(object):
    def __init__(self):
        self.isBusy = False

    def occupied(self):
        self.isBusy = True
        print(type(self).__name__, "is occupied with current movie")

    def available(self):
        self.isBusy = False
        print(type(self).__name__, "is free for the movie")

    def getStatus(self):
        return self.isBusy


class Agent(object):
    def __init__(self):
        self.principal = None

    def work(self):
        self.actor = Actor()
        if self.actor.getStatus():
            self.actor.occupied()
        else:
            self.actor.available()


if __name__ == '__main__':
    r = Agent()
    r.work()
