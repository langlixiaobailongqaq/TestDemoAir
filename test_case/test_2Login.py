# -*- encoding=utf8 -*-
import unittest
from airtest.core.api import *
from airtest.core.android.android import Android
import os
import pymysql
import time
import common.test_mysql as mysql
import test_case.test_1StartSimulator
from common.Print import *
"""
注册，登录
"""

class Test_2Login(unittest.TestCase):
	GAMEID = ''

	def setUp(self):
		# Test_1StartSimulator()
		pass

	"""验证版本号"""
	def test_1version(self):
		from poco.drivers.unity3d import UnityPoco  # 导入并初始化U3d
		poco = UnityPoco()
		time.sleep(2)
		# 版本号-测试服
		version = "1-4-000-000"
		# version = "1-1-100-100"
		version1 = poco("_Text_Version").get_text()
		# 版本号-正式服
		# Version = "1-3-002-001"
		# 验证版本号
		time.sleep(2)
		self.assertEqual(version, version1)
		time.sleep(1)
		# assert poco("_Text_Version").get_text() == version1 == version, "版本验证错误"
		Pr.print("*******************", "版本号验证成功！")

	"""账号登录"""
	def test_2login(self):
		from poco.drivers.unity3d import UnityPoco  # 导入并初始化U3d
		poco = UnityPoco()
		time.sleep(2)
		# 账号登录
		name = "2322"
		password = "2322"
		button_PassPort = poco("_Button_PassPort").get_name()
		poco(button_PassPort).click()
		# poco("_Button_PassPort").click()
		# poco("_Button_WeixinLogon").child("_Button_PassPort").click()
		time.sleep(1)

		poco(text="请输入您的账号").click()
		poco("_InputField_PassPort").set_text(name)
		time.sleep(1)
		poco("Text").click()
		poco(text="请输入您的密码").click()
		poco("_InputField_PassWord").set_text(password)
		poco("Text").click()
		poco("_Button_ConfirmLogin").click()
		time.sleep(6)
		Pr.print("*******************", "登录成功！")


	"""微信登录"""
	def test_3wexinLogin(self):
		# from poco.drivers.unity3d import UnityPoco  # 导入并初始化U3d
		# poco = UnityPoco()
		# time.sleep(5)
		# # 微信登录
		# poco("_Button_WeixinLogon").click()
		# time.sleep(5)
		# print("*******************", "登录成功！")
		pass


	"""用户基本信息"""
	def test_4userInfo(self):
		global GAMEID

		from poco.drivers.unity3d import UnityPoco  # 导入并初始化U3d
		poco = UnityPoco()
		# Test_2Login.GAMEID = poco("_Text_Level").get_text()
		GAMEID = poco("_Text_Level").get_text()    # GameID（游戏ID）
		Pr.print(GAMEID)
		Test_2Login.GAMEID = GAMEID
		Pr.print(Test_2Login.GAMEID)

		# mysql.conn  # 调用初始化连接数据库方法
		# mysql.test_query1()
		# Pr.print(mysql.QUERYRESULTS)
		# if int(Test_2Login.GAMEID) == int(mysql.QUERYRESULTS):
		# 	Pr.print("93行,数据库GameID验证成功")


		name = poco("_Text_Name").get_text()            # 昵称
		Pr.print(name)
		happyBean = poco("_Text_Score").get_text()     # 开心豆
		Pr.print(happyBean)
		redEnvelopes = poco("_Text_Meili").get_text()   # 红包券
		Pr.print(redEnvelopes)
		Pr.print("*******************", "个人信息获取成功！")
		# if Test_Mysql.test_member2().it1[1] == 3:
		# 	print("玩家为金钻")

	def tearDown(self):
		pass


mysql = mysql.Test_Mysql()
# mysql.conn      # 调用初始化连接数据库方法
# mysql.test_query1()
# print(mysql.QUERYRESULTS)


# from poco.drivers.unity3d import UnityPoco  # 导入并初始化U3d
# poco = UnityPoco()
# userInfo = Test_2Login()
# userInfo.test_1version()
# userInfo.test_2login()
# userInfo.test_3wexinLogin()
# userInfo.test_4userInfo()


def main():
	query = Test_2Login()
	query.Test_2Login()
	pass

if __name__ == '__main__':
	main()





