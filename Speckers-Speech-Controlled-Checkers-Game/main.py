# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 16:28:51 2022

@author: Admin
"""

import pygame
import time
from checkers.constant import WIDTH, HEIGHT,SQUARE_SIZE,WHITE,RED,BLACK
from checkers.game import Game
from pygame import mixer
import pyttsx3 
import speech_recognition as sr

FPS = 60

pygame.init()
mixer.init()
  
# Loading the song
mixer.music.load("assets/bgm1.mp3")
  
# Setting the volume
mixer.music.set_volume(0.1)

board_dict = {'Alpha zero': (0,0),'Alpha One': (0,1),'alpha 2': (0,2),'Alpha 3': (0,3),'Alpha 4': (0,4),'Alpha 5': (0,5),'Alpha 6': (0,6),'Alpha 7': (0,7),
              'Bravo zero': (1,0),'Bravo 1': (1,1),'Bravo 2': (1,2),'Bravo 3': (1,3),'Bravo 4': (1,4),'Bravo 5': (1,5),'Bravo six': (1,6),'Bravo 7': (1,7),
              'charli 0': (2,0),'Charlie 1': (2,1),'charli 2': (2,2),'Charlie 3': (2,3),'Charlie 4': (2,4),'charli 5': (2,5),'Charlie 6': (2,6),'Charlie 7': (2,7),
              'Delta zero': (3,0),'Delta 1': (3,1),'Delta 2': (3,2),'Delta 3': (3,3),'Delta 4': (3,4),'Delta 5': (3,5),'Delta 6': (3,6),'Delta 7': (3,7),
              'Eco zero': (4,0),'Eco 1': (4,1),'Eco 2': (4,2),'Eco 3': (4,3),'Eco 4': (4,4),'Eco 5': (4,5),'Eco 6': (4,6),'Eco 7': (4,7),
              'Falcon zero': (5,0),'Falcon 1': (5,1),'Falcon 2': (5,2),'Falcon 3': (5,3),'Falcon 4': (5,4),'Falcon 5': (5,5),'Falcon 6': (5,6),'Falcon 7': (5,7),
              'Golf zero': (6,0),'Golf 1': (6,1),'Golf 2': (6,2),'Golf 3': (6,3),'Golf 4': (6,4),'Golf 5': (6,5),'Golf 6': (6,6),'Golf 7': (6,7),
              'Hurricane zero': (7,0),'Hurricane 1': (7,1),'Hurricane 2': (7,2),'Hurricane 3': (7,3),'Hurricane 4': (7,4),'Hurricane 5': (7,5),'Hurricane 6': (7,6),'Hurricane 7': (7,7)}


WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("SPECKERS")
font = pygame.font.Font('freesansbold.ttf', 62)
font1 = pygame.font.Font('freesansbold.ttf', 18)
font2 = pygame.font.Font('freesansbold.ttf', 24)
text = font.render('  SPECKERS ', True, WHITE)
text1 = font1.render('                 GAME OF LUCK AND SKILLS', True,RED )
text2 = font2.render("Say START to PLAY and QUIT to END GAME", True,RED )

#Text To Speech Section
engine = pyttsx3.init()
engine.runAndWait()
engine.setProperty('rate', 185)
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
#Speech To Text Input Section
def takeCommand():
    mixer.music.set_volume(0.05)
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source,timeout=20)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio)
        print("You said: ", query)
        #querys = str(query)
        print(query)
        return query
        
    except Exception as e:
        print(e)
        speak("Pardon me, can you please say that again...")
        return takeCommand()

def get_row_col_from_mouse(pos):
    x,y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row , col

def start_page():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        
        mixer.music.play()
        s = pygame.draw.rect(WINDOW, WHITE, pygame.Rect(75, 150, 420, 60),2)
        WINDOW.blit(text, s)
        pygame.draw.rect(WINDOW, WHITE, pygame.Rect(75, 150, 420, 70),2)
        pygame.draw.rect(WINDOW, WHITE, pygame.Rect(75, 138, 420, 12),2)
        s1 = pygame.draw.rect(WINDOW, BLACK, pygame.Rect(75, 230, 420, 30),2)
        WINDOW.blit(text1, s1)
        WINDOW.blit(text2,(40,350))
        pygame.display.flip()
        speak("Welcome to Speckers - The GAME OF LUCK AND SKILLS ")
        speak("Please say your command")
        s1=str(takeCommand())
        if s1=='Start' or s1=='start':
            speak(s1)
            mixer.music.set_volume(0.5)
            time.sleep(5)
            run = False
            game_started()
            
            
        elif s1=='exit' or s1 == 'Exit':
            speak("Exiting from Speckers Game")
            pygame.quit()
            exit()
        else:
            speak("Invalid Command !! Please Say Either Play or Exit")
            
            
def game_started():
    run = True
    mixer.music.set_volume(0.2)
    mixer.music.play()
    clock = pygame.time.Clock()
    game= Game(WINDOW)
    
    speak("Welcome to Speckers A.K.A. Speech controlled Checkers")
    speak("The Game is battle between two Groups Team White vs Team Red")
    speak("Team White consists of - Alpha")
    speak("Bravo and Charlie Battalions ")
    speak("Team Red consists of - Falcon")
    speak("Golf and Hurricane Battalions ")
    speak("Since Ages,Both the Teams are in quest to annexe")
    speak("ATLANTIS- The Midas City")
    speak("In order to annexe Atlantis")
    speak("both the Teams Red and White are in context to get Delta and Echo battalions on their side")
    speak("to get an upper hand over each other")
    speak("Let see which team gets extra battalions for the Battle of Atlantis")
    print("------------------------------------------")
    print("Alpha      |0 | 1 | 2 | 3 | 4 | 5 | 6 | 7|")
    print("  ----------------------------------------")
    print("Bravo      |0 | 1 | 2 | 3 | 4 | 5 | 6 | 7|")
    print("  ----------------------------------------")
    print("Charlie    |0 | 1 | 2 | 3 | 4 | 5 | 6 | 7|")
    print("  ----------------------------------------")
    print("Delta      |0 | 1 | 2 | 3 | 4 | 5 | 6 | 7|")
    print("  ----------------------------------------")
    print("Echo       |0 | 1 | 2 | 3 | 4 | 5 | 6 | 7|")
    print("  ----------------------------------------")
    print("Falcon     |0 | 1 | 2 | 3 | 4 | 5 | 6 | 7|")
    print("  ----------------------------------------")
    print("Golf       |0 | 1 | 2 | 3 | 4 | 5 | 6 | 7|")
    print("  ----------------------------------------")
    print("Hurricane  |0 | 1 | 2 | 3 | 4 | 5 | 6 | 7|")
    print("------------------------------------------")
    print("           |0 | 1 | 2 | 3 | 4 | 5 | 6 | 7|")
    print("------------------------------------------")
    
    speak("Please refer the matrix printed below for your moves")
    speak("Note: Command should start with ")
    speak("Team Name from (Alpha , Bravo , Charlie, Delta)")
    speak(" Echo, Falcon,Golf and Hurricane")
    speak("and one number (0-7) For eg. Alpha 0 or Hurricane 7")
    speak("So Let the battle beginnnnn...")
    while run:
        clock.tick(FPS)
        
        if game.winner() != None:
            speak(game.winner())
            run = False
            
        def initial():
            speak("Speak up the block position you want to move")
            s1=str(takeCommand())
            speak(s1+"is selected")
            return s1
          
        def finale():
            pieceFound1 =initial()
            if pieceFound1 == 'Alpha zero':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'Alpha One':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'alpha 2':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'Alpha 3':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'Alpha 4':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'Alpha 5':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'Alpha 6':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'Alpha 7':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'Bravo zero':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'Bravo 1':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'Bravo 2':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'Bravo 3':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'Bravo 4':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'Bravo 5':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'Bravo 6':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'Bravo 7':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'charli 0':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'Charlie 1':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'charli 2':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'Charlie 3':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'Charlie 4':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'charli 5':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'Charlie 6':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'Charlie 7':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'Delta zero':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'Delta 1':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'Delta 2':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'Delta 3':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'Delta 4':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'Delta 5':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'Delta 6':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'Delta 7':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'Eco zero':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'Eco 1':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'Eco 2':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'Eco 3':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'Eco 4':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'Eco 5':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'Eco 6':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'Eco 7':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'Falcon zero':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            
            elif pieceFound1 == 'Falcon 1':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'Falcon 2':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'Falcon 3':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'Falcon 4':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'Falcon 5':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'Falcon 6':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'Falcon 7':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'Golf zero':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'Golf 1':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'Golf 2':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'Golf 3':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'Golf 4':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'Golf 5':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'Golf 6':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'Golf 7':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'Hurricane zero':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'Hurricane 1':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'Hurricane 2':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'Hurricane 3':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'Hurricane 4':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'Hurricane 5':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'Hurricane 6':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                return ini_pos
            elif pieceFound1 == 'Hurricane 7':
                ini_pos = board_dict[pieceFound1]
                print(board_dict[pieceFound1])
                speak(pieceFound1+"is a Valid Position")
                #speak("Valid Position as"+pieceFound1+" corresponds to "+str(board_dict[pieceFound1]))
                return ini_pos
            elif pieceFound1 == 'exit':
                pygame.quit()
                exit()
            else:
                speak("Invalid Move")
                return finale()   
            
        def move_position():
            se = finale()
            print(type(se))
            print(se)
            if type(se) is tuple:
                row , col = se[0],se[1]
                speak(str(row)+" and "+str(col)+'is selected')
                game.select(row, col)
                
            
        move_position()
        game.update()
    
    
   
start_page()