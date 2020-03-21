import pygame
from pygame.locals import *
class Button():
	"""docstring for Button"""
	def __init__(self, x,y,higt,width,cc,c,t=''):
		self.size=(width,higt)
		self.place=(x,y)
		self.click_color=cc
		self.color=c
		self.text=t
	def Draw(self,event,click,screen,mouse_pos,acton=None):
		if self.size[0]+self.place[0]> mouse_pos[0]>self.place[0] and self.size[1]+self.place[1]>mouse_pos[1]>self.place[1]:
			pygame.draw.rect(screen,(0,0,0,0),(self.place[0],self.place[1],self.size[0],self.size[1]))

			if click[0]==1 :
				return True
			else:
				return False
		else:
			pygame.draw.rect(screen,self.color,(self.place[0],self.place[1],self.size[0],self.size[1]))
		smallText = pygame.font.SysFont("comicsansms",20)
		textSurf = smallText.render(self.text,True,(0,0,0))
		center = (self.place[0],self.place[1])
		screen.blit(textSurf, center)