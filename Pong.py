import pygame, time, random

global balls,swidth,sheight,screen,background, paddles, players

pygame.init()

def puttext(surf,pos,text,font,size,color,flag):
	fontrend=pygame.font.Font(font,size)
	textrend=fontrend.render(text,1,color)
	if flag=="center":
		textpos=textrend.get_rect()
		textpos=(int(swidth/2-textrend.get_rect().width/2),int(sheight/2-textrend.get_rect().height/2))
	elif flag == "left":
		textpos=(surf.get_rect().left+2,surf.get_rect().top)
	elif flag=="right":
		textpos=(surf.get_rect().right-textrend.get_rect().width-2,surf.get_rect().top)
	else:
		textpos=pos
	surf.blit(textrend,textpos)
	
class ball:
	def __init__(self, color):
		global balls
		balls.append(self)
		self.colorname=color
		self.size=int(0.01*sheight)
		self.xpos=random.randint(self.size+5,swidth-self.size-5)
		self.ypos=random.randint(self.size+5,sheight-self.size-5)
		self.xvel=int(swidth*.2)
		self.yvel=random.randint(-100,100)
		if color=="white":
			self.color=pygame.color.Color(255,255,255,100)
		if color=="green":
			self.color=pygame.color.Color(0,255,0,100)
		if color=="blue":
			self.color=pygame.color.Color(0,0,255,100)
		if color=="red":
			self.color=pygame.color.Color(255,0,0,100)
		self.now=time.time()
	def	update(self):
		oldnow=self.now
		self.now=time.time()
		secs=self.now-oldnow
		self.xpos=self.xpos+self.xvel*secs
		self.ypos=self.ypos+self.yvel*secs

		paddle=False
#		Paddle collision check
		if self.xpos+self.size>=paddles[1].xpos and self.ypos>=paddles[1].ypos and self.ypos<=paddles[1].ypos+paddles[1].height:
			self.xvel=self.xvel*-1.10
			self.xpos=2*paddles[1].xpos-self.xpos-2*self.size
			self.yvel=self.yvel+paddles[1].yvel*0.3
			paddle=True
		if self.xpos-self.size<=paddles[0].xpos+paddles[0].width and self.ypos>=paddles[0].ypos and self.ypos<=paddles[0].ypos+paddles[0].height:
			self.xvel=self.xvel*-1.10
			self.xpos=2*(paddles[0].xpos+paddles[0].width)-self.xpos+self.size*2
			self.yvel=self.yvel+paddles[0].yvel*0.3
			paddle=True

		if not paddle: # did not hit paddle
			if self.xpos+self.size>=swidth:
#				self.xvel=self.xvel*-1
				self.xpos=2*swidth-self.xpos-2*self.size
				players[0].score=players[0].score+1
				self.xvel=int(swidth*-0.2)
#				ball(10,50,50,120,100,"white")
			elif self.xpos-self.size<0:
#				self.xvel=self.xvel*-1
				self.xpos=-1*self.xpos+self.size*2
				players[1].score=players[1].score+1
				self.xvel=int(swidth*0.2)
			if self.ypos+self.size>=sheight:
				self.yvel=self.yvel*-1
#					ball(10,50,50,120,100,"blue")
				self.ypos=2*sheight-self.ypos-2*self.size
			elif self.ypos-self.size<0:
				self.yvel=self.yvel*-1
#				ball(10,50,50,120,100,"green")
				self.ypos=self.ypos*-1+self.size*2
		
#		print(str(self.xpos)+"  -  "+str(self.ypos))
	def draw(self):		
		pygame.draw.circle(screen,self.color,(self.xpos,self.ypos),self.size,self.size)
	def erase(self):		
		pygame.draw.circle(screen,background,(self.xpos,self.ypos),self.size,self.size)




class paddle:
	def __init__(self, xpos, ypos, color):
		global paddles
		paddles.append(self)
		self.height=int(sheight*0.2)
		self.width=int(sheight*0.01)
		self.xpos=xpos
		self.ypos=ypos
		self.xvel=0
		self.yvel=0
		if color=="white":
			self.color=pygame.color.Color(255,255,255,100)
		if color=="green":
			self.color=pygame.color.Color(0,255,0,100)
		if color=="blue":
			self.color=pygame.color.Color(0,0,255,100)
		if color=="red":
			self.color=pygame.color.Color(255,0,0,100)
		self.now=time.time()
	def	update(self):
		oldnow=self.now
		self.now=time.time()
		secs=self.now-oldnow
		self.xpos=self.xpos+self.xvel*secs
		self.ypos=self.ypos+self.yvel*secs
		if self.ypos+self.height>=sheight:
			self.ypos=sheight-self.height
		elif self.ypos<0:
			self.ypos=0
	def draw(self):		
		pygame.draw.rect(screen,self.color,pygame.Rect(self.xpos,self.ypos,self.width,self.height))
	def erase(self):		
		pygame.draw.rect(screen,background,pygame.Rect(self.xpos,self.ypos,self.width,self.height))

