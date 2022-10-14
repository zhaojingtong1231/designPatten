"""
  -*- encoding: utf-8 -*-
  @Author: zhaojingtong
  @Time  : 2022/10/08 15:42
  @Email: 2665109868@qq.com
  @function
    角色：
        -Command:声明执行操作的接口
        -ConcreteCommand：将一个Receiver对象和一个操作绑定在一起
        -Client：创建ConcreteCommand对象并设定其接收者
        -Invoker（调用者）：要求ConcreteCommand执行这个请求
        -Receiver：知道如何实施与执行一个请求相关的操作

"""
from abc import ABCMeta, abstractmethod


class Command(metaclass=ABCMeta):
    def __init__(self, recv):
        self.recv = recv

    @abstractmethod
    def execute(self):
        pass


class ConcreteCommand(Command):
    def __init__(self, recv):
        self.recv = recv

    def execute(self):
        self.recv.action()


class Receiver:
    def action(self):
        print("Receiver Action")


class Invoker:
    def command(self, cmd):
        self.cmd = cmd

    def execute(self):
        self.cmd.execute()


if __name__ == '__main__':
    recv = Receiver()
    cmd = ConcreteCommand(recv)
    invoker = Invoker()
    invoker.command(cmd)
    invoker.execute()
