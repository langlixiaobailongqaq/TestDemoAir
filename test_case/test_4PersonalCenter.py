
import poco   # poco库
import unittest # unittest库本库
from airtest.core.api import *   # airtest的官方库
from airtest.core.android.android import Android
import os
import time

from test_case.test_1StartSimulator import *
from test_case.test_2Login import *
from test_case.test_3LobbyWindow import *
from common.Print import *

"""
个人中心:
	1.基本信息：个人信息显示
				头像，头像框，昵称，ID显示.。。。
	2.等级，等级进度条
	3.贵族图标/等级
	4.会员/会员时间
	5.实名认证/账号绑定
 """


class Test_4PersonalCenter(unittest.TestCase):

	def setUp(self):
		# Test_1StartSimulator()
		# Test_2Login()
		# Test_3LobbyWindos()
		# print("个人中心环境准备完毕")
		pass

	"""基本信息"""
	def test_1essentialInformation(self):
		from poco.drivers.unity3d import UnityPoco  # 导入并初始化U3d
		poco = UnityPoco()
		# 个人中心
		poco("_Image_Head").click()
		# 头像框 passs
		# 大厅和个人中心玩家昵称/头像框下面显示的昵称
		Test_2Login.test_4userInfo.name = poco("_Text_PassPort").get_text() and poco("_Text_NickName").get_text()
		Pr.print("*******************", "昵称显示一致")
		# 大厅和个人中心玩家ID
		Test_2Login.test_4userInfo.gameId = poco("_Text_GameID").get_text()    # 个人中心玩家ID
		# 等级显示
		Text_GameGrade = poco("_Text_GameGrade").get_text()
		Pr.print("*******************", Text_GameGrade)
		# 等级进度
		Text_GradePro = poco("_Text_GradePro").get_text()
		Pr.print("*******************", Text_GradePro)

		# 贵族等级显示
		Image_NoblePowerNum = poco("_Image_NoblePowerNum").attr('texture')
		Pr.print("*******************", Image_NoblePowerNum)

		# 开心显示
		Text_Gold = poco("_Text_Gold").get_text()
		Pr.print("*******************", Text_Gold)
		# 充值跳转
		Button_Recharge = poco("_Button_Recharge").click()
		Pr.print("*******************", Button_Recharge)
		poco("_Button_Recharge").click()
		time.sleep(2)
		poco(texture="fanhui").click()

		# 红包券显示
		Text_Ticket = poco("_Text_Ticket").get_text()
		Pr.print("*******************", Text_Ticket)
		# 会员显示/非会员显示无/红钻会员显示红钻/蓝钻会员显示蓝钻/金钻会员显示金钻/  会员时间

		# 会员显示/非会员显示无/红钻会员显示红钻/蓝钻会员显示蓝钻/金钻会员显示金钻/  会员时间
		# 会员时间-数据库查询当前用户的会员时间
		if poco("_Text_MemberName").get_text() == "无会员":
			Pr.print("*******************", "玩家为非会员")
		elif poco("_Text_MemberName").get_text() == "<color=#f12b13>红钻</color>":
			# 会员时间
			MembershipTime = poco("_Text_DeadLine").get_text()
			Pr.print("*******************", "玩家为红钻", "会员时间为:", MembershipTime)
			# 查询数据库时间与页面显示是否一致
			pass
		elif poco("_Text_MemberName").get_text() == "<color=#04faf1>蓝钻</color>":
			MembershipTime = poco("_Text_DeadLine").get_text()
			Pr.print("*******************", "玩家为蓝钻", "会员时间为:", MembershipTime)
		elif poco("_Text_MemberName").get_text() == "<color=#f6de70>金钻</color>":
			MembershipTime = poco("_Text_DeadLine").get_text()
			Pr.print("*******************", "玩家为蓝钻", "会员时间为:", MembershipTime)
		else:
			Pr.print("*******************", "会员判断失败！")

		# 实名认证显示/1.未实名认证显示提交认证按钮 2.已实名认证显示已实名认证
		invisible_obj = poco('_Button_ConfirmToVerify', type='Button')
		print(invisible_obj.exists())  # => False. This UI is not visible to user.
		if invisible_obj.exists() == True:
			Pr.print("*******************", "玩家未实名认证！")
		else:
			Pr.print("*******************", "玩家已实名认证")

		# 账号绑定
		poco("_Button_BindPhoneTab").click()
		Button_BindPhoneTab = poco('_Button_ConfirmToVerify', type='Button')
		# print(Button_BindPhoneTab.exists())  # => False. This UI is not visible to user.
		if Button_BindPhoneTab().exists == True:
			Pr.print("*******************", "未绑定手机号")
		else:
			Pr.print("*******************", "已绑定手机号")


	def tearDown(self):
		pass

def main():
		query = Test_4PersonalCenter()
		query.test_1essentialInformation()
if __name__ == '__main__':
	main()

