# -*- encoding=utf8 -*-
# __author__ = "Admin"
import poco   # poco库
import unittest # unittest库本库
from airtest.core.api import *   # airtest的官方库
from airtest.core.android.android import Android
import os 
import time

# auto_setup(__file__)

os.system(r"start C:\Users\Admin\Desktop\start_2.bat")  # 启动夜神模拟器
devs = connect_device("Android://127.0.0.1:5037/127.0.0.1:62025?cap_method=JAVACAP&&ori_method=ADBORI&&touch_method=ADBTOUCH")  #连接夜神模拟器
time.sleep(5)
start_app('com.kaixinyule.kaixingame', activity=None)  # 启动待测app
time.sleep(15)

from poco.drivers.unity3d import UnityPoco  # 导入并初始化U3d
poco = UnityPoco()


time.sleep(5)
# 版本号-测试服
Version = "1-1-100-100"

# 版本号-正式服
# Version = "1-3-002-001"

# 签到第一天
Check_in1 = 10000
# 签到第二天
Check_in2 = 20000
# 签到第三天
Check_in3 = 30000
# 签到第四天
Check_in4 = 40000
# 签到第五天
Check_in5 = 50000
# 签到第六天
Check_in6 = 60000
# 签到第七天
Check_in7 = 70000
# keyevent("KEYCODE_1 KEYCODE_2 KEYCODE_3 KEYCODE_4")




# 验证版本号
assert poco("_Text_Version").get_text() == Version,"版本验证错误"

# 账号登录  
poco("_Button_PassPort").click()
poco(text="请输入您的账号").click()
poco("_InputField_PassPort").set_text("2322")
time.sleep(1)
poco("Text").click()

poco(text="请输入您的密码").click()
poco("_InputField_PassWord").set_text("2322")
poco("Text").click()
poco("_Button_ConfirmLogin").click()
time.sleep(5)
# 微信登录
# poco("_Button_WeixinLogon").click()
# time.sleep(5)
    
    
    
# 获取用户名
Name = poco("_Text_Name").get_text()
# print(Name)
# 获取ID
ID =  poco("_Text_Level").get_text()
# print(ID)
# 获取大厅显示用户奖券
ticket = poco("_Text_Score").get_text()
print(ticket)




# 登录验证
assert poco("_Text_Name").get_text() == Name,"登录失败"  # 断言

# 签到-获取用户大厅开心豆
Score = int(poco("_Text_Score").get_text())
print("*******************", Score, "*******************")
time.sleep(1)

# 当天第一次登录签到弹窗
try:
    poco("_Button_Sign").click()     # 签到弹窗页面签到按钮
    Score1 = int(poco("_Text_Score").get_text())     # 获取签到后的用户开心豆
    print("*******************",Score1-Score,"*******************")
    time.sleep(1)
    Score2 = Score1 - Score  # 签到后开心豆减去签到后开心豆
    if Score2 == Check_in1:
        print("*******************" + "第一天签到成功"+ "*******************")
    elif Score2 == Check_in2:
        print("*******************" + "第二天签到成功"+ "*******************")
    elif Score2 == Check_in3:
        print("*******************" + "第三天签到成功"+ "*******************")
    elif Score2 == Check_in4:
        print("*******************" +"第四天签到成功" + "*******************")
    elif Score2 == Check_in5:
        print("*******************" +"第五天签到成功"+ "*******************")
    elif Score2 == Check_in6:
        print("*******************" +"第六天签到成功"+ "*******************")
    elif Score2 == Check_in7:
        print("*******************" + "第七天签到成功" + "*******************")
    poco("_Button_Back").click()   # 关闭签到
    poco("_Button_Close").click()  # 关闭红包场活动
    poco("_Button_Back").click()   # 关闭初春大礼包（大礼包需做断言）
    #活动弹窗断言   
    assert poco("_Panel_Main", type="Raw.Image").get_name()
    Back = poco("_Button_Back")
    Back.click()
    time.sleep(2)
    #每日礼弹窗包断言   
    assert poco("_Text_Tips").get_name()
    Back.click()
    time.sleep(2)
except:    # 非当天第一次登录
    poco("_Button_Close").click()  # 关闭红包场活动
    poco("_Button_Back").click()   # 关闭初春大礼包（大礼包需做断言）
    # 个人中心
    poco("_Image_PortraitFrame").click()
    time.sleep(2)
    
    
    
    
# 个人中心 
assert poco("_Text_NickName").get_text() == Name, "昵称显示错误"
time.sleep(1) 
assert poco("_Text_GameID").get_text() == ID, "ID显示错误"  # ID验证
poco("_Button_Safe").click()  # 账号安全
Back = poco("_Button_Back")   # 返回
Back.click()





