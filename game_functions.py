# /usr/bin/python
# encoding=utf-8
import sys
import pygame
from bullet import Bullet
from alien import Alien
def check_events(ai_settings,screen,ship,bulltes):
	"""响应按键和鼠标事件"""
	for event in pygame.event.get():
		# print("event.type:  "+str(event.type))
		if event.type==pygame.QUIT:
			sys.exit()
		elif event.type==pygame.KEYDOWN:
			check_keydown_events(event,ai_settings,screen,ship,bulltes)
		elif event.type==pygame.KEYUP:
			check_keyup_events(event,ship)
def update_screen(ai_settings, screen, ship, alines, bulltes):
	"""更新屏幕上的图像,并切换到新屏幕"""
	# 每次循环时都重绘屏幕
	#screen.fill(bg_color)
	screen.fill(ai_settings.bg_color)
	for bullte in bulltes.sprites():
		bullte.draw_bullet()
	ship.blitme()
	alines.draw(screen)
	# 让最近绘制的屏幕可见
	pygame.display.flip()
def check_keydown_events(event,ai_settings,screen,ship,bulltes):
	"""响应按键"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key==pygame.K_SPACE:
		fire_bullet(ai_settings,screen,ship,bulltes)
	elif event.key==pygame.K_q:
		sys.exit()
def check_keyup_events(event, ship):
	"""响应松开"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False
def update_bullets(bulltes):
	"""更新子弹的位置，并删除已消失的子弹"""
	#更新子弹的位置
	bulltes.update()
		#删除已经消失的子弹
	for bullte in bulltes.copy():
		if bullte.rect.bottom<=0:
			bulltes.remove(bullte)
def fire_bullet(ai_settings,screen,ship,bulltes):
	#如果还没有到达限制，就发射一颗子弹
	# 创建一颗子弹,并将其加入到编组bullets中
		if len(bulltes)<ai_settings.bulltes_allowed:
			new_bullet = Bullet(ai_settings,screen,ship)
			# print("add new bullte")
			bulltes.add(new_bullet)
def get_number_aliens_x(ai_settings,aline_width):
	"""计算每行可以容纳多少个外星人"""
	available_space_x=ai_settings.screen_width-2*aline_width
	number_alines_x=int(available_space_x/(2*aline_width))
	return number_alines_x
def create_fleet(ai_settings,screen,ship,alines):
	"""创建外星人群"""
	#创建一个外星人，并计算一行可以容纳多好个外星人
	#外星人间距为外星人的宽度
	alien=Alien(ai_settings,screen)
	# alien_width=alien.rect.width
	number_alines_x=get_number_aliens_x(ai_settings,alien.rect.width)
	number_rows=get_number_rows(ai_settings,ship.rect.height,alien.rect.height)
	#创建第一行外星人
	for row_number in range(number_rows):
		for alien_number in range(number_alines_x):
			create_aline(ai_settings,screen,alines,alien_number,row_number)
def create_aline(ai_settings,screen,aliens,alien_number,row_number):
	#创建一个外星人并将其加入当前行
	alien = Alien(ai_settings,screen)
	alien_width = alien.rect.width
	alien.x = alien_width+2*alien_width*alien_number
	alien.rect.x = alien.x
	alien.rect.y=alien.rect.height+2*alien.rect.height*row_number
	aliens.add(alien)
def get_number_rows(ai_settings,ship_height,alien_height):
	"""计算屏幕可容纳多少行外星人"""
	available_space_y=(ai_settings.screen_height-(3*alien_height)-ship_height)
	number_rows=int(available_space_y/(2*alien_height))
	return number_rows