import pygame
import sys
import random

pygame.init()

fp = open('wordlist.txt', 'r')
lines=fp.readlines()
wordnumber=random.randint(1,500)
word=lines[wordnumber]
word=word.upper()
word=word[4:12]
#GameVariables
screenheight=600
screenwidth=800
background=pygame.image.load('images/background.png')
letterbox=pygame.image.load('images/letterbox.png')
letterboxcross=pygame.image.load('images/letterboxcross.png')
hanglevel=[
    'images/level1.png',
    'images/level2.png',
    'images/level3.png',
    'images/level4.png',
    'images/level5.png',
    'images/level6.png',
    'images/level7.png',
    'images/level8.png']

gamescreen=pygame.display.set_mode((screenwidth,screenheight))
pygame.display.set_caption('Hangman by Manas')
FPS=60
clock=pygame.time.Clock()
lettersused=[]
mistake=0
correct=0
hanglevelimage=pygame.image.load(hanglevel[mistake])


hangman=True

def screendisplay(lettersused):
    gamescreen.blit(background,(0,0))
    i=30
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    #Loop for Input Letters
    Counter='A'
    while i<740:
        if Counter in lettersused:
            gamescreen.blit(letterboxcross,(i,470))
        else:
            gamescreen.blit(letterbox,(i,470))
        textsurface = myfont.render(str(Counter), False, (0, 0, 0))
        gamescreen.blit(textsurface,((i+10),475))
        Counter = chr(ord(Counter) + 1)
        if Counter in lettersused:
            gamescreen.blit(letterboxcross,(i,530))
        else:
            gamescreen.blit(letterbox,(i,530))
        textsurface = myfont.render(str(Counter), False, (0, 0, 0))
        gamescreen.blit(textsurface,((i+10),530))
        Counter = chr(ord(Counter) + 1)
        i+=55
    #Loop for Main Word
    i=250
    for letter in word:
        gamescreen.blit(letterbox,(i,340))
        if letter in lettersused:
            textsurface=myfont.render(str(letter),False,(0,0,0))
            gamescreen.blit(textsurface,((i+10),340))
        i+=55

    hanglevelimage = pygame.image.load(hanglevel[mistake])
    gamescreen.blit(hanglevelimage,(50,30))
    pygame.display.update()

#Funtion to check if letter is there or not
def checkletter(key,word):
    global mistake
    global correct
    if key in word:
        correct+=1
    else:
        mistake+=1

def gameoverscreen():
    global correct
    global mistake
    gamescreen.blit(background,(0,0))
    text=pygame.font.SysFont('Comic Sans MS', 30)
    if mistake==6:
        hanglevelimage = pygame.image.load(hanglevel[6])
        textsurface=text.render('GAME OVER',False,(0,0,0))
    elif correct==8:
        hanglevelimage = pygame.image.load(hanglevel[7])
        textsurface = text.render('YOU WIN', False, (0, 0, 0))

    gamescreen.blit(hanglevelimage, (50, 30))
    gamescreen.blit(textsurface,(400,300))
    textsurface= text.render(str(word),False,(0,0,0))
    gamescreen.blit(textsurface,(400,350))
    pygame.display.update()

while hangman:
    pygame.time.delay(100)
    clock.tick(FPS)
    keys=pygame.key.get_pressed()

