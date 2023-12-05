#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Created on Fri Mar  6 16:58:41 2020

@author: anushka
"""

import pygame
import sys

pygame.init()

pygame.display.set_caption("SLITHER" )

class Snake():
	
	def changeDirection(self,dir):
		if dir=="RIGHT" and not self.direction=="LEFT":
			self.direction = "RIGHT"
		elif dir=="LEFT" and not self.direction=="RIGHT":
			self.direction = "LEFT"
		elif dir=="UP" and not self.direction=="DOWN":
			self.direction = "UP"
		elif dir=="DOWN" and not self.direction=="UP":
			self.direction = "DOWN"
			
	def move(self):
		if self.direction == "RIGHT":
			self.position[0] = self.position[0] + 10
		elif self.direction == "LEFT":
			self.position[0] = self.position[0] - 10
		elif self.direction == "UP":
			self.position[1] = self.position[1] - 10
		elif self.direction == "DOWN":
			self.position[1] = self.position[1] + 10
		self.body.insert(0,list(self.position))
		
	def snake_head(self):
		return self.position
	
	def getBody(self):
		return self.body
		
	
class Snake_1(Snake):
	def __init__(self):
		self.position =[400,100]
		self.body=[[400,100],[400,100],[400,100]]
		self.direction = "DOWN"
		
	def checkCollision(self,snake2):
		if self.position[0] > 490 or self.position[0] < 10:
			return 1
		elif self.position[1] > 500 or self.position[1] < 10:
			return 1
		for bodyPart in snake2.body[1:]:
			if self.position == bodyPart:
				return 1
		for bodyPart in self.body[1:]:
			if self.position == bodyPart:
				return 1
		return 0
	
	
class Snake_2(Snake):
	def __init__(self):
		self.position =[100,400]
		self.body=[[100,400],[100,400],[100,400]]
		self.direction = "UP"

	def checkCollision(self,snake1):
		if self.position[0] > 490 or self.position[0] < 10:
			return 1
		elif self.position[1] > 500 or self.position[1] < 10:
			return 1
		for bodyPart in snake1.body[1:]:
			if self.position == bodyPart:
				return 1
		for bodyPart in self.body[1:]:
			if self.position == bodyPart:
				return 1
		return 0
	

window = pygame.display.set_mode((500 + 20, 500 + 20))
py_clock=pygame.time.Clock()

#Fonts
font = pygame.font.SysFont('Agency FB',30,True)
smallfont = pygame.font.SysFont('Agency FB',20,True)

#Displaying text
def screen_text(text, font, color, x, y):
	textobj = font.render(text,1,color)
	window.blit(textobj,(x,y))

def gameStart():
	click = False
	while True:
		window.fill(pygame.Color(0,0,0))
		screen_text("Welcome Serpents", font,(240,255,255), 160,80)
		screen_text("How to play:", font,(255,255,255), 200,130)
		screen_text("Serpent that survives the longest wins.", smallfont,(208,208,208), 125,180)
		screen_text("You will lose if you colliside.", smallfont,(208,208,208), 160,210)
		screen_text("Player 1: Use WASD                  Player 2: Use arrow keys", smallfont,(255,255,255), 80,250)
		screen_text("Press Start to begin the game", font,(255,255,255), 110,320)
		
		mx, my = pygame.mouse.get_pos() 
		
		#Start Button creation
		start = pygame.Rect(215, 395, 100, 50)
		if start.collidepoint((mx,my)):
			if click:
				snake1 = Snake_1()
				snake2 = Snake_2()
				mainGame(snake1, snake2, 0,0)
		pygame.draw.rect(window, (162,67,67), start)
		screen_text("START", font,(255,255,255), 232,400)
		
		click = False
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True
		
		pygame.display.update()
		py_clock.tick(20)

def gameOver(score1,score2):
	click = False
	while True:
		window.fill(pygame.Color(0,0,0))
		if (score1>score2):
			winner_text = font.render("Congratulations! Player " + str(1) + " is winning",200,(255,255,255))
			window.blit(winner_text,(80,90))
		elif (score1<score2):
			winner_text = font.render("Congratulations! Player " + str(2) + " is winning",200,(255,255,255))
			window.blit(winner_text,(100,90))
		else:
			winner_text = font.render("Congratulations! Both players with equal score",200,(255,255,255))
			window.blit(winner_text,(25,90))

		score_text = font.render("Scores - Player 1: " + str(score1) + "   Player 2: " + str(score2),200,(208,208,208))
		window.blit(score_text,(100,150))
        
		mx, my = pygame.mouse.get_pos()
		
		#continue, new game, quit buttons
		conti_game = pygame.Rect(170, 220, 200, 50)
		new_game = pygame.Rect(170, 280, 200, 50)
		game_quit = pygame.Rect(170, 340, 200, 50)
		if conti_game.collidepoint((mx,my)):
			if click:
				snake1 = Snake_1()
				snake2 = Snake_2()
				mainGame(snake1, snake2, score1,score2)
		if new_game.collidepoint((mx,my)):
			if click:
				snake1 = Snake_1()
				snake2 = Snake_2()
				mainGame(snake1, snake2, 0,0)
		if game_quit.collidepoint((mx,my)):
			if click:
				pygame.quit()
				sys.exit()
		pygame.draw.rect(window, (150,187,154), conti_game)
		screen_text("CONTINUE", font,(255,255,255), 220,225)
		pygame.draw.rect(window, (93,118,167), new_game)
		screen_text("NEW GAME", font,(255,255,255), 220,285)
		pygame.draw.rect(window, (162,67,67), game_quit)
		screen_text("QUIT", font,(255,255,255), 245,345)
        
		click = False
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True
		        
		pygame.display.update()
		py_clock.tick(20)

def mainGame(snake1, snake2, score1,score2):
	move1 = 0
	move2 = 0
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameOver(score1,score2)
			
			key_pressed1 = pygame.key.get_pressed()
			key_pressed2 = pygame.key.get_pressed()
			
		
			if key_pressed1[pygame.K_RIGHT]:
				snake1.changeDirection("RIGHT")
			elif key_pressed1[pygame.K_LEFT]:
				snake1.changeDirection("LEFT")
			elif key_pressed1[pygame.K_UP]:
				snake1.changeDirection("UP")
			elif key_pressed1[pygame.K_DOWN]:
				snake1.changeDirection("DOWN")
			elif key_pressed1[pygame.K_ESCAPE]:
				running = False
				gameOver(score1,score2)
			
			if key_pressed2[pygame.K_d]:
				snake2.changeDirection("RIGHT")
			elif key_pressed2[pygame.K_a]:
				snake2.changeDirection("LEFT")
			elif key_pressed2[pygame.K_w]:
				snake2.changeDirection("UP")
			elif key_pressed2[pygame.K_s]:
				snake2.changeDirection("DOWN")
			elif key_pressed2[pygame.K_ESCAPE]:
				running = False
				gameOver(score1,score2)
			
	
		if(snake1.move() == 1 ):
			move1+=1
		if(snake2.move() == 1):
			move2+=1
		
		window.fill(pygame.Color(10,0,10))
		
		#Border
		for x in range(0, 510, 10):
			pygame.draw.rect(window, (105,105,105),[x, 0,10,10])
			pygame.draw.rect(window, (105,105,105),[x, 510,10,10])
			pygame.draw.rect(window, (105,105,105),[0, x,10,10])
			pygame.draw.rect(window, (105,105,105),[510, x,10,10])


		for pos in snake1.getBody():
			pygame.draw.rect(window, pygame.Color(170,98,122),pygame.Rect(pos[0],pos[1],10,10))

		for pos in snake2.getBody():
			pygame.draw.rect(window,pygame.Color(98,144,170),pygame.Rect(pos[0],pos[1],10,10))
				
		if(snake1.checkCollision(snake2)==1):
			score1+= 1
			running = False
			gameOver(score1,score2)
		elif(snake2.checkCollision(snake1)==1):
			score2+= 1
			running = False
			gameOver(score1,score2)
				
		pygame.display.flip()
		py_clock.tick(10)

gameStart()
pygame.quit()


# In[ ]:





# In[ ]:




