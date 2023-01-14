# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 19:41:55 2022

@author: Admin
"""

import pygame
from .constant import RED, WHITE , BLUE , SQUARE_SIZE
from checkers.board import Board
import pyttsx3 
#import speech_recognition as sr

#Text To Speech Section
engine = pyttsx3.init()
engine.runAndWait()
engine.setProperty('rate', 200)
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)


board_dict = {'Alpha zero': (0,0),'Alpha One': (0,1),'alpha 2': (0,2),'Alpha 3': (0,3),'Alpha 4': (0,4),'Alpha 5': (0,5),'Alpha 6': (0,6),'Alpha 7': (0,7),
              'Bravo zero': (1,0),'Bravo 1': (1,1),'Bravo 2': (1,2),'Bravo 3': (1,3),'Bravo 4': (1,4),'Bravo 5': (1,5),'Bravo six': (1,6),'Bravo 7': (1,7),
              'charli 0': (2,0),'Charlie 1': (2,1),'charli 2': (2,2),'Charlie 3': (2,3),'Charlie 4': (2,4),'charli 5': (2,5),'Charlie 6': (2,6),'Charlie 7': (2,7),
              'Delta zero': (3,0),'Delta 1': (3,1),'Delta 2': (3,2),'Delta 3': (3,3),'Delta 4': (3,4),'Delta 5': (3,5),'Delta 6': (3,6),'Delta 7': (3,7),
              'Eco zero': (4,0),'Eco 1': (4,1),'Eco 2': (4,2),'Eco 3': (4,3),'Eco 4': (4,4),'Eco 5': (4,5),'Eco 6': (4,6),'Eco 7': (4,7),
              'Falcon zero': (5,0),'Falcon 1': (5,1),'Falcon 2': (5,2),'Falcon 3': (5,3),'Falcon 4': (5,4),'Falcon 5': (5,5),'Falcon 6': (5,6),'Falcon 7': (5,7),
              'Golf zero': (6,0),'Golf 1': (6,1),'Golf 2': (6,2),'Golf 3': (6,3),'Golf 4': (6,4),'Golf 5': (6,5),'Golf 6': (6,6),'Golf 7': (6,7),
              'Hotel zero': (7,0),'Hotel 1': (7,1),'Hotel 2': (7,2),'Hotel 3': (7,3),'Hotel 4': (7,4),'Hotel 5': (7,5),'Hotel 6': (7,6),'Hotel 7': (7,7)}

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

class Game:
    def __init__(self,win):
        self._init()
        self.win = win
        self.active = False
        self.x =0
        self.y =0
        
        
    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()
        
    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.valid_moves ={}
        
    def make_active(self):
        self.active =True
        
    def winner(self):
        return self.board.winner()
        
    def reset(self):
        self._init()
        
    def select(self,row,col):
        if self.selected:
            result = self._move(row,col)
            print(result)
            if not result:
                self.selected = None
                print(self.selected)
                self.select(row, col)
        piece = self.board.get_piece(row,col)
        
        
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
        return False
        
    def _move(self,row,col):
        piece = self.board.get_piece(row,col)
        if self.selected and piece == 0 and (row,col) in self.valid_moves:
            self.board.move(self.selected,row,col)
            skipped = self.valid_moves[(row, col)]
            
            if skipped:
                self.board.remove(skipped)
                print(self.board.remove(skipped))
               
            self.change_turn()
        else:
            return False
        return True
    
    def draw_valid_moves(self,moves):
        for move in moves:
            row,col = move
            print(move)
            for i,j in board_dict.items():
                if j==move:
                    a=i       
            pygame.draw.circle(self.win,BLUE,(col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2),15)
            speak("Valid moves are: "+str(a))
            
            
            
    
    def change_turn(self):
        self.valid_moves ={}
        if self.turn ==  RED:
            self.turn = WHITE
            speak("White's Turn Now")
            
        else:
            self.turn = RED
            speak("RED'S TURN Now")
        
            
            
