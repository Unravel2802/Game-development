import pygame, time, random, math

pygame.init()

white = (255,255,255,255)
black = (0,0,0,255)
red = (191,11,32,255)
blue = (0,0,255,255)
wood = (186,140,99,255)
milk = (245,244,211,255)
chosen = (186,255,36,255)
pink = (220,20,150,180)

turn = 0

w=640
h=700

now=time.time()

a=80


def puttext(surf,pos,text,font,size,color,flag):
	fontrend=pygame.font.Font(font,size)
	textrend=fontrend.render(text,1,color)
	if flag=="center":
		textpos=textrend.get_rect()
		textpos=(int(w/2-textrend.get_rect().width/2),int(h/2-textrend.get_rect().height/2))
	elif flag == "left":
		textpos=(surf.get_rect().left+2,surf.get_rect().top)
	elif flag=="right":
		textpos=(surf.get_rect().right-textrend.get_rect().width-2,surf.get_rect().top)
	else:
		textpos=pos
	surf.blit(textrend,textpos)

class square:
	def __init__(self,xpos,ypos):
		squares.append(self)
		self.xpos=xpos
		self.ypos=ypos
		self.wpiece=False
		self.rpiece=False
		self.isSelect=False	
		self.isKing=False
		self.isMoved=False
		
	def draw(self):
		if ((self.xpos+self.ypos-60)/a)%2==1:
			pygame.draw.rect(board, black,[self.xpos,self.ypos,a,a])
		elif (self.xpos+self.ypos-60)/a%2==0:
			pygame.draw.rect(board, milk,[self.xpos,self.ypos,a,a])
	
	def update(self):
		if self.wpiece==True:
			pygame.draw.circle(board, white, [self.xpos+40, self.ypos+40], 30)
		elif self.rpiece==True:
			pygame.draw.circle(board, red, [self.xpos+40, self.ypos+40], 30)
		#Red move
		if self.isSelect==True and self.rpiece==True:
			(x1,y1)=pygame.mouse.get_pos()	
			if y1>80:
				p=cboard.index([x1-(x1%80),y1-(y1%80)-20])
			else:
				p=cboard.index([x1-(x1%80),y1-20])
			rsx=self.xpos+80
			rsy=self.ypos-80 
			r2sx=self.xpos+160
			r2sy=self.ypos-160					
			if rsx<640 and rsy>0:
				rsp=cboard.index([rsx,rsy])
			if r2sx<640 and r2sy>0:
				r2sp=cboard.index([r2sx,r2sy])
			sp=cboard.index([self.xpos,self.ypos])
			lsx=self.xpos-80
			lsy=self.ypos-80
			l2sx=self.xpos-160
			l2sy=self.ypos-160
			if lsx>=0 and lsy>0:	
				lsp=cboard.index([lsx,lsy])
			if l2sx>=0 and l2sy>0:	
				l2sp=cboard.index([l2sx,l2sy])			
				
			if self.ypos==60:
				self.isKing=True
					
			if self.isKing==True:
				rsxd=self.xpos+80
				rsyd=self.ypos+80			
				r2sxd=self.xpos+160
				r2syd=self.ypos+160
				if rsxd<640 and rsyd>0:
					rspd=cboard.index([rsxd,rsyd])
				if r2sxd<640 and r2syd>0:
					r2spd=cboard.index([r2sxd,r2syd])
				lsxd=self.xpos-80
				lsyd=self.ypos+80
				l2sxd=self.xpos-160
				l2syd=self.ypos+160			
				if l2sxd>=0 and l2syd>0:
					l2spd=cboard.index([l2sxd,l2syd])	
				if lsxd>=0 and lsyd>0:	
					lspd=cboard.index([lsxd,lsyd])									
			#Red move	
			#Red capture up right side 
			if pygame.mouse.get_pressed()==(0,0,1) and (x1-x1%80, y1-y1%80-20)==(self.xpos,self.ypos):
				isSelect=False
			if pygame.mouse.get_pressed()==(1,0,0) and rsx<640 and rsy>60 and squares[rsp].wpiece==True and (x1-x1%80, y1-y1%80-20)==(self.xpos+160,self.ypos-160):	
				if r2sx<640 and squares[r2sp].wpiece==True:
					self.isMoved=False
				else:
					if self.isKing==True:
						squares[r2sp].isKing=True
						self.isKing=False				
					self.rpiece=False
					squares[p].rpiece=True
					squares[rsp].wpiece=False
					squares[rsp].isKing=False
					rpieces.append([r2sx,r2sy])
					rpieces.remove([self.xpos,self.ypos])
					wpieces.remove([rsx,rsy])
					pygame.draw.circle(board,black, [rsx+40, rsy+40], 31)
					pygame.draw.circle(board,black, [self.xpos+40, self.ypos+40], 31)
					self.isSelect=False
			#Red capture white left side	
			elif pygame.mouse.get_pressed()==(1,0,0) and lsx>=0 and lsy>60 and squares[lsp].wpiece==True and (x1-x1%80, y1-y1%80-20)==(self.xpos-160,self.ypos-160):
				if l2sx>0 and squares[l2sp].wpiece==True:
					self.isSelect=False
					self.isMoved=False
				else:
					if self.isKing==True:
						squares[l2sp].isKing=True
						self.isKing=False				
					squares[p].rpiece=True
					self.rpiece=False
					squares[lsp].wpiece=False
					squares[lsp].isKing=False
					rpieces.append([l2sx,l2sy])
					rpieces.remove([self.xpos,self.ypos])					
					wpieces.remove([lsx,lsy])
					pygame.draw.circle(board,black, [lsx+40, lsy+40], 31)
					pygame.draw.circle(board,black, [self.xpos+40, self.ypos+40], 31)	
					self.isSelect=False
			#Red move up right		
			elif pygame.mouse.get_pressed()==(1,0,0) and rsy>0 and (x1-x1%80,y1-y1%80-20)==(self.xpos+80, self.ypos-80):
				if rsx<640 and (squares[rsp].rpiece==True or squares[rsp].wpiece==True):
					self.isSelect=False
					self.isMoved=False
				else:
					if self.isKing==True:
						squares[p].isKing=True
						self.isKing=False
					squares[p].rpiece=True
					self.rpiece=False
					rpieces.append([squares[p].xpos,squares[p].ypos])
					rpieces.remove([self.xpos,self.ypos])						
					pygame.draw.circle(board, black, [self.xpos+40, self.ypos+40], 31)
					self.isSelect=False
			#Red move up left
			elif pygame.mouse.get_pressed()==(1,0,0) and lsy>0 and (x1-x1%80,y1-y1%80-20)==(self.xpos-80, self.ypos-80):
				if lsx>=0 and (squares[lsp].rpiece==True or squares[lsp].wpiece==True):
					self.isSelect=False
					self.isMoved=False
				else:
					if self.isKing==True:
						squares[p].isKing=True
						self.isKing=False					
					self.rpiece=False
					squares[p].rpiece=True
					rpieces.append([squares[p].xpos,squares[p].ypos])
					rpieces.remove([self.xpos,self.ypos])	
					pygame.draw.circle(board, black, [self.xpos+40, self.ypos+40], 31)
					self.isMoved=True
					self.isSelect=False		
			#Red king capture down right
			elif pygame.mouse.get_pressed()==(1,0,0) and self.isKing==True and rsxd<640 and squares[rspd].wpiece==True and (x1-x1%80, y1-y1%80-20)==(self.xpos+160,self.ypos+160):
				if r2sxd<640 and squares[r2spd].wpiece==True:
					self.isSelect=False
					self.isMoved=False	
				else:
					self.rpiece=False
					self.isKing=False					
					squares[r2spd].rpiece=True
					squares[r2spd].isKing=True
					squares[rspd].wpiece=False
					rpieces.append([r2sxd,r2syd])
					rpieces.remove([self.xpos,self.ypos])	
					wpieces.remove([rsxd,rsyd])
					pygame.draw.circle(board,black, [rsxd+40, rsyd+40], 31)
					pygame.draw.circle(board,black, [self.xpos+40, self.ypos+40], 31)
					self.isSelect=False	
			#Red king capture down left
			elif pygame.mouse.get_pressed()==(1,0,0) and self.isKing ==True and lsxd>0 and squares[lspd].wpiece==True and (x1-x1%80, y1-y1%80-20)==(self.xpos-160,self.ypos+160):
				if l2sxd>0 and squares[l2spd].wpiece==True:
					self.isSelect=False
					self.isMoved=False
				else:	

					self.rpiece=False
					self.isKing=False
					squares[l2spd].rpiece=True
					squares[l2spd].isKing=True
					squares[lspd].wpiece=False
					rpieces.append([l2sxd,l2syd])
					rpieces.remove([self.xpos,self.ypos])	
					wpieces.remove([lsxd,lsyd])
					pygame.draw.circle(board,black, [lsxd+40, lsyd+40], 31)
					pygame.draw.circle(board,black, [self.xpos+40, self.ypos+40], 31)
					self.isSelect=False
			#Red king move down right			
			elif pygame.mouse.get_pressed()==(1,0,0) and self.isKing==True and rsyd>0 and (x1-x1%80,y1-y1%80-20)==(self.xpos+80, self.ypos+80):
				if rsxd<640 and (squares[rspd].wpiece==True or squares[rspd].rpiece==True):
					self.isSelect=False
					self.isMoved=False
				else:	
					self.isKing=False
					self.rpiece=False
					squares[p].rpiece=True
					squares[p].isKing=True						
					rpieces.append([squares[p].xpos,squares[p].ypos])
					rpieces.remove([self.xpos,self.ypos])	
					pygame.draw.circle(board, black, [self.xpos+40, self.ypos+40], 31)
					self.isSelect=False
			#Red king move down left		
			elif pygame.mouse.get_pressed()==(1,0,0) and self.isKing==True and lsyd>0 and (x1-x1%80,y1-y1%80-20)==(self.xpos-80, self.ypos+80):
				if lsxd>0 and (squares[lspd].wpiece==True or squares[lspd].rpiece==True):
					self.isSelect=False
					self.isMoved=False
				else:
					self.rpiece=False
					self.isKing=False
					squares[p].rpiece=True
					squares[p].isKing=True						
					rpieces.append([squares[p].xpos,squares[p].ypos])
					rpieces.remove([self.xpos,self.ypos])	
					pygame.draw.circle(board, black, [self.xpos+40, self.ypos+40], 31)
					self.isSelect=False

						
		#White move		
		elif self.isSelect==True and self.wpiece==True:
			(x1,y1)=pygame.mouse.get_pos()
			if y1>80:
				p=cboard.index([x1-(x1%80),y1-(y1%80)-20])
			else:
				p=cboard.index([x1-(x1%80),60])
			rsx=self.xpos+80
			rsy=self.ypos+80
			if rsx<640 and rsy<700 and rsy>0:
				rsp=cboard.index([rsx,rsy])
			r2sx=self.xpos+160
			r2sy=self.ypos+160
			if r2sx<640 and r2sy<700 and r2sy>0:
				r2sp=cboard.index([r2sx,r2sy])
			lsx=self.xpos-80
			lsy=self.ypos+80
			l2sx=self.xpos-160
			l2sy=self.ypos+160				
	
			if lsx>=0 and lsy<700 and lsy>=0:
				lsp=cboard.index([lsx,lsy])
			if l2sx>=0 and l2sx<640 and l2sy<700 and l2sy>0:
				l2sp=cboard.index([l2sx,l2sy])		
			sp=cboard.index([self.xpos,self.ypos])
			
			if self.ypos==620:
				self.isKing=True
				
			if self.isKing==True:
				rsxu=self.xpos+80
				rsyu=self.ypos-80
				r2sxu=self.xpos+160
				r2syu=self.ypos-160
				if rsxu<640 and rsyu<700 and rsyu>0:
					rspu=cboard.index([rsxu,rsyu])
				if r2sxu<640 and r2syu>0:
					r2spu=cboard.index([r2sxu,r2syu])	
				lsxu=self.xpos-80
				lsyu=self.ypos-80
				l2sxu=self.xpos-160
				l2syu=self.ypos-160	
				if lsxu>=0 and lsyu>0:	
					lspu=cboard.index([lsxu,lsyu])	
				if l2sxu>=0 and l2syu>0:
					l2spu=cboard.index([l2sxu,l2syu])	
			#White king capture up right
			if pygame.mouse.get_pressed()==(1,0,0) and self.isKing==True and rsxu<640 and rsxu>0 and squares[rspu].rpiece==True and (x1-x1%80, y1-y1%80-20)==(self.xpos+160,self.ypos-160):	
				if r2sxu<640 and squares[r2spu].rpiece==True:
					self.isSelect=False
					self.isMoved=False
				else:
					self.wpiece=False
					self.isKing=False
					squares[r2spu].wpiece=True
					squares[r2spu].isKing=True
					squares[rspu].rpiece=False
					wpieces.append([r2sxu,r2syu])
					wpieces.remove([self.xpos,self.ypos])	
					rpieces.remove([rsxu,rsyu])
					pygame.draw.circle(board,black, [rsxu+40, rsyu+40], 31)
					pygame.draw.circle(board,black, [self.xpos+40, self.ypos+40], 31)
					self.isSelect=False
			#White king capture up left 	
			elif pygame.mouse.get_pressed()==(1,0,0) and self.isKing==True and lsxu<640 and lsxu>0 and squares[lspu].rpiece==True and (x1-x1%80, y1-y1%80-20)==(self.xpos-160,self.ypos-160):
				if l2sxu>0 and squares[l2spu].rpiece==True:
					self.isSelect=False
					self.isMoved=False
				else:
					self.wpiece=False
					self.isKing=False
					squares[l2spu].wpiece=True
					squares[l2spu].isKing=True
					squares[lspu].rpiece=False
					wpieces.append([l2sxu,l2syu])
					wpieces.remove([self.xpos,self.ypos])	
					rpieces.remove([lsxu,lsyu])
					pygame.draw.circle(board,black, [lsxu+40, lsyu+40], 31)
					pygame.draw.circle(board,black, [self.xpos+40, self.ypos+40], 31)	
					self.isSelect=False
			#White king move up right		
			elif pygame.mouse.get_pressed()==(1,0,0) and self.isKing==True and rsy>0 and (x1-x1%80,y1-y1%80-20)==(self.xpos+80, self.ypos-80):
				if rsxu<640 and (squares[rspu].rpiece==True or squares[rspu].wpiece==True):
					self.isSelect=False
					self.isMoved=False
				else:
					self.wpiece=False
					self.isKing=False
					squares[p].isKing=True
					squares[p].wpiece=True
					wpieces.append([squares[p].xpos,squares[p].ypos])
					wpieces.remove([self.xpos,self.ypos])	
					pygame.draw.circle(board, black, [self.xpos+40, self.ypos+40], 31)
					self.isSelect=False
			#White king move up left
			elif pygame.mouse.get_pressed()==(1,0,0) and self.isKing==True and lsy>0 and (x1-x1%80,y1-y1%80-20)==(self.xpos-80, self.ypos-80):
				if lsxu>0 and (squares[lspu].rpiece==True or squares[lspu].wpiece==True):
					self.isSelect=False
					self.isMoved=False
				else:	
					self.isKing=False
					self.wpiece=False					
					squares[p].isKing=True
					squares[p].wpiece=True
					wpieces.append([squares[p].xpos,squares[p].ypos])
					wpieces.remove([self.xpos,self.ypos])	
					pygame.draw.circle(board, black, [self.xpos+40, self.ypos+40], 31)
					self.isMoved=True
					self.isSelect=False			

			#White capture down right 	
			elif pygame.mouse.get_pressed()==(1,0,0) and rsx<640 and rsy<700 and squares[rsp].rpiece==True and (x1-x1%80, y1-y1%80-20)==(self.xpos+160,self.ypos+160):
				if r2sx<640 and squares[r2sp].rpiece==True:
					self.isSelect=False
					self.isMoved=False	
				else:
					if self.isKing==True:
						squares[rsp].isKing=True
						self.isKing=False				
					self.wpiece=False
					squares[p].wpiece=True
					squares[rsp].rpiece=False
					squares[rsp].isKing=False
					wpieces.append([r2sx,r2sy])
					wpieces.remove([self.xpos,self.ypos])
					rpieces.remove([rsx,rsy])	
					pygame.draw.circle(board,black, [rsx+40, rsy+40], 31)
					pygame.draw.circle(board,black, [self.xpos+40, self.ypos+40], 31)
					self.isSelect=False
			#White capture down left 
			elif pygame.mouse.get_pressed()==(1,0,0) and lsx>=0 and lsy<700 and squares[lsp].rpiece==True and (x1-x1%80, y1-y1%80-20)==(self.xpos-160,self.ypos+160):
				if l2sx>0 and squares[l2sp].rpiece==True:
					self.isSelect=False
					self.isMoved=False
				else:	
					if self.isKing==True:
						squares[lsp].isKing=True
						self.isKing=False				
					self.wpiece=False					
					squares[p].wpiece=True
					squares[lsp].isKing=False
					squares[lsp].rpiece=False
					wpieces.append([l2sx,l2sy])
					wpieces.remove([self.xpos,self.ypos])
					rpieces.remove([lsx,lsy])	
					pygame.draw.circle(board,black, [lsx+40, lsy+40], 31)
					pygame.draw.circle(board,black, [self.xpos+40, self.ypos+40], 31)
					self.isSelect=False
			#White move down right			
			elif pygame.mouse.get_pressed()==(1,0,0) and (x1-x1%80,y1-y1%80-20)==(self.xpos+80, self.ypos+80):
				if rsx<640 and (squares[rsp].wpiece==True or squares[rsp].rpiece==True):
					self.isSelect=False
					self.isMoved=False
				else:	
					if self.isKing==True:
						squares[p].isKing=True
						self.isKing=False
					self.wpiece=False
					squares[p].wpiece=True
					wpieces.append([squares[p].xpos,squares[p].ypos])
					wpieces.remove([self.xpos,self.ypos])	
					pygame.draw.circle(board, black, [self.xpos+40, self.ypos+40], 31)
					self.isSelect=False
			#White move down left		
			elif pygame.mouse.get_pressed()==(1,0,0) and (x1-x1%80,y1-y1%80-20)==(self.xpos-80, self.ypos+80):
				if lsx>0 and (squares[lsp].wpiece==True or squares[lsp].rpiece==True):
					self.isSelect=False
					self.isMoved=False
				else:	
					if self.isKing==True:
						squares[p].isKing=True
						self.isKing=False
					self.wpiece=False
					squares[p].wpiece=True
					wpieces.append([squares[p].xpos,squares[p].ypos])
					wpieces.remove([self.xpos,self.ypos])	
					pygame.draw.circle(board, black, [self.xpos+40, self.ypos+40], 31)
					self.isSelect=False

			
