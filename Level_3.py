import pygame as pg
from pygame.math import Vector2
import sys
from InputBox import *
from PyQt5 import QtCore, QtGui, QtWidgets
from Level_4 import Room4
	

cell_size = 10
cell_number = 30
c = 0 
b = 0

class BUTTON(object):
    def __init__(self, text=''):
        self.color = (0,0,0)
        self.x = 1500
        self.y = 800
        self.width = 250
        self.height = 50
        self.text = text

    def draw(self,screen,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pg.draw.rect(screen, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pg.draw.rect(screen, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pg.font.Font('Poppins-Regular.ttf',40)
            text = font.render(self.text, 1, (255,255,255))
            screen.blit(text,(self.x,self.y))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False




class Player(object):


	def __init__(self,screen,x_pos,y_pos):
		self.screen = screen
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.Player_pos = Vector2(self.x_pos,self.y_pos)

	def draw_Player(self):
		
		Player_rect = pg.Rect(self.Player_pos.x,self.Player_pos.y,cell_size,cell_size)
		pg.draw.rect(self.screen,(255,0,0),Player_rect)
		
	


class Puzzle(object):

	def __init__(self,screen):
		
		self.screen = screen

	def draw_puzzle(self):
		self.x = 1550
		self.y = 140
		self.pos = Vector2(self.x,self.y)
		puzzle_rect = pg.Rect(self.pos.x,self.pos.y,cell_size,cell_size)
		pg.draw.rect(self.screen,(0,0,0),puzzle_rect)
		

	def picture(self):
		riddle = pg.image.load("Jumbled_word.jpg")
		(self.screen).blit(riddle,(100,200))

	def inputbox(self,event):
		Input = InputBox(300, 650, 140, 40)
		self.input = Input
		
		self.input.update()
		self.input.draw(self.screen)



class Main(object):

	def __init__(self,screen,x_pos,y_pos,event,c):
		self.Player = Player(screen,x_pos,y_pos)
		self.Puzzle = Puzzle(screen)
		self.event = event
		

	def Update(self):
		self.check_collision()
		

	def draw_elements(self):
		self.Puzzle.draw_puzzle()
		self.Player.draw_Player()
		
	def check_collision(self):
		global c
		#print(self.Puzzle.pos,self.Player.Player_pos)
		if self.Puzzle.pos == self.Player.Player_pos:
			c = 1
			#print(self.Puzzle.pos,self.Player.Player_pos)
			(self.Puzzle).picture()
			#(self.Puzzle).inputbox(self.event)
			


class Room3(object):

	
	def Room_3(self,mainWindow):
		global b
		pg.init()


		def Level4():
			self.window = QtWidgets.QMainWindow()
			self.ui = Room4()
			self.ui.Room_4(self.window)
			self.window.showMaximized()

		screen = pg.display.set_mode((1920,1000))
		clock = pg.time.Clock()
		bg = pg.image.load("Room3_bg.jpg")
		DISPLAYSURF = pg.display.set_mode((1920,1000),pg.RESIZABLE)

		room_map = pg.Surface((290,290))
		room_map.fill((128,128,128))
		room_border = pg.Rect(1495,95,300,300)
		
		event = pg.event.get()

		x_pos = 1680
		y_pos = 370
		#main_game = Main(screen,x_pos,y_pos,event)


		inputbox = InputBox(350, 675, 140, 40)

		Button = BUTTON("Next Room>")


		SCREEN_UPDATE = pg.USEREVENT

		while True:



			pg.display.set_caption("Sherlock's Escape")
			screen.blit(bg,(0, 0))																# Setting the background image
			
			pg.draw.rect(screen,(255,255,255),room_border)
			screen.blit(room_map,(1500,100))


			font = pg.font.Font('Poppins-Regular.ttf', 72)										# Using Font
			text = font.render('Room 3', True, (255,255,255))
			textRect = text.get_rect()
			textRect.center = (200,100)
			screen.blit(text,textRect)



			for event in pg.event.get():
				if event.type == pg.QUIT:
					pg.quit()
					sys.exit()

				if event.type == SCREEN_UPDATE:
					main_game.Update()
				

				if event.type == pg.KEYDOWN:													# Code for Movement
						if event.key == pg.K_LEFT :
							if x_pos <= 1500:
								print("Cannot move further in this direction") 
							else:
								x_pos -= 10
								print("left")
						if event.key == pg.K_RIGHT:
							if x_pos >= 1780:
								print("Cannot move further in this direction") 
							else:
								x_pos += 10
								print("right")
						if event.key == pg.K_UP:
							if y_pos <= 100:
								print("Cannot move further in this direction") 
							else:
								y_pos -= 10
								print("forward")
						if event.key == pg.K_DOWN:
							if y_pos >= 380:
								print("Cannot move further in this direction") 
							else:
								y_pos += 10
								print("backward")
				main_game = Main(screen,x_pos,y_pos,event,c)

				input_answer = inputbox.handle_event(event)

				pos = pg.mouse.get_pos()

				if input_answer == "mycroft":
					b = 1

					
				
			main_game = Main(screen,x_pos,y_pos,event,c)	
			main_game.draw_elements()
			main_game.Update()


			if c == 1:
				inputbox.update()
				inputbox.draw(screen)
				
			if b == 1:
				Button.draw(screen,(0,0,0))
				if event.type == pg.MOUSEBUTTONDOWN:
					if Button.isOver(pos):
						Level4()
						
						
						


			pg.display.update()
			clock.tick(60)
