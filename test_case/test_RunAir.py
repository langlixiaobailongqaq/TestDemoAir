"""
用例执行管理

"""

import unittest
from test_case.test_1StartSimulator import *
from test_case.test_2Login import *
from test_case.test_5GameMall import *

import os   # 用户访问操作系统功能的模块
from BSTestRunner import BSTestRunner  # 测试报告模板
import time
import smtplib                          # SMTP邮件
from email.mime.text import MIMEText    # 发送正文只包含简单文本的邮件，引入MIMEText即可
from email.header import Header         # 用来设置邮件头和邮件主题
import sys, logging                     # logging 测试日志输出


sys.path.append(os.path.dirname(os.path.abspath(__file__)) + r'\..')  # 返回脚本的路径
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='log_test.log',
                    filemode='w')
logger = logging.getLogger()



def send_mail(latest_report):
    f = open(latest_report, "rb")  # 读取到最新的测试报告
    mail_content = f.read()
    f.close()

    # 第三方 SMTP 服务
    mail_host = "smtp.qq.com"  # 设置服务器
    mail_user = ""  # 用户名  1544717589@qq.com
    mail_pass = "vocanmhcyywgjgdf"  # 口令

    sender = '1544717589@qq.com'  # 发送邮箱
    receivers = ['1544717589@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    # 发送邮件主题和内容
    subject = 'Python SMTP 邮件测试'

    # HTML邮件正文
    message = MIMEText(mail_content, 'html', 'utf-8')  # 内容
    message['Subject'] = Header(subject, 'utf-8')  # 主题
    message['From'] = "1544717589@qq.com"
    message['To'] = "1544717589@qq.com"

    try:
        smtpObj = smtplib.SMTP()  # 创建一个连接
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)  # 用户名密码验证
        smtpObj.sendmail(sender, receivers, message.as_string())  # 填入邮件的相关信息并发送
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")


def latest_report(report_dir):
    #  os.listdir() 方法用户返回指定的文件夹包含的文件或文件夹的名字的列表
    lists = os.listdir(report_dir)

    # 按时间顺序对改目录文件夹下面的文件进行排序
    lists.sort(key=lambda fn: os.path.getatime(report_dir+"\\"+fn))
    print(lists)
    print("latest report is :"+lists[-1])

    # 输出最新报告的路径
    file = os.path.join(report_dir, lists[-1])
    print(file)
    return file



"执行所有测试用例"
test_dir = 'D:/Pycharm/Pycharm/TestDemoAir/test_case'
# discovery = unittest.defaultTestLoader.discover(test_dir, pattern='test*py')  # 所有

# 执行多个
discovery = unittest.TestSuite()  # 整合测试用例
# discovery.addTest(Test_1StartSimulator("test_1assert"))    # 选择测试用例
discovery.addTest(Test_1StartSimulator("test_1assert"))
discovery.addTest(Test_2Login("test_2login"))
# discovery.addTest(Test_2Login("test_4userInfo"))
discovery.addTest(Test_5GameMall("test_1chongzhi"))



if __name__ == '__main__':
    # 存放报告的文件夹
    report_dir = "D:/Pycharm/Pycharm/TestDemoAir/test_report"  # 需要使用绝对路径，相对路径无法找到
    # 报告命名时间格式化
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    # 报告文件完整路径
    report_name = report_dir + "/" + now + "result.html"

    # 打开文件再报告文件写入测试结果
    with open(report_name, "wb") as f:  # wb 表示以二进制写方式打开，只能写文件， 如果文件不存在，创建该文件；如果文件已存在，则覆盖写
        runner = BSTestRunner(stream=f, title="测试报告", description="happyGame")
        runner.run(discovery)
        f.close()

# 获取最新的测试报告
latest_report = latest_report(report_dir)
send_mail(latest_report)


"""执行所有测试用例
test_dir = './'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*py')  # 所有
if __name__ == '__main__':
    runner=unittest.TextTestRunner()
    runner.run(discover)

"""


"执行单个/多个"
# if __name__ == '__main__':
#     suit = unittest.TestSuite()  # 整合测试用例
#     suit.addTest(Test_PersonalCenter("test_1essentialInformation"))    # 选择测试用例
#     # suit.addTest(Test_Login("test_version"))
#
#     runner = unittest.TextTestRunner()  # 用来执行测试用例
#     runner.run(suit)