class player:
	def __init__(self,name,color):
		global players
		self.name=name
		self.paddle=paddle
		self.score=0
		players.append(self)
							
board = pygame.display.set_mode((w,h))
squares = []
cboard = []
pieces = []
wpieces = []	
rpieces = []

highlights=[]
pygame.display.update()

newxPos = 0
newyPos = 0 

x=0
y=60
c=0
r=0
rows, cols = (64, 2)	
cboard = [[0 for i in range(cols)] for j in range(rows)]
while r<64:
	while x<640:
		cboard[r][0]=x
		x+=80
		r+=1
	x=0
while c<64:
	cboard[c][1]=(int)(c/8)*80+60
	c+=1		
for s in cboard:
	square(s[0],s[1])

def select():
	if pygame.mouse.get_pressed()==(1,0,0) and board.get_at(pygame.mouse.get_pos())==red:
		newP=pygame.mouse.get_pos()
		pos=cboard.index([newP[0]-(newP[0]%80),newP[1]-(newP[1]%80)-20])
		squares[pos].isSelect=True
	
	
end = False

p=0

count=1

while count < 24:
	if count==1 or count==3 or count==5:
		squares[count].wpiece = True
		wpieces.append([squares[count].xpos,squares[count].ypos])
		count+=2
		continue		
	if count==7:
		squares[count].wpiece = True	
		wpieces.append([squares[count].xpos,squares[count].ypos])
	if count==8 or count==10 or count==12 or count==14:
		squares[count].wpiece = True
		wpieces.append([squares[count].xpos,squares[count].ypos])
		count+=2
		continue	
	if count==17 or count==19 or count==21 or count==23:
		squares[count].wpiece = True
		wpieces.append([squares[count].xpos,squares[count].ypos])
		count+=2
		continue
	else:	
		count+=1
