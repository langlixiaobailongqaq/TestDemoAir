"""
SetUP与TearDown管理

"""
import unittest


class Setup_tearDown(unittest.TestCase):
	def setUp(self):
		# __author__ = "Admin"
		# from airtest.core.api import *
		# auto_setup(__file__)
		import poco  # poco库
		from airtest.core.android.android import Android
		import os
		import time

		from poco.drivers.unity3d import UnityPoco  # 导入并初始化U3d
		poco = UnityPoco()
		import unittest

	def tearDown(self):
		pass

