import pygame
from pygame.locals import *
import time
import random
import gc
    
   
class PlayerPlane(object):
    #bullet
    BulletList=[]
    
    def __init__(self,screen):
       
	
			
	   	#plane
	 	Plane='./image/hero1.png'
		PlaneDown1='./image/hero_blowup_n1.png'
		PlaneDown2='./image/hero_blowup_n2.png'
		PlaneDown3='./image/hero_blowup_n3.png'
		PlaneDown4='./image/hero_blowup_n4.png'

		self.plane1 =pygame.image.load(Plane).convert_alpha()
		self.planedown1 =pygame.image.load(PlaneDown1).convert_alpha()
		self.planedown2 =pygame.image.load(PlaneDown2).convert_alpha()
		self.planedown3 =pygame.image.load(PlaneDown3).convert_alpha()
		self.planedown4 =pygame.image.load(PlaneDown4).convert_alpha()
		self.symbol=0
	
		#location
		self.x=230
		self.y=600
	
		 	
		#set
		self.screen=screen
		self.healthy=10
		self.injured=30
		self.middle=50
		self.borken=70
		self.defeat=220
	
	
    
    def DrawPlane(self):
	
		#calculation
		if(EnemyPlane.symbol<2400):
			for temp in EnemyPlane.Bullet1:
				if (temp.x>self.x+30 and temp.x<self.x+62) and (temp.y<self.y+70 and temp.y>self.y+10):
					self.symbol+=1
			for temp in EnemyPlane.Bullet2:
				if (temp.x>self.x+30 and temp.x<self.x+62) and (temp.y<self.y+70  and temp.y>self.y+10):
					self.symbol+=1	
			for temp in EnemyPlane.Bullet3:
				if (temp.x>self.x+30 and temp.x<self.x+62) and (temp.y<self.y+70  and temp.y>self.y+10):
					self.symbol+=1	
			for temp in EnemyPlane.Bullet4:
				if (temp.x>self.x+30 and temp.x<self.x+62) and (temp.y<self.y+70  and temp.y>self.y+10):
					self.symbol+=1
			for temp in EnemyPlane.Bullet5:
				if (temp.x>self.x+30 and temp.x<self.x+62) and (temp.y<self.y+70  and temp.y>self.y+10):
					self.symbol+=1
			for temp in Enemy.Bullet1:
				if (temp.x>self.x+30 and temp.x<self.x+62) and (temp.y<self.y+70  and temp.y>self.y+10):
					self.symbol+=1
	
		#display
		if self.symbol<self.healthy:
			self.screen.blit(self.plane1,(self.x,self.y))
		elif self.symbol<self.injured:
			self.screen.blit(self.planedown1,(self.x,self.y))
		elif self.symbol<self.middle:
			self.screen.blit(self.planedown2,(self.x,self.y))
		elif self.symbol<self.borken:
			self.screen.blit(self.planedown3,(self.x,self.y))
		elif self.symbol<self.defeat :
			self.screen.blit(self.planedown4,(self.x,self.y))
			self.symbol+=1
	
		#shoot
		if self.symbol<self.borken:
			for temp in PlayerPlane.BulletList:
			    temp.DrawBullet()
	   	    

    def KeyHandle(self,keyValue):
    
	 	if self.symbol<self.borken:
			if self.symbol<self.middle:
			    if keyValue=="left":
			        if self.x>0:    
						self.x -=10
					    #print "left"
			    elif keyValue=="right":
			        if self.x<400:    
						self.x +=10
					    #print "right"
			    elif keyValue=="up":
			        if self.y>0:
						self.y -=10
					    #print "up"
			    elif keyValue=="down":
			        if self.y<610:
						self.y +=10
					    #print "down"
			    elif keyValue=="space":
			        PlayerPlane.BulletList.append(PlayerBullet(self.screen,self.x+40,self.y-5))
			else :
				if keyValue=="left":
					if self.x>0:    
						self.x -=5
						#print "left"
				elif keyValue=="right":
					if self.x<400:    
						self.x +=5
						#print "right"
				elif keyValue=="up":
					if self.y>0:
						self.y -=5
						#print "up"
				elif keyValue=="down":
					if self.y<610:
						self.y +=5
						#print "down"
				elif keyValue=="space":
					PlayerPlane.BulletList.append(PlayerBullet(self.screen,self.x+40,self.y-5))

	
    def Event(self):
        
		key_press=pygame.key.get_pressed()	
		if key_press[K_a] or key_press[K_LEFT]:
			self.KeyHandle("left")
		if key_press[K_d]or key_press[K_RIGHT]:
			self.KeyHandle("right")
		if key_press[K_w] or key_press[K_UP]:
			self.KeyHandle("up")
		if key_press[K_s] or key_press[K_DOWN]:
			self.KeyHandle("down")
		if key_press[K_SPACE]:
			self.KeyHandle("space")
	  	    

