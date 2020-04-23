
import unittest
import pymysql
# from test_case.test_2Login import *  不能互相引用，会导致循环导入。


class Test_Mysql():
	QUERYRESULTS = ''           # 查询结果
	MYSQLGAMEID = '603476'     # gameid
	MYSQLUSERID = ''          # userid

	def __init__(self):
		# 建立数据库连接
		self.conn = pymysql.Connect(
			host='127.0.0.1',
			port=3306,
			user='root',
			passwd='Zx123456',
			# db='',
			charset='utf8',
		)

		"""查询用户信息"""
	def test_query1(self):
		global QUERYRESULTS
		# global MYSQLGAMEID
		# global MYSQLUSERID

		cursor = self.conn.cursor()
		# 获取游标
		# print(conn)
		# print(cursor)
		# 1、从数据库中查询
		# gameid = "1090662"

		gameid = Test_Mysql.MYSQLGAMEID
		sql = "SELECT UserID,GameID,NickName,Ticket,LoveLiness,registerdate,IsNew FROM qpaccountsdb.AccountsInfo WHERE GameID ="+ gameid
		# cursor执行sql语句
		cursor.execute(sql)
		row = cursor.fetchone()  # 返回单个的元组，也就是一条记录(row)，如果没有结果 则返回 None
		QUERYRESULTS = row[1]
		print(row)

		MYSQLUSERID = str(row[0])

		# print(QUERYRESULTS)
		# Test_Mysql.MYSQLUSERID = row[0]     # userID

		Test_Mysql.QUERYRESULTS = QUERYRESULTS   # gameID
		# print(Test_Mysql.QUERYRESULTS)

		# 数据库连接和游标的关闭
		self.conn.close()
		cursor.close()

		# row = cursor.fetchall()  # 返回多个元组，即返回多个记录(rows),如果没有结果 则返回 ()
		# for it in row:
		# 	for i in range(len(it)):
		# 		print(it[i], ' ', end='')
		# 	print('\n')
		# print(it[1])
		# 数据库连接和游标的关闭
		# self.conn.close()
		# cursor.close()


	# def __del__(self):
	# 	# 数据库连接和游标的关闭
	# 	# 1.关闭游标
	# 	self.conn.close()
	# 	# 2.关闭连接
	# 	self.cursor.close()

	"""查询玩家会员信息"""
	def test_member2(self):
		mysql.test_query1()   # 先查询用户信息，得到userID
		# print(MYSQLUSERID)
		# print(type(MYSQLUSERID))

		cursor = self.conn.cursor()
		# userid = MYSQLUSERID
		sql = "SELECT * FROM qpaccountsdb.AccountsMember WHERE UserID ="+userid
		# cursor执行sql语句
		cursor.execute(sql)
		# row = cursor.fetchone()0  # 返回单个的元组，也就是一条记录(row)，如果没有结果 则返回 None
		row = cursor.fetchall()  # 返回多个元组，即返回多个记录(rows),如果没有结果 则返回 ()
		for it in row:
			for i in range(len(it)):
				print(it[i], ' ', end='')
			print('\n')
		print(it[1])
		# print(row)



		# QUERYRESULTS = row[1]
		# print(QUERYRESULTS)
		# Test_Mysql.QUERYRESULTS = QUERYRESULTS
		# print(Test_Mysql.QUERYRESULTS)

		self.conn.close()
		cursor.close()

	"""查询玩家金币信息"""
	def test_scoreInfo3(self):
		cursor = self.conn.cursor()
		sql = "SELECT * FROM qptreasuredb.GameScoreInfo WHERE UserID='1000100'"
		# cursor执行sql语句
		cursor.execute(sql)
		row = cursor.fetchone()  # 返回单个的元组，也就是一条记录(row)，如果没有结果 则返回 None
		self.conn.close()
		cursor.close()

	"""查询玩家累充宝箱信息"""
	def test_cumulative4(self):
		cursor = self.conn.cursor()
		sql = "SELECT * FROM qpextensiondb.RechargeCaseRecord WHERE userid='468021'"
		# cursor执行sql语句
		cursor.execute(sql)
		# row = cursor.fetchone()  # 返回单个的元组，也就是一条记录(row)，如果没有结果 则返回 None
		row = cursor.fetchall()  # 返回多个元组，即返回多个记录(rows),如果没有结果 则返回 ()
		for it in row:
			for i in range(len(it)):
				print(it[i], ' ', end='')
			print('\n')
		# 数据库连接和游标的关闭
		self.conn.close()
		cursor.close()

	"""累充宝箱配置表"""
	def test_cumulativeConfig5(self):
		cursor = self.conn.cursor()
		sql = "SELECT * FROM qpextensiondb.RechargeCaseConfig"
		# cursor执行sql语句
		cursor.execute(sql)
		# row = cursor.fetchone()  # 返回单个的元组，也就是一条记录(row)，如果没有结果 则返回 None
		row = cursor.fetchall()  # 返回多个元组，即返回多个记录(rows),如果没有结果 则返回 ()
		for it in row:
			for i in range(len(it)):
				print(it[i], ' ', end='')
			print('\n')
		# 数据库连接和游标的关闭
		self.conn.close()
		cursor.close()

	"""开心豆配置"""
	def test_rechargeConfig6(self):
		cursor = self.conn.cursor()
		sql = "SELECT * FROM qpextensiondb.RechargeConfig WHERE ChannelID='happyGame'  ORDER BY `InsertTime` DESC"
		# cursor执行sql语句
		cursor.execute(sql)
		# row = cursor.fetchone()  # 返回单个的元组，也就是一条记录(row)，如果没有结果 则返回 None
		row = cursor.fetchall()  # 返回多个元组，即返回多个记录(rows),如果没有结果 则返回 ()
		for it in row:
			for i in range(len(it)):
				print(it[i], ' ', end='')
			print('\n')
		# 数据库连接和游标的关闭
		self.conn.close()
		cursor.close()


		"""宝箱兑换配置"""
	def test_boxConfig7(self):
		cursor = self.conn.cursor()
		sql = "SELECT * FROM qpextensiondb.BoxConfig"
		# cursor执行sql语句
		cursor.execute(sql)
		# row = cursor.fetchone()  # 返回单个的元组，也就是一条记录(row)，如果没有结果 则返回 None
		row = cursor.fetchall()  # 返回多个元组，即返回多个记录(rows),如果没有结果 则返回 ()
		for it in row:
			for i in range(len(it)):
				print(it[i], ' ', end='')
			print('\n')
		# 数据库连接和游标的关闭
		self.conn.close()
		cursor.close()


	"""宝箱兑换概率配置"""
	def test_bxDate8(self):
		cursor = self.conn.cursor()
		sql = "SELECT * FROM qpextensiondb.BoxDate"
		# cursor执行sql语句
		cursor.execute(sql)
		# row = cursor.fetchone()  # 返回单个的元组，也就是一条记录(row)，如果没有结果 则返回 None
		row = cursor.fetchall()  # 返回多个元组，即返回多个记录(rows),如果没有结果 则返回 ()
		for it in row:
			for i in range(len(it)):
				print(it[i], ' ', end='')
			print('\n')
		# 数据库连接和游标的关闭
		self.conn.close()
		cursor.close()


	"""兑换数值配置"""
	def test_recharge9(self):
		cursor = self.conn.cursor()
		sql = "SELECT * FROM qpextensiondb.Recharge"
		# cursor执行sql语句
		cursor.execute(sql)
		# row = cursor.fetchone()  # 返回单个的元组，也就是一条记录(row)，如果没有结果 则返回 None
		row = cursor.fetchall()  # 返回多个元组，即返回多个记录(rows),如果没有结果 则返回 ()
		for it in row:
			for i in range(len(it)):
				print(it[i], ' ', end='')
			print('\n')
		# 数据库连接和游标的关闭
		self.conn.close()
		cursor.close()

	"""抽奖配表"""
	def test_drawConfig10(self):
		cursor = self.conn.cursor()
		sql = "SELECT * FROM qpextensiondb.DrawConfig"
		# cursor执行sql语句
		cursor.execute(sql)
		# row = cursor.fetchone()  # 返回单个的元组，也就是一条记录(row)，如果没有结果 则返回 None
		row = cursor.fetchall()  # 返回多个元组，即返回多个记录(rows),如果没有结果 则返回 ()
		for it in row:
			for i in range(len(it)):
				print(it[i], ' ', end='')
			print('\n')
		# 数据库连接和游标的关闭
		self.conn.close()
		cursor.close()

	"""签到领取记录-1.更改领取时间，改为前一天；2.RedisDesktopManager中，
		stringGameID下的GameId更改时间戳（秒级，一直改为昨天的时间）"""
	def test_signRecord11(self):
		cursor = self.conn.cursor()
		sql = "SELECT * FROM qpextensiondb.SignRecord WHERE GameID='400142'"
		# cursor执行sql语句
		cursor.execute(sql)
		# row = cursor.fetchone()  # 返回单个的元组，也就是一条记录(row)，如果没有结果 则返回 None
		row = cursor.fetchall()  # 返回多个元组，即返回多个记录(rows),如果没有结果 则返回 ()
		for it in row:
			for i in range(len(it)):
				print(it[i], ' ', end='')
			print('\n')
		# 数据库连接和游标的关闭
		self.conn.close()
		cursor.close()

	"""所有活动卡，新手卡已领取卡号，密码记录"""
	def test_noviceCard12(self):
		cursor = self.conn.cursor()
		sql = "SELECT * FROM qpextensiondb.NoviceCard WHERE UseTime>='2019-05-06 11:15:03'"
		# cursor执行sql语句
		cursor.execute(sql)
		# row = cursor.fetchone()  # 返回单个的元组，也就是一条记录(row)，如果没有结果 则返回 None
		row = cursor.fetchall()  # 返回多个元组，即返回多个记录(rows),如果没有结果 则返回 ()
		for it in row:
			for i in range(len(it)):
				print(it[i], ' ', end='')
			print('\n')
		# 数据库连接和游标的关闭
		self.conn.close()
		cursor.close()

	"""活动卡，新手卡领取记录"""
	def test_noviceCardRecord13(self):
		cursor = self.conn.cursor()
		sql = "SELECT * FROM qpextensiondb.NoviceCardRecord WHERE GameID='400142'"
		# cursor执行sql语句
		cursor.execute(sql)
		# row = cursor.fetchone()  # 返回单个的元组，也就是一条记录(row)，如果没有结果 则返回 None
		row = cursor.fetchall()  # 返回多个元组，即返回多个记录(rows),如果没有结果 则返回 ()
		for it in row:
			for i in range(len(it)):
				print(it[i], ' ', end='')
			print('\n')
		# 数据库连接和游标的关闭
		self.conn.close()
		cursor.close()


	"""解决新手注册没新手礼包限制，1.查找gameID下的RegisterMachine"""
	def test_noviceCardRecord13(self):
		cursor = self.conn.cursor()
		sql = "SELECT GameID,RegisterMachine from qpaccountsdb.AccountsInfo where GameID='404903'"

		# cursor执行sql语句
		cursor.execute(sql)
		row = cursor.fetchone()  # 返回单个的元组，也就是一条记录(row)，如果没有结果 则返回 None
		# row = cursor.fetchall()  # 返回多个元组，即返回多个记录(rows),如果没有结果 则返回 ()
		# for it in row:
		# 	for i in range(len(it)):
		# 		print(it[i], ' ', end='')
		# 	print('\n')
		# # 数据库连接和游标的关闭
		self.conn.close()
		cursor.close()


mysql = Test_Mysql()



def main():
	query = Test_Mysql()
	query.test_query1()
	# print(a)
		#  test_member2  test_query1

if __name__ == '__main__':
	# from test_case.test_2Login import Test_2Login
	# userInfo = Test_2Login()
	# userInfo.test_4userInfo()
	# Test_Mysql.MYSQLGAMEID = userInfo.GAMEID

	# a = Test_Mysql.MYSQLGAMEID

	# print(userInfo.GAMEID)
	# print(Test_Mysql.MYSQLGAMEID)
	main()








# 2数据库中插入数据
# sql_insert = "INSERT INTO userinfor(username,password) values('中兴','123')"
# # 执行语句
# cursor.execute(sql_insert)
# # 事务提交，否则数据库得不到更新
# conn.commit()
# print(cursor.rowcount)
#
# # 修改数据库中的内容
# sql_update = "UPDATE userinfor SET username='121' WHERE id=21"
# cursor.execute(sql_update)
# conn.commit()
#
# # 删除数据库中的内容，并利用try catch语句进行事务回滚
# try:
# 	sql_delete = "DELETE FROM userinfor WHERE id=6"
# 	cursor.execute(sql_delete)
# 	conn.commit()
# except Exception as e:
# 	print(e)
# 	# 事务回滚，即出现错误后，不会继续执行，而是回到程序未执行的状态，原先执行的也不算了
# 	conn.rollback()

# 数据库连接和游标的关闭
