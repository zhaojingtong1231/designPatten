"""
  -*- encoding: utf-8 -*-
  @Author: zhaojingtong
  @Time  : 2022/10/08 18:26
  @Email: 2665109868@qq.com
  @function
    内容：定义一个操作中的算法的骨架，而将一些步骤延迟到子类中。模板方法使得子类可以不改变
        一个算法的结构即可重定义该算法的某些特定步骤
    角色：
        -抽象类（AbstractClass):定义抽象的原子操作；实现一个模板方法作为算法的骨架
        -具体类（ConcreteClass）：实现原子操作
    适用场景：
        -一次性实现一个算法的不变的部分
        -各个子类中的公共行为应该被提取出来并集中到一个公共父类中以避免代码重复
        -控制子类扩展

"""

from abc import ABCMeta, abstractmethod


class Compiler(metaclass=ABCMeta):
    @abstractmethod
    def collectSource(self):
        pass

    @abstractmethod
    def compileToObject(self):
        pass

    @abstractmethod
    def run(self):
        pass

    def compileAndRun(self):
        self.collectSource()
        self.compileToObject()
        self.run()


class iOSCompiler(Compiler):
    def collectSource(self):
        print("Collecting Swift Source Code")

    def compileToObject(self):
        print("Compiling Swift code to LLVM bitcode")

    def run(self):
        print("Program runing on runtime environment")


iOS = iOSCompiler()
iOS.compileAndRun()
