"""
  -*- encoding: utf-8 -*-
  @Author: zhaojingtong
  @Time  : 2022/10/14 17:17
  @Email: 2665109868@qq.com
  @function
"""
from abc import abstractmethod, ABCMeta


class State(metaclass=ABCMeta):
    @abstractmethod
    def doThis(self):
        pass


class StartState(State):
    def doThis(self):
        print("TV Switching ON..")


class StopState(State):
    def doThis(self):
        print("TV Switching OFF..")


class TVContext(State):
    def __init__(self):
        self.state = None

    def getState(self):
        return self.state

    def setState(self, state):
        self.state = state

    def doThis(self):
        self.state.doThis()


context = TVContext()
context.getState()

start = StartState()
stop = StopState()

context.setState(start)
context.doThis()
