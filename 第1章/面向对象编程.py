"""
  -*- ecoding: utf-8 -*-
  @Author: zhaojingtong
  @Time  : 2022/10/04 16:05
  @Email: 2665109868@qq.com
  @function
    1.封装 对象的行为对于外部世界来说是不可见的
"""


class Person(object):

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def get_person(self):
        return "<Person {%s,%s}>"%(self.name,self.age)


p = Person('John',32)
print("Type of Object:",type(p),"Memory Address:",id(p))

