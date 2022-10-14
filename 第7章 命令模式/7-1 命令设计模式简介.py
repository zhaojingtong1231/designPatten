"""
  -*- encoding: utf-8 -*-
  @Author: zhaojingtong
  @Time  : 2022/10/08 15:23
  @Email: 2665109868@qq.com
  @function
    内容：是一种行为设计模式，其中对象用于封装在完成一项操作时
        或在触发一个事件时所需的全部信息。信息包含：
            -方法名称；
            -拥有方法的对象；
            -方法参数的值

"""

class Wizard():
    def __init__(self, src, rootdir):
        self.choices = []
        self.rootdir = rootdir
        self.src = src

    def preferences(self, command):
        self.choices.append(command)

    def execute(self):
        for choice in self.choices:
            if list(choice.values())[0]:
                print("Copying binaries --", self.src, " to ", self.rootdir)
            else:
                print("No Operation")


if __name__ == '__main__':
    # client code
    wizard = Wizard('python3.5.gzip', '/usr/bin')
    # Users chooses to install python only
    wizard.preferences({'python':True})
    wizard.preferences({'java':False})
    wizard.execute()

