"""
  -*- ecoding: utf-8 -*-
  @Author: zhaojingtong
  @Time  : 2022/10/04 16:05
  @Email: 2665109868@qq.com
  @function
    1.封装 -对象的行为对于外部世界来说是不可见的
          -客户端不能通过直接操作来改变对象的内部状态
    2.多态 -对象根据输入参数提供方法的不同实现
          -不同类型的对象可以使用相同的接口
    3.继承 -继承表示一个类可以继承父类的功能
          -继承被描述为一个重用基类中定义的功能并允许对原始软件的实现进行独立扩展的选项
          -继承可以利用不同类的对象之间的关系简历层结构，python支持多重继承

"""


class Person(object):

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def get_person(self):
        return "<Person {%s,%s}>"%(self.name,self.age)


p = Person('John',32)
print("Type of Object:",type(p),"Memory Address:",id(p))

