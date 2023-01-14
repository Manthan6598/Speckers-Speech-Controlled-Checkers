# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 16:52:54 2022

@author: Admin
"""

import pygame
from .constant import RED,BLACK,ROWS,SQUARE_SIZE,COLS,WHITE,SKIN
from .piece import Piece

class Board:
    
    def __init__(self):
        self.board =[]
        self.red_left = self.white_left = 12
        self.red_king = self.white_king = 0
        self.create_board()
        
    def draw_squares(self,win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, COLS , 2):
                
                pygame.draw.rect(win, SKIN, (row*SQUARE_SIZE,col*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE))
              
    def move(self,piece,row,col):
        self.board[piece.row][piece.col],self.board[row][col] =self.board[row][col],self.board[piece.row][piece.col]
        piece.move(row,col)
        
        if row == ROWS - 1 or row == 0:
            piece.make_king()
            if piece.color == WHITE:
                self.white_king += 1
            else:
                self.red_king += 1
      
    def get_piece(self,row,col):
        return self.board[row][col]
        
    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row,col,WHITE))
                    elif row > 4:
                        self.board[row].append(Piece(row,col,RED))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)
                    
        q = str(RED)
        s = str(WHITE)
        piece_position = []
        checker_piece_pos={}
        for r in range(len(self.board)):
            for c in range(len(self.board)):
                p = str(self.board[r][c])
                if p==q or p==s:
                    piece_position.append((r,c))
        #print("==========Board Position=========")
        board_dict = {'Alpha zero': (0,0),'Alpha One': (0,1),'alpha 2': (0,2),'Alpha 3': (0,3),'Alpha 4': (0,4),'Alpha 5': (0,5),'Alpha 6': (0,6),'Alpha 7': (0,7),
                      'Bravo zero': (1,0),'Bravo 1': (1,1),'Bravo 2': (1,2),'Bravo 3': (1,3),'Bravo 4': (1,4),'Bravo 5': (1,5),'Bravo six': (1,6),'Bravo 7': (1,7),
                      'charli 0': (2,0),'Charlie 1': (2,1),'charli 2': (2,2),'Charlie 3': (2,3),'Charlie 4': (2,4),'charli 5': (2,5),'Charlie 6': (2,6),'Charlie 7': (2,7),
                      'Delta zero': (3,0),'Delta 1': (3,1),'Delta 2': (3,2),'Delta 3': (3,3),'Delta 4': (3,4),'Delta 5': (3,5),'Delta 6': (3,6),'Delta 7': (3,7),
                      'Eco zero': (4,0),'Eco 1': (4,1),'Eco 2': (4,2),'Eco 3': (4,3),'Eco 4': (4,4),'Eco 5': (4,5),'Eco 6': (4,6),'Eco 7': (4,7),
                      'Falcon zero': (5,0),'Falcon 1': (5,1),'Falcon 2': (5,2),'Falcon 3': (5,3),'Falcon 4': (5,4),'Falcon 5': (5,5),'Falcon 6': (5,6),'Falcon 7': (5,7),
                      'Golf zero': (6,0),'Golf 1': (6,1),'Golf 2': (6,2),'Golf 3': (6,3),'Golf 4': (6,4),'Golf 5': (6,5),'Golf 6': (6,6),'Golf 7': (6,7),
                      'Hotel zero': (7,0),'Hotel 1': (7,1),'Hotel 2': (7,2),'Hotel 3': (7,3),'Hotel 4': (7,4),'Hotel 5': (7,5),'Hotel 6': (7,6),'Hotel 7': (7,7)}
        print("==========Board Position=========")            
        print(board_dict)
        for key,value in board_dict.items():
            for j in piece_position:
                if value == j:
                    checker_piece_pos[key] = value
        print("=========Piece Position==========")              
        print(checker_piece_pos)
                    
    def draw(self,win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0 :
                    piece.draw(win)
                    
    
    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == RED:
                    self.red_left -= 1
                else:
                    self.white_left -= 1            
    
    def winner(self):
        if self.red_left <= 0:
            winner_player = "CONGRATULATIONS TEAM WHITE WON !!!"
            return winner_player
        elif self.white_left <= 0:
            winner_player = "CONGRATULATIONS TEAM RED WON !!!"
            return winner_player
        
        return None 
    
    def get_valid_moves(self,piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row 
        
        if piece.color == RED or piece.king:
            moves.update(self._traverse_left(row -1, max(row -3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row -1, max(row -3, -1), -1, piece.color, right))
        if piece.color == WHITE or piece.king:
            moves.update(self._traverse_left(row +1, min(row +3, ROWS), 1, piece.color, left))
            moves.update(self._traverse_right(row +1, min(row +3, ROWS), 1, piece.color, right))
        return moves
    
    def _traverse_left(self,start,stop,step,color,left,skipped=[]):
        last =[]
        moves ={}
        for r in range(start,stop,step):
            if left < 0:
                break
            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r,left)] = last + skipped
                else:
                    moves[(r,left)] = last
                if last:
                    if step == -1:
                        row = max(r-3,0)
                    else:
                        row = min(r+3,ROWS)
                        
                    moves.update(self._traverse_left(r+step, row, step, color, left-1,skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, color, left+1,skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]
            left -= 1
        return moves
    
    def _traverse_right(self,start,stop,step,color,right,skipped=[]):
        last =[]
        moves ={}
        for r in range(start,stop,step):
            if right >= COLS:
                break
            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r,right)] = last + skipped
                else:
                    moves[(r,right)] = last
                if last:
                    if step == -1:
                        row = max(r-3,0)
                    else:
                        row = min(r+3,ROWS)
                        
                    moves.update(self._traverse_left(r+step, row, step, color, right-1,skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, color, right+1,skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]
            right += 1
        return moves
        
    
            
        
                
                
        