#Checkforletters Start
    for event in pygame.event.get():
        if event.type==pygame.QUIT or keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

    if keys[pygame.K_a] and not('A' in lettersused):
        key="A"
        lettersused.append(key)
        print(lettersused)
        checkletter(key,word)
    elif keys[pygame.K_b] and not('B' in lettersused):
        key="B"
        lettersused.append(key)
        print(lettersused)
        checkletter(key,word)
    elif keys[pygame.K_c] and not('C' in lettersused):
        key="C"
        lettersused.append(key)
        print(lettersused)
        checkletter(key,word)
    elif keys[pygame.K_d] and not('D' in lettersused):
        key="D"
        lettersused.append(key)
        print(lettersused)
        checkletter(key,word)
    elif keys[pygame.K_e] and not('E' in lettersused):
        key="E"
        lettersused.append(key)
        print(lettersused)
        checkletter(key,word)
    elif keys[pygame.K_f] and not('F' in lettersused):
        key="F"
        lettersused.append(key)
        print(lettersused)
        checkletter(key,word)
    elif keys[pygame.K_g] and not('G' in lettersused):
        key="G"
        lettersused.append(key)
        print(lettersused)
        checkletter(key,word)
    elif keys[pygame.K_h] and not('H' in lettersused):
        key="H"
        lettersused.append(key)
        print(lettersused)
        checkletter(key,word)
    elif keys[pygame.K_i] and not('I' in lettersused):
        key="I"
        lettersused.append(key)
        print(lettersused)
        checkletter(key,word)
    elif keys[pygame.K_j] and not('J' in lettersused):
        key="J"
        lettersused.append(key)
        print(lettersused)
        checkletter(key,word)
    elif keys[pygame.K_k] and not('K' in lettersused):
        key="K"
        lettersused.append(key)
        print(lettersused)
        checkletter(key,word)
    elif keys[pygame.K_l] and not('L' in lettersused):
        key="L"
        lettersused.append(key)
        print(lettersused)
        checkletter(key,word)
    elif keys[pygame.K_m] and not('M' in lettersused):
        key="M"
        lettersused.append(key)
        print(lettersused)
        checkletter(key,word)
    elif keys[pygame.K_n] and not('N' in lettersused):
        key="N"
        lettersused.append(key)
        print(lettersused)
        checkletter(key,word)
    elif keys[pygame.K_o] and not('O' in lettersused):
        key="O"
        lettersused.append(key)
        print(lettersused)
        checkletter(key,word)
    elif keys[pygame.K_p] and not('P' in lettersused):
        key="P"
        lettersused.append(key)
        print(lettersused)
        checkletter(key,word)
    elif keys[pygame.K_q] and not('Q' in lettersused):
        key="Q"
        lettersused.append(key)
        print(lettersused)
        checkletter(key,word)
    elif keys[pygame.K_r] and not('R' in lettersused):
        key="R"
        lettersused.append(key)
        print(lettersused)
        checkletter(key,word)
    elif keys[pygame.K_s] and not('S' in lettersused):
        key="S"
        lettersused.append(key)
        print(lettersused)
        checkletter(key,word)
    elif keys[pygame.K_t] and not('T' in lettersused):
        key="T"
        lettersused.append(key)
        print(lettersused)
        checkletter(key,word)
    elif keys[pygame.K_u] and not('U' in lettersused):
        key="U"
        lettersused.append(key)
        print(lettersused)
        checkletter(key,word)
    elif keys[pygame.K_v] and not('V' in lettersused):
        key="V"
        lettersused.append(key)
        print(lettersused)
        checkletter(key,word)
    elif keys[pygame.K_w] and not('W' in lettersused):
        key="W"
        lettersused.append(key)
        print(lettersused)
        checkletter(key,word)
    elif keys[pygame.K_x] and not('X' in lettersused):
        key="X"
        lettersused.append(key)
        print(lettersused)
        checkletter(key,word)
    elif keys[pygame.K_y] and not('Y' in lettersused):
        key="Y"
        lettersused.append(key)
        print(lettersused)
        checkletter(key,word)
    elif keys[pygame.K_z] and not('Z' in lettersused):
        key="Z"
        lettersused.append(key)
        print(lettersused)
        checkletter(key,word)
#Checkforletters End
    screendisplay(lettersused)
    if mistake==6 or correct==8:
        hangman=False

gameover=True
while gameover:

    keys=pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            gameover=False
    gameoverscreen()
pygame.quit()
sys.exit()


