"""
  -*- encoding: utf-8 -*-
  @Author: zhaojingtong
  @Time  : 2022/10/07 9:58
  @Email: 2665109868@qq.com
  @function
"""
from abc import ABCMeta, abstractmethod


# 抽象实体
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def do_pay(self):
        pass


# 实体
class Bank(Payment):
    def __init__(self):
        self.card = None
        self.account = None

    def __getAccount(self):
        self.account = self.card
        return self.account

    def __hasFunds(self):
        print("Bank:: Checking if Account", self.__getAccount(), "has enough funds")
        return True

    def setCard(self, card):
        self.card = card

    def do_pay(self):
        if self.__hasFunds():
            print("Bank:: Paying the merchant")
            return True
        else:
            print("Bank:: Sorry, not enough funds!")
            return False


# 代理
class DebitCard(Payment):
    def __init__(self):
        self.bank = Bank()

    def do_pay(self):
        card = input("Proxy:: Punch in Card Number: ")
        self.bank.setCard(card)
        return self.bank.do_pay()


# 客户端
class You:
    def __init__(self):
        print("You:: Lets buy the Denim Shirt")
        self.debitCard = DebitCard()
        self.isPurchased = None

    def make_payment(self):
        self.isPurchased = self.debitCard.do_pay()

    def __del__(self):
        if self.isPurchased:
            print("You:: Wow! Denim shirt is Mine :-)")
        else:
            print("You: I should earn more:(")


you = You()
you.make_payment()