class PlayerBullet():
    
	def __init__(self,screen,x,y):
	
		bullet='./image/bullet.png'
		self.bullet=pygame.image.load(bullet).convert_alpha()
		self.screen=screen	
		self.x=x
		self.y=y
	
	def DrawBullet(self):
		if self.y>0:
			self.y-=20
			self.screen.blit(self.bullet,(self.x,self.y))
		
	
class Enemy(object):

	symbol=0
	Bullet1=[]
	def __init__(self,screen):
		Plane='./image/enemy0.png'
		PlaneDown1='./image/enemy0_down1.png'
		PlaneDown2='./image/enemy0_down2.png'
		PlaneDown3='./image/enemy0_down3.png'
		PlaneDown4='./image/enemy0_down4.png'
		self.plane1 =pygame.image.load(Plane).convert_alpha()
		self.planedown1 =pygame.image.load(PlaneDown1).convert_alpha()
		self.planedown2 =pygame.image.load(PlaneDown2).convert_alpha()
		self.planedown3 =pygame.image.load(PlaneDown3).convert_alpha()
		self.planedown4 =pygame.image.load(PlaneDown4).convert_alpha()
		self.screen=screen
		self.x=0
		self.y=0
		self.move="left"
		
	def Move(self):
		if self.x >350:
			self.move="right"
		elif self.x<10:
			self.move="left"
		if cmp(self.move,"right"):
			self.x+=3
			self.y+=3
		else:
			self.x-=3	
			self.y-=3
	

	def DrawPlane(self):
		if self.symbol<5:
			self.Move()
			self.Shoot()
		for temp in PlayerPlane.BulletList:
			if (temp.x>self.x and temp.x<self.x+51) and (temp.y<self.y+39 and temp.y>self.y):
				EnemyPlane.symbol+=1
		if Enemy.symbol<110:
			if EnemyPlane.symbol<1:
				self.screen.blit(self.plane1,(self.x,self.y))
			elif EnemyPlane.symbol<3:
				self.screen.blit(self.planedown1,(self.x,self.y))
			elif EnemyPlane.symbol<4:
				self.screen.blit(self.planedown2,(self.x,self.y))
			elif EnemyPlane.symbol<5:
				self.screen.blit(self.planedown3,(self.x,self.y))
			else :
				self.screen.blit(self.planedown4,(self.x,self.y))
				Enemy.symbol+=1
		else :
			EnemyPlane.number +=1
	
			
	def Shoot(self):
		
		if random.uniform(1,100)<5:
			Enemy.Bullet1.append(EnemyBullet(self.screen,self.x+25,self.y+39))
			
		for temp in Enemy.Bullet1:
			temp.DrawBullet1()

		
	

