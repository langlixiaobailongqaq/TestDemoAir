
import os   # 用户访问操作系统功能的模块
import unittest
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
	mail_user = "1544717589@qq.com"  # 用户名
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
	# os.listdir() 方法用户返回指定的文件夹包含的文件或文件夹的名字的列表
	lists = os.listdir(report_dir)

	# 按时间顺序对改目录文件夹下面的文件进行排序
	lists.sort(key=lambda fn: os.path.getatime(report_dir+"\\"+fn))
	print(lists)
	print("latest report is :"+lists[-1])

	# 输出最新报告的路径
	file = os.path.join(report_dir, lists[-1])
	print(file)
	return file

if __name__ == '__main__':
	# 定义测试用例路径
	test_dir = "./test_case"
	# 定义测试报告路径
	report_dir = "./test_report"
	discover = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py")
	now = time.strftime("%Y-%m-%d %H_%M_%S")
	report_name = report_dir+"/"+now + "result.html"

	# 打开文件再报告文件写入测试结果
	with open(report_name, "wb") as f:
		runer = BSTestRunner(stream=f, title="Test Report", description="Test case result")
		runer.run(discover)
		f.close()

	# 获取最新的测试报告
latest_report = latest_report(report_dir)
send_mail(latest_report)

