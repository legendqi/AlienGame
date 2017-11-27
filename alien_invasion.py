# /usr/bin/python
# encoding=utf-8
import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
def run_game():
	# 初始化游戏并创建一个屏幕对象
	pygame.init()
	ai_settings=Settings()
	screen=pygame.display.set_mode((1000,600))
	#screen=pygame.display.set_mode(ai_settings.screen_width,ai_settings.screen_height)
	pygame.display.set_caption("Alien Invasion")
	# 创建一艘飞船
	ship=Ship(ai_settings,screen)
	# 创建一个用于存储子弹的编组
	bulltes=Group()
	# 设置背景色
	bg_color=(230,230,230)

	# 开始游戏的主循环 
	while  True:

		# 监视键盘和鼠标事件
		gf.check_events(ai_settings,screen,ship,bulltes)
		# ship.update()
		bulltes.update()
		gf.update_screen(ai_settings,screen,ship,bulltes)
run_game()
