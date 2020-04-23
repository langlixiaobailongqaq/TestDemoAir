
import poco   # poco库
import unittest # unittest库本库
from airtest.core.api import *   # airtest的官方库
from airtest.core.android.android import Android
import os
import time
from common.test_mysql import *
from common.Print import *

"""大厅弹窗: 
	1.新手：新手红包-签到-红包场-礼包活动(母亲节礼包)/每日礼包
	2.未签到老用户：签到-红包场-礼包活动(母亲节礼包)/每日礼包
	3.已签到老用户：红包场-礼包活动(母亲节礼包)/每日礼包
	4.已签到,已购买完每日礼包,老用户：红包场-礼包活动(母亲节礼包)/月卡
	5.已签到,已购买完每日礼包,月卡,老用户：红包场-礼包活动(母亲节礼包)/商城
	
	"""


class Test_3LobbyWindos(unittest.TestCase):
	def setUp(self):
		pass

	"""1.新手"""
	def test_1novice(self):
		from poco.drivers.unity3d import UnityPoco  # 导入并初始化U3d
		poco = UnityPoco()
		try:
			exists(Template(r"NoviceRedEnvelope.png"))
			poco("Image (5)").click()
			Pr.print("领取新手礼包")
			poco("_Button_Back").click()
			Pr.print("关闭新手礼包页面")
		except:
			# if Test_Mysql.test_query1().row[-1] == 0:  # 查询数据库，查询新用户字段是否为0
			Pr.print("该用户不是新注册用户")

		Button_QianDao = poco('_Button_QianDao', type='Button')
		# print(Button_QianDao.exists())  # => False. This UI is not visible to user.
		if Button_QianDao.exists() == True:
			poco("_Button_Close").click()  # 签到弹窗
			Pr.print("关闭签到弹窗")
		else:
			Pr.print("无签到弹窗")

		Button_MeKnow = poco("_Button_MeKnow").attr('texture')
		if Button_MeKnow == "anniu_zhidaole":
			poco("_Button_Close").click()  # 红包场活动弹窗
			Pr.print("关闭红包场活动弹窗")
		else:
			Pr.print("无红包场活动弹窗")


		# try:
		# 	poco("_Button_Back").click()  # 母亲节礼包（活动礼包）弹窗
		# 	Pr.print("关闭母亲节礼包（活动礼包）弹窗")
		# except:
		# 	Pr.print("无母亲节礼包（活动礼包）弹窗")

		# try:
		# 	libao = poco('_Text_Tips').get_text()
		# 	libao1 = "每日礼包每种面额只能购买一次"
		# 	self.assertEqual(libao, libao1)
		# 	poco("_Button_Back").click()  # 关闭每日礼包弹窗
		# 	Pr.print("关闭每日礼包弹窗")
		# except:
		# 	Pr.print("无每日礼包弹窗")

		Button_Tips = poco('_Button_Tips', type='Button')
		# print(Button_QianDao.exists())  # => False. This UI is not visible to user.
		if Button_Tips.exists() == True:
			poco("_Button_Back").click()  # 每日礼包弹窗
			Pr.print("关闭每日礼包弹窗")
		else:
			Pr.print("无每日礼包弹窗")


		facaijin = poco('_Text_Tips (1) ' ).get_text()
		facaijin1 = "开心豆少于1000才可以领取发财金"
		self.assertEqual(facaijin, facaijin1)
		try:
			poco("_Button_Exit").click()
			Pr.print("关闭发财金弹窗")
		except:
			Pr.print("该用户开心豆加银行开心豆大于1000")


	# """未签到老用户"""
	# def test_2noSignIn(self):
	# 	from poco.drivers.unity3d import UnityPoco  # 导入并初始化U3d
	# 	poco = UnityPoco()
	# 	try:
	# 		poco("_Button_Close").click()    # 签到弹窗
	# 		Pr.print("关闭签到弹窗")
	# 		poco("_Button_Close").click()   # 红包场活动弹窗
	# 		Pr.print("关闭红包场活动弹窗")
	# 	except:
	# 		pass
	#
	# 	try:
	# 		poco("_Button_Back").click()  # 母亲节礼包（活动礼包）弹窗
	# 		Pr.print("关闭母亲节礼包（活动礼包）弹窗")
	# 	except:
	# 		pass
	#
	# 	try:
	# 		poco("_Button_Back").click()  # 关闭每日礼包弹窗
	# 		Pr.print("关闭每日礼包弹窗")
	# 	except:
	# 		pass
	#
	# """已签到老用户"""
	# def test_3checkin(self):
	# 	from poco.drivers.unity3d import UnityPoco  # 导入并初始化U3d
	# 	poco = UnityPoco()
	# 	try:
	# 		poco("_Button_Close").click()  # 红包场活动弹窗
	# 		Pr.print("关闭红包场活动弹窗")
	# 	except:
	# 		pass
	# 	try:
	# 		poco("_Button_Back").click()  # 母亲节礼包（活动礼包）弹窗
	# 		Pr.print("关闭母亲节礼包（活动礼包）弹窗")
	# 	except:
	# 		pass
	# 	try:
	# 		poco("_Button_Back").click()  # 关闭每日礼包弹窗
	# 		Pr.print("关闭每日礼包弹窗")
	# 	except:
	# 		pass
	#
	# """已签到,已购买完每日礼包,老用户"""
	# def test_4purchasedDaily(self):
	# 	from poco.drivers.unity3d import UnityPoco  # 导入并初始化U3d
	# 	poco = UnityPoco()
	# 	try:
	# 		poco("_Button_Close").click()  # 红包场活动弹窗
	# 		Pr.print("关闭红包场活动弹窗")
	# 	except:
	# 		pass
	# 	try:
	# 		poco("_Button_Back").click()  # 母亲节礼包（活动礼包）弹窗
	# 		Pr.print("关闭母亲节礼包（活动礼包）弹窗")
	# 	except:
	# 		pass
	# 	try:
	# 		poco("_Button_Back").click()  # 关闭月卡弹窗
	# 		Pr.print("关闭月卡弹窗")
	# 	except:
	# 		pass
	#
	# """已签到, 已购买完每日礼包, 月卡, 老用户"""
	# def test_5purchasMonthly(self):
	# 	from poco.drivers.unity3d import UnityPoco  # 导入并初始化U3d
	# 	poco = UnityPoco()
	# 	try:
	# 		poco("_Button_Close").click()  # 红包场活动弹窗
	# 		Pr.print("关闭红包场活动弹窗")
	# 	except:
	# 		pass
	# 	try:
	# 		poco("_Button_Back").click()  # 母亲节礼包（活动礼包）弹窗
	# 		Pr.print("关闭母亲节礼包（活动礼包）弹窗")
	# 	except:
	# 		pass
	# 	try:
	# 		poco("_Button_Back").click()  # 关闭商城弹窗
	# 		Pr.print("关闭商城卡弹窗")
	# 	except:
	# 		pass

	def tearDown(self):
		pass
