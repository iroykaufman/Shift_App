import pygame
from pygame.locals import *
from InputBox import InputBox
from button import Button
import time
from datasave import start,end
class main_page():

 	"""docstring for open_page"""
 	def __init__(self,width=400,hight=350,backraund=(200,200,200),FontTitel='chalkduster.ttf'
 		,textFont='344',titel="New_Shift",fill_one="Name:",fill_two="ID:"):
 		self.w=width
 		self.h=hight
 		self.screen=pygame.display.set_mode((hight,width))
 		self.titelfont=pygame.font.SysFont(FontTitel, 72)
 		self.Titel_r=self.titelfont.render(titel,True,(255,255,255))
 		self.Tfont=pygame.font.SysFont(textFont,24)
 		self.first_parameter=self.Tfont.render(fill_one,True,(255,255,255))
 		self.second_parameter=self.Tfont.render(fill_two,True,(255,255,255))
 		self.backraund_color=backraund
 		self.input_box1 = InputBox(70, 120, 85, 20)
 		self.input_box2 = InputBox(45, 95, 85, 20) 	
 		self.Sflag=False
 		self.Eflag=False
 		self.Stexttime=None
 		self.Etexttime=None
 	def draw(self,event,m,c):
 		ts=None
 		te=None
 		self.screen.fill(self.backraund_color)
 		self.screen.blit(self.Titel_r,(100,20))
 		self.screen.blit(self.first_parameter,(20,120))
 		self.screen.blit(self.second_parameter,(20,95))
 		for x in [self.input_box1,self.input_box2]:
 			x.handle_event(event)
 			x.update()
 			x.draw(self.screen)
 		btstart=Button(t="start",x=0,y=150,width=100000,higt=35,cc=(0,0,0),c=(255,255,255)).Draw(event,c,self.screen,m)
 		btend=Button(t="end",x=0,y=190,width=100000,higt=35,cc=(0,0,0),c=(255,255,255)).Draw(event,c,self.screen,m)
 		smallText = pygame.font.SysFont("comicsansms",20)
 		if(btstart and self.Eflag==False):
 			self.Sflag=True
 			ts=time.localtime()
 			self.Stexttime="{}:{}".format(ts.tm_hour,ts.tm_min)
 			s=start(self.input_box1.Text(),self.input_box2.Text())
 		if(self.Sflag==True ):
 			textSurf = smallText.render("Start time:{}".format(self.Stexttime),True,(0,0,0))
 			self.screen.blit(textSurf, (0,250)) 			
 		if(self.Sflag==True and  btend):
 			self.Eflag=True
 			te=time.localtime()
 			self.Etexttime="{}:{}".format(te.tm_hour,te.tm_min)
 			end(self.input_box1.Text(),self.input_box2.Text())
 		if(self.Eflag==True):
 			textSurf = smallText.render("End time:{}".format(self.Etexttime),True,(0,0,0))
 			self.screen.blit(textSurf, (0,300))
 		pygame.display.update()
if __name__ == '__main__':
	pygame.init()
	test=main_page()
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	run=True
	while run:
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		for event in pygame.event.get():
			if event.type==QUIT:
				run=False
			test.draw(event,mouse,click)
	pygame.quit()
	