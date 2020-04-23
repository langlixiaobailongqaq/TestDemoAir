# -*- encoding=utf8 -*-
# __author__ = "Admin"

import poco   # poco库
import unittest  # unittest库本库
from airtest.core.api import *   # airtest的官方库
from airtest.core.android.android import Android
import os
import time
from common.Print import *

"""启动夜神模拟器"""


class Test_1StartSimulator(unittest.TestCase):
	def setUp(self):
		pass


	def test_1assert(self):
		try:
			# os.system(r"start D:\yeshen\Nox\bin\Nox_1")  # 启动夜神模拟器
			os.system(r"start C:\Users\Admin\Desktop\start_2.bat")
			time.sleep(5)
		except:
			print("夜神模拟器已启动")
		devs = connect_device(
			"Android://127.0.0.1:5037/127.0.0.1:62025?cap_method=JAVACAP&&ori_method=ADBORI&&touch_method=ADBTOUCH")  # 连接夜神模拟器
		time.sleep(10)
		start_app('com.kaixinyule.kaixingame', activity=None)  # 启动待测app     # 获取包名 aapt dump badging test.apk     查看端口 netstat -ano
		time.sleep(15)

		from poco.drivers.unity3d import UnityPoco  # 导入并初始化U3d
		poco = UnityPoco()
		# 测试当前页面微信登录UI控件是否存在
		invisible_obj = poco('_Button_WeixinLogon', type='Button')
		Pr.print(invisible_obj.exists())
		if invisible_obj.exists() == True:
			Pr.print("*******************", "成功启动模拟器,APP")
		else:
			Pr.print("*******************", "启动模拟器失败,APP")
		# assert poco("_Button_WeixinLogon").get_name() == "_Button_WeixinLogon"
		# login = poco("_Button_WeixinLogon").get_name()
		# self.assertEqual(login, "_Button_WeixinLogon")


	def tearDown(self):
		pass


def main():
	query = Test_1StartSimulator()
	query.test_1assert()

if __name__ == '__main__':
	main()