# 开心豆充值
poco("_Button_AddScore").click()
poco("_Text_Present").click()
time.sleep(5)
exists(Template(r"pay_immediately.png", record_pos=(0.006, -0.395), resolution=(1080, 1920)))
keyevent("BACK")
time.sleep(3)
poco("_Button_OK").click()




# 月卡充值
poco(texture="qh_yueka").click()
poco(texture="shangcheng3").click()
time.sleep(3)
exists(Template(r"pay_immediately.png", record_pos=(0.006, -0.395), resolution=(1080, 1920)))
keyevent("BACK")
time.sleep(3)
poco(texture="shangcheng4").click()
poco("_Button_Back").click()





# 兑换中心
poco("_Button_Exchange").click()
ticket1 = poco("_Text_BeanNum").get_text() # 获取兑换中心显示的用户开心豆
CostTicket = poco("_Text_CostTicket").get_text() # 获取红包劵兑换第一个开心豆的奖券
doudou = poco("_Text_Title").get_text()    # 获取红包劵兑换第一个的开心豆
hongbao =  poco("_Text_TicketNum").get_text()  # 获取用户红包劵数量
hongbao1 =  poco("_Text_Content").get_text()  # 获取红包劵兑换白银宝箱所需数量
Cardiac_Value = poco("_Text_LoveValue").get_text()  # 心动值


# 红包判断
if hongbao >= CostTicket:
    poco(text="500").click()
    poco("_Button_Confirm").click()
    ticket1 = doudou + ticket
    print(ticket1)
elif hongbao < CostTicket:
    poco(text="500").click()
    print("奖券不足")
    time.sleep(2)

    
    
# 宝箱兑换
poco("_Button_BoxGiftExchange").click()
poco("_Button_ExchangeBox").click()
# 红包劵判断
if hongbao >= hongbao1:
    time.sleep(1)
    poco("Image (3)").click()
    time.sleep(1)
    hongbao = hongbao - hongbao1
    print("***********",hongbao,"***********")
    time.sleep(1)
if exists(Template(r"Red_envelope.png", record_pos=(-0.007, -0.005), resolution=(1920, 1080))):
    hongbao = hongbao + 68
    print("***********",hongbao,"***********")
else:
    print("1")
poco("Image (3)").click()   
poco("_Button_Close").click()
poco("_Button_Record").click() # 兑换记录
poco("_Button_Exit").click()

# 客服
poco("_Button_Customer").click()
poco("_Button_UserCenter").click()
poco(texture="renwuditu4").click()
keyevent("BACK")    # 返回

# 邮件
poco("_Button_Mail").click()
poco("_Button_Back").click()


# 排行榜
poco("_Button_Rank").click()
for i in range(7):
    swipe(v1=(698,868),v2=(698,400))   # 查看排行榜排名
    sleep(2)
#快速冲榜
poco("_Button_GoldQuickEnter").click() 
poco(texture="shangcheng3").click()
time.sleep(5)
keyevent("BACK")
time.sleep(1)
poco("_Button_OK").click()
poco(texture="qh_yueka").click()
poco("_Button_LimitedTime").click()
time.sleep(5)
keyevent("BACK")
time.sleep(1)
poco("_Button_OK").click()
poco("_Button_Back").click()
poco("_Button_QuickStart").click()



# 每日礼包
poco("_Button_DailyGift").click()
poco("_Button_Buy1").click()
time.sleep(5)
keyevent("BACK")
poco("_Button_OK").click()
poco("_Button_Back").click()


# 月卡
poco("_Button_MonthCard").click()
poco("_Button_Buy").click()
time.sleep(5)
keyevent("BACK")
poco("_Button_OK").click()
poco("_Button_Back").click()



# 商城-开心豆充值
poco("_Button_Charge").click()
poco(texture="shangcheng3").click()
time.sleep(6)
keyevent("BACK")
poco("_Button_OK").click()


# 商城-月卡充值
poco(texture="qh_yueka").click()
poco(texture="shangcheng3").click()
time.sleep(6)
keyevent("BACK")
poco("_Button_OK").click()
poco("_Button_Back").click()


# 保险箱
poco("_Button_Bank").click()
try:
    poco("_InputField_Passwd").set_text("111111")
    poco("_Button_Login").click()
    time.sleep(1)
except: 
    print("不需要输入密码")
    
if poco("Placeholder").get_text() == "请输入初始密码":
    poco("_InputField_Passwd").set_text("123456")
    poco("_Button_Login").click()
