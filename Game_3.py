import numpy as np
import math
import pygame
import tkinter as tk
from tkinter import messagebox


ROW_COUNTS=6
COLUMN_COUNTS=7

def create_board():
    board=np.zeros((ROW_COUNTS,COLUMN_COUNTS)) # matrix 6X7 of zeros
    return board

def drop_piece(board,row,col, piece):
    board[row][col] = piece
    

def is_valid_location(board,col):
    return board[ROW_COUNTS-1][col] == 0 #check if the top row  is empty

def get_next_open_row(board,col):
    for r in range(ROW_COUNTS):
        if board[r][col] == 0:
            return r # retur the  first emppty row in that col
def message_box(subject,content):
        root=tk.Tk()
        root.attributes("-topmost",True)# be in top of any thing in pc screen
        root.withdraw() #be invis
        messagebox.showinfo(subject,content)
        try:
            root.destroy()
        except:
            pass        
def winning_move(board,piece):
    #check horizontal locations for win
    for c in range (COLUMN_COUNTS-3):
        for r in range (ROW_COUNTS):
            if board[r][c]==piece and board[r][c+1]==piece and board[r][c+2]==piece and board[r][c+3]==piece :
                return True
        
    #check vertical locations for win
    for c in range (COLUMN_COUNTS):
        for r in range (ROW_COUNTS-3):
            if board[r][c]==piece and board[r+1][c]==piece and board[r+2][c]==piece and board[r+3][c]==piece :
              return True
    #check positively sloped diaganols
    for c in range (COLUMN_COUNTS-3):
        for r in range (ROW_COUNTS-3):
            if board[r][c]==piece and board[r+1][c+1]==piece and board[r+2][c+2]==piece and board[r+3][c+3]==piece :
              return True       
    #check negatively sloped diaganols
    for c in range (COLUMN_COUNTS):
        for r in range (3,ROW_COUNTS):
            if board[r][c]==piece and board[r-1][c+1]==piece and board[r-2][c+2]==piece and board[r-3][c+3]==piece :
              return True


def Draw_board(board):
    #draw backview
    for c in range (COLUMN_COUNTS):
        for r in range (ROW_COUNTS):
            pygame.draw.rect(screen,(0,0,255),(c*SQUARESIZE ,r*SQUARESIZE+SQUARESIZE,SQUARESIZE,SQUARESIZE))
            pygame.draw.circle(screen,(0,0,0),(int(c*SQUARESIZE+(SQUARESIZE/2)) ,int(r*SQUARESIZE+SQUARESIZE+(SQUARESIZE/2))),RADIUS)
#draw balls 
    for c in range (COLUMN_COUNTS):
        for r in range (ROW_COUNTS):
            if (board[r][c] == 1):
                pygame.draw.circle(screen,(255,0,0),(int(c*SQUARESIZE+(SQUARESIZE/2)), height- int(r*SQUARESIZE+(SQUARESIZE/2))),RADIUS)
            elif (board[r][c] == 2):
                pygame.draw.circle(screen,(0,255,0),(int(c*SQUARESIZE+(SQUARESIZE/2)) , height- int(r*SQUARESIZE+(SQUARESIZE/2))),RADIUS)
            else :
                 pass
    

board=create_board()
game_over=False
turn=0

pygame.init()

SQUARESIZE=100 #PIXEL
width = (ROW_COUNTS+1) * SQUARESIZE
height = COLUMN_COUNTS* SQUARESIZE
RADIUS=int(SQUARESIZE/2 -5)
size=(width , height)

screen=pygame.display.set_mode(size)

myfont=pygame.font.SysFont("monospace",75)

while not game_over:
    pygame.display.update()
    Draw_board(board)  
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEMOTION :#draw next circle
            pygame.draw.rect(screen,(0,0,0),(0,0,width,SQUARESIZE))
            posx=event.pos[0]
            if turn==0 :
                pygame.draw.circle(screen,(255,0,0),(posx,int(SQUARESIZE/2)),RADIUS)
            else:
                pygame.draw.circle(screen,(0,255,0),(posx,int(SQUARESIZE/2)),RADIUS)                    
        if event.type == pygame.MOUSEBUTTONDOWN :
            if turn==0 :
                posx=event.pos[0]# mouse clik position
                col = math.floor(posx/SQUARESIZE)
                if is_valid_location(board,col):
                    row =get_next_open_row(board,col)
                    drop_piece(board,row,col, 1)
                    if winning_move(board,1):
                        #pygame.draw.rect(screen,(0,0,0),(0,0,width,SQUARESIZE))
                        label=myfont.render("player 1 wins",1,(255,0,0))
                        screen.blit(label,(40,10))
                        message_box("player 1 wins ","Play again ")
                        game_over=True
                #P2
            else :
                posx=event.pos[0]# mouse clik position
                col = math.floor(posx/SQUARESIZE)
                if is_valid_location(board,col):
                    row =get_next_open_row(board,col)
                    drop_piece(board,row,col, 2)
                    if winning_move(board,2):
                        #pygame.draw.rect(screen,(0,0,0),(0,0,width,SQUARESIZE))
                        label=myfont.render("player 2 wins",1,(0,255,0))
                        screen.blit(label,(40,10))
                        message_box("player 2 wins ","Play again ")
                        game_over=True
         
            turn +=1
            turn %=2
#end

            
    
     
