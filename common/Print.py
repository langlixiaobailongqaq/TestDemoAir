
import time

"""重新定义print方法"""
_print = print
class Print():
	# def print(*args, **kwargs):
	def print(*args, **kwargs):
		# _print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), *args, **kwargs)
		_print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), *args, **kwargs)

Pr = Print()
Pr.print()
