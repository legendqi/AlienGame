# /usr/bin/python
# encoding=utf-8
import sys
import pygame
from bullet import Bullet
def check_events(ai_settings, screen, ship, bullets):
	"""响应按键和鼠标事件"""
	for event in pygame.event.get():
		print("event.type:  "+str(event.type))
		if event.type==pygame.QUIT:
			sys.exit()
		elif event.type==pygame.KEYDOWN:
			check_keydown_events(event,ai_settings,screen,ship,bullets)
			# print("centerx: "+ship.rect.centerx+ "  bottom :"+ship.rect.bottom)
			# if event.key==pygame.K_RIGHT:
			# 	#向右移动飞船
			# 	ship.moving_right=True
			# 	ship.rect.centerx+=1
			# 	print(str(ship.rect.centerx))
			# elif event.key==pygame.K_LEFT:
			# 	#向移动飞船
			# 	print('left')
			# 	ship.moving_left=True
			# 	print('left centerx>0')
			# 	ship.rect.centerx-=1
			# elif event.key==pygame.K_SPACE:
			# 	# 创建一颗子弹,并将其加入到编组bullets中
			# 	new_bullet=Bullte(ai_settings,screen,ship)
			# 	print("add new bullte")
			# 	bullets.add(new_bullet)
		elif event.type==pygame.KEYUP:
			# if event.key==pygame.K_RIGHT:
			# 	ship.moving_right=False
			# elif event.key==pygame.K_LEFT:
			# 	ship.moving_left=False
			check_keyup_events(event,ship)
def update_screen(ai_settings, screen, ship,bulltes):
	"""更新屏幕上的图像,并切换到新屏幕"""
	# 每次循环时都重绘屏幕
	#screen.fill(bg_color)
	screen.fill(ai_settings.bg_color)
	for bullte in bulltes.sprites():
		bullte.draw_bullet()
	ship.blitme()
	# 让最近绘制的屏幕可见
	pygame.display.flip()
def check_keydown_events(event,ai_settings,screen,ship,bulltes):
	"""响应按键"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.type==pygame.K_SPACE:
		# 创建一颗子弹,并将其加入到编组bullets中
		new_bullet=Bullte(ai_settings,screen,ship)
		print("add new bullte")
		bulltes.add(new_bullet)
def check_keyup_events(event, ship):
	"""响应松开"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False