class EnemyPlane(object):
	number=0
	Bullet1=[]
	Bullet2=[]
	Bullet3=[]
	Bullet4=[]	
	Bullet5=[]	
	symbol=0
    
	def __init__(self,screen):

		Plane1='./image/enemy2.png'
		PlaneDown1='./image/enemy2_down1.png'
		PlaneDown2='./image/enemy2_down2.png'
		PlaneDown3='./image/enemy2_down3.png'
		PlaneDown4='./image/enemy2_down4.png'
		PlaneDown5='./image/enemy2_down5.png'
		PlaneDown6='./image/enemy2_down6.png'

		self.plane1 =pygame.image.load(Plane1).convert_alpha()
		self.planedown1 =pygame.image.load(PlaneDown1).convert_alpha()
		self.planedown2 =pygame.image.load(PlaneDown2).convert_alpha()
		self.planedown3 =pygame.image.load(PlaneDown3).convert_alpha()
		self.planedown4 =pygame.image.load(PlaneDown4).convert_alpha()
		self.planedown5 =pygame.image.load(PlaneDown5).convert_alpha()
		self.planedown6 =pygame.image.load(PlaneDown6).convert_alpha()
		self.screen=screen
		self.x=160
		self.y=50
		self.move="left"
	
     
	def DrawPlane(self):
			
		if EnemyPlane.symbol<2000:
			self.Move()
		if EnemyPlane.symbol<2400:	
			self.Shoot()   	
			#calculation	
		for temp in PlayerPlane.BulletList:
			if (temp.x>self.x and temp.x<self.x+150) and (temp.y<self.y+200 and temp.y>self.y):
				EnemyPlane.symbol+=1
		if EnemyPlane.symbol<200:
			self.screen.blit(self.plane1,(self.x,self.y))
		elif EnemyPlane.symbol<400:
			self.screen.blit(self.planedown1,(self.x,self.y))
		elif EnemyPlane.symbol<1000:
			self.screen.blit(self.planedown2,(self.x,self.y))
		elif EnemyPlane.symbol<1600:
			self.screen.blit(self.planedown3,(self.x,self.y))
		elif EnemyPlane.symbol<2000:
			self.screen.blit(self.planedown4,(self.x,self.y))
		elif EnemyPlane.symbol<2400:
			self.screen.blit(self.planedown5,(self.x,self.y))
		else :
			self.screen.blit(self.planedown6,(self.x,self.y))
			EnemyPlane.symbol+=1
    
	def Move(self):
	
		if self.x >350:
			self.move="right"
		elif self.x<10:
			self.move="left"
		if cmp(self.move,"right"):
			self.x+=3
		else:
			self.x-=3
		
	def Shoot(self):
		
		if random.uniform(1,100)<1:
			EnemyPlane.Bullet1.append(EnemyBullet(self.screen,self.x+13,self.y+100))
		elif random.uniform(1,100)>99:
			EnemyPlane.Bullet2.append(EnemyBullet(self.screen,self.x+143,self.y+100))
		if random.uniform(100,200)<102:
			EnemyPlane.Bullet3.append(EnemyBullet(self.screen,self.x+30,self.y+200))
		elif random.uniform(100,200)>198:
			EnemyPlane.Bullet4.append(EnemyBullet(self.screen,self.x+125,self.y+200))
		if random.uniform(100,200)<104:
			EnemyPlane.Bullet3.append(EnemyBullet(self.screen,self.x+80,self.y+245))


		for temp in EnemyPlane.Bullet1:
			temp.DrawBullet1()
		for temp in EnemyPlane.Bullet2:
			temp.DrawBullet1()
		for temp in EnemyPlane.Bullet3:
			temp.DrawBullet1()
		for temp in EnemyPlane.Bullet4:
			temp.DrawBullet1()
    	
class EnemyBullet(object):
    
    def __init__(self,screen,x,y):

		bullet='./image/bullet2.png'
		self.bullet=pygame.image.load(bullet).convert_alpha()
		self.screen=screen	
		self.x=x
		self.y=y
	
    def DrawBullet1(self):
		if self.y<800:
			self.y+=2
			self.screen.blit(self.bullet,(self.x,self.y))
		
	
	
    def DrawBullet2(self):
		if self.y<800:
			self.y+=4
			self.screen.blit(self.bullet,(self.x,self.y))

	

if __name__=='__main__':
    
	screen=pygame.display.set_mode((480,700),0,0)

	bgImageFile='./image/background.png'

	background=pygame.image.load(bgImageFile).convert()

	player=PlayerPlane(screen)

	enemyboss=EnemyPlane(screen)

	enemy=Enemy(screen)
	
	
	
	

	#xianshi
	while True:
	
		screen.blit(background,(0,0))
		    
		for event in pygame.event.get():
			if event.type==QUIT:
				print "exit"
				exit()       
		#conduction
		player.Event()
		#draw player's plane and bullets
	
		
		enemy.DrawPlane()
			
			
		if player.symbol<player.defeat:     
			player.DrawPlane()
		if enemyboss.number>1:		
			if enemyboss.symbol<2500:
				enemyboss.DrawPlane()
	
		#flush
		pygame.display.update()
		time.sleep(0.02)



