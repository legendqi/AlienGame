# /usr/bin/python
# encoding=utf-8

import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien

def run_game():
	# 初始化游戏并创建一个屏幕对象
	pygame.init()
	ai_settings=Settings()
	screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	# 创建一艘飞船
	ship=Ship(ai_settings,screen)
	#创建一个外星人
	alines=Group()
	aline=Alien(ai_settings,screen)
	gf.create_fleet(ai_settings,screen,ship,alines)
	# 创建一个用于存储子弹的编组
	bulltes=Group()
	# 设置背景色
	bg_color=(230,230,230)
	# 开始游戏的主循环 
	while  True:
		# 监视键盘和鼠标事件
		gf.check_events(ai_settings,screen,ship,bulltes)
		ship.update()
		gf.update_bullets(bulltes)
		gf.update_screen(ai_settings,screen,ship,alines,bulltes)

run_game()
