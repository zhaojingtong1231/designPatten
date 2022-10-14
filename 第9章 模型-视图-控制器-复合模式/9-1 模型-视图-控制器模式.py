"""
  -*- encoding: utf-8 -*-
  @Author: zhaojingtong
  @Time  : 2022/10/14 8:21
  @Email: 2665109868@qq.com
  @function
    角色：
        -模型：声明一个存储和操作数据的类
        -视图：声明一个类来构建用户界面和显示数据
        -控制器：声明一个连接模型和视图的类
        -客户端：声明一个类，根据某些操作来获得某些结果

"""


class Model(object):
    services = {
        'email': {'number': 1000, 'price': 2, },
        'sms': {'number': 1000, 'price': 10, },
        'voice': {'number': 1000, 'price': 15, }
    }


class View(object):
    def list_services(self, services):
        for svc in services:
            print(svc, ' ')

    def list_pricing(self, services):
        for svc in services:
            print("For ", Model.services[svc]['number'],
                  svc, "message you pay $",
                  Model.services[svc]['price'])


class Controller(object):
    def __init__(self):
        self.model = Model()
        self.view = View()

    def get_services(self):
        services = self.model.services.keys()
        return (self.view.list_services(services))

    def get_pricing(self):
        services = self.model.services.keys()
        return (self.view.list_pricing(services))


class Client(object):
    controller = Controller()
    print("Services Provided:")
    controller.get_services()
    print("Pricing for Services:")
    controller.get_pricing()
