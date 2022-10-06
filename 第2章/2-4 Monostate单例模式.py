"""
  -*- ecoding: utf-8 -*-
  @Author: zhaojingtong
  @Time  : 2022/10/05 11:00
  @Email: 2665109868@qq.com
  @function 实现所有对象共享相同状态
"""


# class Borg:
#     __shared_state = {"1": "2"}
#
#     def __init__(self):
#         self.x = 1
#         self.__dict__ = self.__shared_state
#         pass


# 通过修改__new__方法本身来实现Borg模式。__new__方法是用来创建对象的实例的
class Borg(object):
    __share_state = {"1":"2"}

    def __new__(cls, *args, **kwargs):
        obj = super(Borg, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.__share_state
        return obj


b = Borg()
b1 = Borg()
b.x = 4

print("Borg Object 'b': ", b)
print("Borg Object 'b1': ", b1)
print("Object State 'b': ", b.__dict__)
print("Object State ' b1': ", b1.__dict__)
