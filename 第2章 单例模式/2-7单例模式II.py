"""
  -*- ecoding: utf-8 -*-
  @Author: zhaojingtong
  @Time  : 2022/10/06 12:56
  @Email: 2665109868@qq.com
  @function 单例模式应用：基础设施提供运行状态监控服务
"""


class HealthCheck:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not HealthCheck._instance:
            HealthCheck._instance = super(HealthCheck, cls).__new__(cls, *args, **kwargs)
        return HealthCheck._instance

    def __init__(self):
        self._servers = []

    def addServer(self):
        self._servers.append("server 1")
        self._servers.append("server 2")
        self._servers.append("server 3")
        self._servers.append("server 4")

    def changeServer(self):
        self._servers.pop()
        self._servers.append("server 5")


hc1 = HealthCheck()
hc2 = HealthCheck()

hc1.addServer()
print("Schedule health check for servers (1)...")

for i in range(4):
    print("Checking ", hc1._servers[i])
hc2.changeServer()
print("Schedule health check for servers (2)...")
for i in range(4):
    print("Checking ", hc2._servers[i])
#输出结果
"""
Schedule health check for servers (1)...
Checking  server 1
Checking  server 2
Checking  server 3
Checking  server 4
Schedule health check for servers (2)...
Checking  server 1
Checking  server 2
Checking  server 3
Checking  server 5
"""
