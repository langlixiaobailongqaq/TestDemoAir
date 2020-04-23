# -*- encoding=utf8 -*-

__author__ = "Admin"
from airtest.core.api import *
auto_setup(__file__)
import poco   # poco库
from airtest.core.android.android import Android
import os
import time

from poco.drivers.unity3d import UnityPoco  # 导入并初始化U3d
poco = UnityPoco()
import unittest

"""
启动模拟器和APP
"""


class Test_StartSimulator(unittest.TestCase):
	def setUp(self):
		from poco.drivers.unity3d import UnityPoco  # 导入并初始化U3d
		poco = UnityPoco()
		# os.system(r"start D:\yeshen\Nox\bin\Nox.exe")  # 启动夜神模拟器
		# devs = connect_device(
		# 	"Android://127.0.0.1:5037/127.0.0.1:62001?cap_method=JAVACAP&&ori_method=ADBORI&&touch_method=ADBTOUCH")  # 连接夜神模拟器
		# time.sleep(10)
		# start_app('com.kaixinyule.kaixingame', activity=None)  # 启动待测app
		# time.sleep(15)
		pass

	def test_assert(self):
		# from poco.drivers.unity3d import UnityPoco  # 导入并初始化U3d
		# poco = UnityPoco()
		# assert poco("_Button_WeixinLogon").get_name() == "_Button_WeixinLogon"
		# # login = poco("_Button_WeixinLogon").get_name()
		# # self.assertEqual(login, "_Button_WeixinLogon")
		# print("*******************", "成功启动模拟器,APP")
		pass


	def tearDown(self):
		pass

