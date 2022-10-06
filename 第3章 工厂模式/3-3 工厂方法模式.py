"""
  -*- encoding: utf-8 -*-
  @Author: zhaojingtong
  @Time  : 2022/10/06 16:08
  @Email: 2665109868@qq.com
  @function
    -定义一个用于创建对象的接口（工厂接口），让子类决定实例化哪一个产品类
    角色：
        -抽象工厂角色
        -具体工厂角色
        -抽象产品角色
        -具体产品角色

    优点：
        -具有更大的灵活性，使得代码更加通用
        -松耦合，创建对象的代码与使用它的代码是分开的。客户端完全不需要关心要传递哪些参数以及
        需要实例化哪些类
"""
from abc import ABCMeta, abstractmethod


class Section(metaclass=ABCMeta):
    @abstractmethod
    def describe(self):
        pass


class PersonalSection(Section):
    def describe(self):
        print("Personal Section")


class AlbumSection(Section):
    def describe(self):
        print("Album Section")


class PatentSection(Section):
    def describe(self):
        print("Patent Section")


class PublicationSection(Section):
    def describe(self):
        print("Publication Section")


class Profile(metaclass=ABCMeta):
    def __init__(self):
        self.sections = []
        self.createProfile()

    @abstractmethod
    def createProfile(self):
        pass

    def getSections(self):
        return self.sections

    def addSections(self, section):
        self.sections.append(section)


class linkedin(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(PatentSection())
        self.addSections(PublicationSection())
class facebook(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(AlbumSection())

if __name__ == '__main__':
    profile_type = input("Which Profile you'd like to create?[LinkedIn or FaceBook]")
    profile = eval(profile_type.lower())()
    print("Create Profile..",type(profile).__name__)
    print("Profile has section -- ",profile.getSections())
