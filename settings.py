# /usr/bin/python
# encoding=utf-8
class Settings():
	"""存储《外星人入侵》的所有设置的类"""
	def __init__(self):
		"""初始化游戏的设置"""
		# 子弹设置
		self.bullet_speed_factor = 1
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		# 飞船的设置
		self.ship_speed_factor = 1.5
		# 屏幕设置
		self.screen_width=1000
		self.screen_height=600
		self.bg_color=(230,230,230)