count2=40
while count2 < 64:
	if count2==40 or count2==42 or count2==44 or count2==46:
		squares[count2].rpiece = True
		rpieces.append([squares[count2].xpos,squares[count2].ypos])
		count2+=2
		continue		
	if count2==49 or count2==51 or count2==53:
		squares[count2].rpiece = True
		rpieces.append([squares[count2].xpos,squares[count2].ypos])
		count2+=2
		continue
	if count2==55:
		squares[count2].rpiece = True				
		rpieces.append([squares[count2].xpos,squares[count2].ypos])
	if count2==56 or count2==58 or count2==60 or count2==62:
		squares[count2].rpiece = True
		rpieces.append([squares[count2].xpos,squares[count2].ypos])
		count2+=2
		continue
	else:	
		count2+=1				

for s in squares:
	s.draw()
puttext(board, [w/2-120, 0], "Player 1", None,90,(220,20,150,180), None)		
				
while not end:	
	keysup=pygame.event.get(pygame.KEYUP)
	keysdown=pygame.event.get(pygame.KEYDOWN)
	if time.time()-now >= 0.01:
					pygame.event.get()
	if len(keysup)>0:
				for a in keysup:
					if a.key == pygame.K_ESCAPE:
						exit()			
	if turn%2==0:
		for s in squares:
			s.update()
		if turn>0:				
			puttext(board, [w/2-120, 0], "Player 2", None, 90, black, None)	
		puttext(board, [w/2-120, 0], "Player 1", None, 90, pink, None)					
		if pygame.mouse.get_pressed()==(1,0,0) and board.get_at(pygame.mouse.get_pos())==red:
			newP=pygame.mouse.get_pos()
			if newP[1]>80 and newP[1]%80<50:
				pos=cboard.index([newP[0]-(newP[0]%80), newP[1]-(newP[1]%80)-20])
				pygame.draw.circle(board, (186, 255, 36), [newP[0]-(newP[0]%80)+40, newP[1]-(newP[1]%80)+20], 31, 1)
			elif newP[1]>80 and newP[1]%80>=50:
				pos=cboard.index([newP[0]-(newP[0]%80), newP[1]-(newP[1]%80)+60])
				pygame.draw.circle(board, (186, 255, 36), [newP[0]-(newP[0]%80)+40, newP[1]-(newP[1]%80)+100], 31, 1)				
			else: 
				pos=cboard.index([newP[0]-(newP[0]%80),60])	
				pygame.draw.circle(board, (186, 255, 36), [newP[0]-(newP[0]%80)+40, newP[1]-(newP[1]%80)+20], 31, 1)
			squares[pos].isSelect=True
			for s in squares:
				s.update()
			turn+=1
		for s in squares:
			s.update()
			
	if turn%2!=0:			
		for s in squares:
			s.update()
		puttext(board, [w/2-120, 0], "Player 1", None, 90, black, None)						
		puttext(board, [w/2-120, 0], "Player 2", None, 90, pink, None)
		
		if pygame.mouse.get_pressed()==(1,0,0) and pygame.Surface.get_at(board, (pygame.mouse.get_pos()))==white:
			newP=pygame.mouse.get_pos()
			if newP[1]>80 and newP[1]%80<50:
				pos=cboard.index([newP[0]-(newP[0]%80), newP[1]-(newP[1]%80)-20])
				pygame.draw.circle(board, (186, 255, 36), [newP[0]-(newP[0]%80)+40, newP[1]-(newP[1]%80)+20], 31, 1)
			elif newP[1]>80 and newP[1]%80>=50:
				pos=cboard.index([newP[0]-(newP[0]%80), newP[1]-(newP[1]%80)+60])
				pygame.draw.circle(board, (186, 255, 36), [newP[0]-(newP[0]%80)+40, newP[1]-(newP[1]%80)+20], 31, 1)				
			else: 
				pos=cboard.index([newP[0]-(newP[0]%80),60])	
				pygame.draw.circle(board, (186, 255, 36), [newP[0]-(newP[0]%80)+40, newP[1]-(newP[1]%80)+20], 31, 1)
			squares[pos].isSelect=True	
			for s in squares:
				s.update()	
			turn+=1	
		for s in squares:
			s.update()	
		for s in squares:
			if s.wpiece==True:
				continue
	if len(rpieces)==0:		
		puttext(board, [w/2-220, h/2], "Player 2 Wins!", None,90,pink, None)
		
	if len(wpieces)==0:		
		puttext(board, [w/2-220, h/2], "Player 1 Wins!", None,90,pink, None)	
	pygame.display.update()			