class scoreboard:
	def __init__(self):
		self.width=int(swidth/5)
		self.height=int(sheight/5)
		self.board=pygame.Surface((self.width,self.height));
	def erase(self):
		self.board.fill(pygame.color.Color(0,0,0,0))
	def draw(self):
		self.board.fill(pygame.color.Color(30,30,220,150))
		puttext(self.board,(int(self.width*.05),int(self.height*.05)),"Player 1: "+str(players[0].score),None,30,(220,20,150,180),None)
		puttext(self.board,(int(self.width*.05),int(self.height*.55)),"Player 2: "+str(players[1].score),None,30,(220,20,150,180),None)
		screen.blit(self.board,(int(swidth/2)-int(self.width/2),sheight-self.height))		

class player:
	def __init__(self,name,paddle):
		global players
		self.name=name
		self.paddle=paddle
		self.score=0
		players.append(self)
	def addpoint(self):
		self.score=self.score+1

inf=pygame.display.Info()
swidth=int(inf.current_w)
sheight=int(inf.current_h)

red=0
blue=0
green=0

screen=pygame.display.set_mode((swidth,sheight),pygame.FULLSCREEN)
background=pygame.color.Color(red,green,blue,255)

screen.fill(background)

puttext(screen,(int(swidth/2),int(sheight/2)),"Let's Play Pong!!!",None,30,(220,20,150,180),"center")
pygame.display.flip()
time.sleep(2)

screen.fill(background)

now=time.time()

balls=[]
paddles=[]
players=[]
sboard=scoreboard()

ball("green")
paddle(0,30,"red")
paddle(swidth-10,30,"blue")
player("Bob",paddles[0])
player("Fred",paddles[1])

akey=False
zkey=False
upkey=False
downkey=False
winner=0

while True:
#			pygame.event.pump()
# key handling
			keysup=pygame.event.get(pygame.KEYUP)
			keysdown=pygame.event.get(pygame.KEYDOWN)
			if time.time()-now >= 0.01:
					pygame.event.get()

			paddles[0].yvel=0
			paddles[1].yvel=0
            
			if len(keysup)>0:
				for a in keysup:
					if a.key == pygame.K_ESCAPE:
						exit()
					if a.key==pygame.K_UP:
						upkey=False
					if a.key==pygame.K_DOWN:
						downkey=False
					if a.key==pygame.K_a:
						akey=False
					if a.key==pygame.K_z:
						zkey=False
			if len(keysdown)>0:
				for a in keysdown:
					if a.key==pygame.K_UP:
						upkey=True
					if a.key==pygame.K_DOWN:
						downkey=True
					if a.key==pygame.K_a:
						akey=True
					if a.key==pygame.K_z:
						zkey=True

			if akey:
						paddles[0].yvel=paddles[0].yvel+int(-1*sheight*.2)
			if zkey:
						paddles[0].yvel=paddles[0].yvel+int(sheight*.2)
			if upkey:
						paddles[1].yvel=paddles[1].yvel+int(-1*sheight*.2)
			if downkey:
						paddles[1].yvel=paddles[1].yvel+int(sheight*.2)

#erase all
			sboard.erase()
			for p in paddles:
				p.erase()

			for b in balls:
				b.erase()

#update and draw all
			sboard.draw()
			for p in paddles:
				p.update()
				p.draw()

			for b in balls:
				b.update()
				b.draw()

			if players[0].score>=10:
				winner=1
				break
			if players[1].score>=10:
				winner=2
				break

			if time.time()-now >= 0.005:
					now=time.time()
#					background=pygame.color.Color(red,green,blue,100)
#					screen.fill(background)	
					pygame.display.flip()
		
screen.fill(background)
puttext(screen,(int(swidth/2),int(sheight/2)),"PLAYER "+str(winner)+" WINS!!!!!",None,90,(220,20,150,180),"center")
pygame.display.flip()
time.sleep(4)
screen.fill(background)
		
		
		
		
		


			