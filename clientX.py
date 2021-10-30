import socket
import atexit
import pygame
from pygame.locals import *
from threading import Thread
pygame.init()
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("client")
white=(255,255,255)
black=(0,0,0)
import time

msg = ''
turn = True
createMessage = False
oppDraw = True

x1 = -1
y1 = -1

def tttSocket():
    global msg
    global turn
    global createMessage
    global oppDraw
    global x1
    global y1
    
    host = "localhost"
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    print("connected")

    
    while True:
        if turn and createMessage and oppDraw:
            print("sending")
            s.sendall(msg.encode())
            turn = False
            print("sent, now receiving")
            
            
        if turn == False:
            data = s.recv(1024)
            coordinates = (data.decode().split(","))
            x1 = int(coordinates[0])
            y1 = int(coordinates[1])
            oppDraw = False
            createMessage = False
            turn = True
            print("received, now sending")
            
sThread = Thread(target = tttSocket)
sThread.start()

ticTacToe={1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:''}

def game():
    global ticTacToe
    global msg
    global turn
    global createMessage
    global x1
    global y1
    global oppDraw
    
    screen.fill(black)

    ##checked=false means it is the "X's" turn, if checked=true, it is "O's" turn
    
    checked=False

    ## Checks if someone already won, and if someone hasn't won after 9 turns it is a tie

    winCheck=False
    x=-1
    y=-1
    while True:
        # draws the grid
        for i in range(6):
            for j in range(3):
                pygame.draw.rect(screen,white,(400*i,200*j,200,200),4)
                pygame.draw.rect(screen,white,(400*i+200,200*j,200,200),4)
        
        
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                exit()
            elif event.type==pygame.MOUSEBUTTONDOWN:
                #print("You pressed the left mouse button at",event.pos)
                x,y=event.pos
                

    ## Player "X" move           
        if createMessage == False and turn and oppDraw:
            if 0<=x<200 and 0<=y<200 and ticTacToe[1]=='':
                pygame.draw.line(screen,white,(0,0),(200,200),4)
                pygame.draw.line(screen,white,(200,0),(0,200),4)
                ticTacToe[1]='x'
                msg = (str(x) + "," + str(y))
                createMessage = True
            if 0<=x<200 and y<400 and y>200 and ticTacToe[4]=='':
                pygame.draw.line(screen,white,(0,200),(200,400),4)
                pygame.draw.line(screen,white,(200,200),(0,400),4)
                ticTacToe[4]='x'
                msg = (str(x) + "," + str(y))
                createMessage = True
            if 0<=x<200 and 400<y<=600 and ticTacToe[7]=='':
                pygame.draw.line(screen,white,(0,400),(200,600),4)
                pygame.draw.line(screen,white,(200,400),(0,600),4)
                ticTacToe[7]='x'
                msg = (str(x) + "," + str(y))
                createMessage = True
            if 200<x<400 and 0<=y<200 and ticTacToe[2]=='': 
                pygame.draw.line(screen,white,(200,0),(400,200),4)
                pygame.draw.line(screen,white,(400,0),(200,200),4)
                ticTacToe[2]='x'
                msg = (str(x) + "," + str(y))
                createMessage = True
            if 200<x<400 and y<400 and y>200 and ticTacToe[5]=='':
                pygame.draw.line(screen,white,(200,200),(400,400),4)
                pygame.draw.line(screen,white,(400,200),(200,400),4)
                ticTacToe[5]='x'
                msg = (str(x) + "," + str(y))
                createMessage = True
            if 200<x<400 and 400<y<=600 and ticTacToe[8]=='':
                pygame.draw.line(screen,white,(200,400),(400,600),4)
                pygame.draw.line(screen,white,(400,400),(200,600),4)
                ticTacToe[8]='x'
                msg = (str(x) + "," + str(y))
                createMessage = True
            if 400<x<600 and 0<=y<200 and ticTacToe[3]=='':
                pygame.draw.line(screen,white,(400,0),(600,200),4)
                pygame.draw.line(screen,white,(600,0),(400,200),4)
                ticTacToe[3]='x'
                msg = (str(x) + "," + str(y))
                createMessage = True
            if 400<x<=600 and y<400 and y>200 and ticTacToe[6]=='':
                pygame.draw.line(screen,white,(400,200),(600,400),4)
                pygame.draw.line(screen,white,(600,200),(400,400),4)
                ticTacToe[6]='x'
                msg = (str(x) + "," + str(y))
                createMessage = True
            if 400<x<=600 and 400<y<=600 and ticTacToe[9]=='':
                pygame.draw.line(screen,white,(400,400),(600,600),4)
                pygame.draw.line(screen,white,(600,400),(400,600),4)
                ticTacToe[9]='x'
                msg = (str(x) + "," + str(y))
                createMessage = True
        pygame.display.update()

        #Player O draw
        if turn and oppDraw == False and createMessage == False:
            if 0<=x1<200 and 0<=y1<200 and ticTacToe[1]=='':
                pygame.draw.circle(screen,white,(100,100),(100),4)
                pygame.display.update()
                ticTacToe[1]='o'
                oppDraw = True
            if 0<=x1<200 and y1<400 and y1>200 and ticTacToe[4]=='':
                pygame.draw.circle(screen,white,(100,300),(100),4)
                pygame.display.update()
                ticTacToe[4]='o'
                oppDraw = True
            if 0<=x1<200 and 400<y1<=600 and ticTacToe[7]=='':
                pygame.draw.circle(screen,white,(100,500),(100),4)
                pygame.display.update()
                ticTacToe[7]='o'
                oppDraw = True
            if 200<x1<400 and 0<=y1<200 and ticTacToe[2]=='': 
                pygame.draw.circle(screen,white,(300,100),(100),4)
                pygame.display.update()
                ticTacToe[2]='o'
                oppDraw = True
            if 200<x1<400 and y1<400 and y1>200 and ticTacToe[5]=='':
                pygame.draw.circle(screen,white,(300,300),(100),4)
                pygame.display.update()
                ticTacToe[5]='o'
                oppDraw = True
            if 200<x1<400 and 400<y1<=600 and ticTacToe[8]=='':
                pygame.draw.circle(screen,white,(300,500),(100),4)
                pygame.display.update()
                ticTacToe[8]='o'
                oppDraw = True
            if 400<x1<600 and 0<=y1<200 and ticTacToe[3]=='':
                pygame.draw.circle(screen,white,(500,100),(100),4)
                pygame.display.update()
                ticTacToe[3]='o'
                oppDraw = True
            if 400<x1<=600 and y1<400 and y1>200 and ticTacToe[6]=='':
                pygame.draw.circle(screen,white,(500,300),(100),4)
                pygame.display.update()
                ticTacToe[6]='o'
                oppDraw = True
            if 400<x1<=600 and 400<y1<=600 and ticTacToe[9]=='':
                pygame.draw.circle(screen,white,(500,500),(100),4)
                pygame.display.update()
                ticTacToe[9]='o'
                oppDraw = True

        
        ## Win Conditions

        ## If player "X" wins               
        if ticTacToe[1]=='x' and ticTacToe[2]=='x' and ticTacToe[3]=='x':
            print("Congratulations! You won!")
            winCheck=True
            break
        if ticTacToe[4]=='x' and ticTacToe[5]=='x' and ticTacToe[6]=='x':
            print("Congratulations! You won!")
            winCheck=True
            break
        if ticTacToe[7]=='x' and ticTacToe[8]=='x' and ticTacToe[9]=='x':
            print("Congratulations! You won!")
            winCheck=True
            break
        if ticTacToe[1]=='x' and ticTacToe[4]=='x' and ticTacToe[7]=='x':
            print("Congratulations! You won!")
            winCheck=True
            break
        if ticTacToe[2]=='x' and ticTacToe[5]=='x' and ticTacToe[8]=='x':
            print("Congratulations! You won!")
            winCheck=True
            break
        if ticTacToe[3]=='x' and ticTacToe[6]=='x' and ticTacToe[9]=='x':
            print("Congratulations! You won!")
            winCheck=True
            break
        if ticTacToe[1]=='x' and ticTacToe[5]=='x' and ticTacToe[9]=='x':
            print("Congratulations! You won!")
            winCheck=True
            break
        if ticTacToe[3]=='x' and ticTacToe[5]=='x' and ticTacToe[7]=='x':
            print("Congratulations! You won!")
            winCheck=True
            break
        
        ## If player "O" wins
        
        if ticTacToe[1]=='o' and ticTacToe[2]=='o' and ticTacToe[3]=='o':
            print("Sorry, you lost.")
            winCheck=True
            break
        if ticTacToe[4]=='o' and ticTacToe[5]=='o' and ticTacToe[6]=='o':
            print("Sorry, you lost.")
            winCheck=True
            break
        if ticTacToe[7]=='o' and ticTacToe[8]=='o' and ticTacToe[9]=='o':
            print("Sorry, you lost.")
            winCheck=True
            break
        if ticTacToe[1]=='o' and ticTacToe[4]=='o' and ticTacToe[7]=='o':
            print("Sorry, you lost.")
            winCheck=True
            break
        if ticTacToe[2]=='o' and ticTacToe[5]=='o' and ticTacToe[8]=='o':
            print("Sorry, you lost.")
            winCheck=True
            break
        if ticTacToe[3]=='o' and ticTacToe[6]=='o' and ticTacToe[9]=='o':
            print("Sorry, you lost.")
            winCheck=True
            break
        if ticTacToe[1]=='o' and ticTacToe[5]=='o' and ticTacToe[9]=='o':
            print("Sorry, you lost.")
            winCheck=True
            break
        if ticTacToe[3]=='o' and ticTacToe[5]=='o' and ticTacToe[7]=='o':
            print("Sorry, you lost.")
            winCheck=True
            break
        
        ## If it is a tie
        
        if ticTacToe[1]!='' and ticTacToe[2]!='' and ticTacToe[3]!='' and ticTacToe[4]!='' and ticTacToe[5]!='' and ticTacToe[6]!='' and ticTacToe[7]!='' and ticTacToe[8]!='' and ticTacToe[9]!='' and winCheck==False:
            print("It is a tie.")
            break
        pygame.display.update()

game()



