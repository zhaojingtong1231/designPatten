"""
  -*- ecoding: utf-8 -*-
  @Author: zhaojingtong
  @Time  : 2022/10/06 15:35
  @Email: 2665109868@qq.com
  @function 简单工厂模式
    -不直接向客户端暴露对象创建的实现细节，而是通过一个工厂类来负责创建产品类的实例
    角色： 工厂角色，抽象产品角色，具体产品角色
    优点：
        -隐藏了对象创建的实现细节
        -客户端不需要修改代码
    缺点：
        -违反了单一职责原则，将创建逻辑集中到一个工厂类
        -当添加新产品时，需要修改工厂类代码，违反了开闭原则
"""

from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    @abstractmethod
    def do_say(self):
        pass


class Dog(Animal):
    def do_say(self):
        print("Bhow Bhow!!")


class Cat(Animal):
    def do_say(self):
        print("Meow Meow!!")


# forest factory defined
class ForestFactory(object):
    def make_sound(self, object_type):
        return eval(object_type)().do_say()


#client code

if __name__ == '__main__':
    ff = ForestFactory()
    animal = input("Which animal should make_sound Dog or Cat?")
    ff.make_sound(animal)