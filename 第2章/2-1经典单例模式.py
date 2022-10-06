# -*- encoding: utf-8 -*-
# @Author: zhaojingtong
# @Time  : 2022/10/05 10:19
# @Email: 2665109868@qq.com
# @function 实现经典的单例模式
# 单例模式：保证一个类只有一个实例，并提供一个访问它的全局访问点

"""
通过覆盖__new__方法来控制对象的创建。
"""


class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


s = Singleton()
print('Object created', s)
s1 = Singleton()
print('Object created', s1)