else:        
# 保险箱-存取-全部取出
    poco("_Button_AllBank").click()
    poco("_Button_Take").click()
    poco(texture="ditu1").click()
    time.sleep(1)


    # 全部存入
poco("_Button_AllScore").click()
poco("_Button_Transfer").click()
poco(texture="ditu1").click()
time.sleep(1)

    # 刷新
poco("_Button_AllBank").click()
poco(texture="shuaxin").click()
time.sleep(1)
poco("_Button_AllScore").click()
poco(texture="shuaxin").click()
time.sleep(1)

    # 存入
poco("_InputField_OperateScore").set_text("10000")
poco("_Button_Transfer").click()
poco(texture="ditu1").click()
time.sleep(2)
    #取出
poco("_InputField_OperateScore").set_text("10000")
poco("_Button_Take").click()

    # 修改密码
poco("_Button_Modify#").click()
poco("RedPacketMarket(Clone)").child("_Button_Start").click()
poco("_InputField_PwdOld").set_text("123456")
sleep(1)
poco("_InputField_PwdNew").set_text("111111")
sleep(1)
poco("_InputField_PwdConfirm").set_text("111111")
sleep(1)
poco("_Button_Transfer").click()

    # 设置
poco("_Button_Setting#").click()
poco("_Button_Transfer").click()


# 免费金币 -签到
poco("_Button_FreeGold").click()
poco("_Button_Sign").click()
poco("_Button_Back").click()

    # 救济金
doudou = poco("_Text_Score").get_text()
print("************************",doudou)
sleep(1) 
poco("_Button_Relief").click()
Alms = poco("Text1").get_text()
print("************************",Alms)
Alms2 = poco("Text2").get_text()
print("************************",Alms2)
Alms3 = poco("Text3").get_text()
print("************************",Alms3)
poco("_Text_CountDown").click()

poco("_Button_ShareToget").click()
sleep(3)

touch(Template(r"back.png", record_pos=(-0.473, -0.229), resolution=(1920, 1080)))
touch(Template(r"Not_Retained.png", record_pos=(0.091, 0.073), resolution=(1080, 1920)))
sleep(3)
poco("_Button_Exit").click()

  # 活动卡
poco("_Button_ActivityCard").click()
poco("_InputField_CardNum").set_text("1")
poco("_InputField_Password").set_text("2")
poco("_Button_GetReward").click()
sleep(1)
poco("_Button_Close").click()

    # 新手卡
poco(texture="hongbao-wenzi").click()
poco("_InputField_CardNum").set_text("1")
poco("_InputField_Password").set_text("2")
poco("_Button_GetReward").click()
poco("_Button_Exit").click()

    # 来赚钱-个人中心
poco("_Button_SpreadNew").click()
sleep(3)
touch(Template(r"Personal_center.png", record_pos=(0.278, -0.2), resolution=(1920, 1080)))
sleep(3)
keyevent("BACK") 
    # 奖励
touch(Template(r"reward.png", record_pos=(0.283, -0.074), resolution=(1920, 1080)))
sleep(1)
poco("BirdsAndAnimals(Clone)").child("_Button_Start").click()
    # 二维码
touch(Template(r"QR_code.png", record_pos=(0.334, 0.03), resolution=(1920, 1080)))
sleep(1)
keyevent("BACK")

  # 成员列表
touch(Template(r"Member_list.png", record_pos=(-0.258, 0.108), resolution=(1920, 1080)))
sleep(3)
touch(Template(r"Ordinary_player.png", record_pos=(-0.227, -0.13), resolution=(1920, 1080)))
sleep(1)
touch(Template(r"Not_logged_in.png", record_pos=(-0.116, -0.13), resolution=(1920, 1080)))
sleep(1)
keyevent("BACK")

    # 收益明细
poco("_Button_Share").click()
touch(Template(r"Secondary_agent.png", record_pos=(-0.229, -0.154), resolution=(1920, 1080)))
sleep(1)
touch(Template(r"Tertiary_agent.png", record_pos=(-0.132, -0.156), resolution=(1920, 1080)))
sleep(1)
touch(Template(r"Inquire.png", record_pos=(0.343, -0.202), resolution=(1920, 1080)))
keyevent("BACK")

    # 奖励明细
poco("_Button_Relief").click()
keyevent("BACK")

    # 茶馆简介
poco("_Button_SpreadNew").click()
touch(Template(r"Teahouse_description.png", record_pos=(-0.144, -0.106), resolution=(1920, 1080)))
keyevent("Z 32")
poco("_Button_Start").click()
keyevent("BACK")
keyevent("BACK")
keyevent("BACK")
