import pygame
import random
import sys
import time
import threading
pygame.init()
screen_width = 1000
screen_hight = 1000
screen = pygame.display.set_mode((screen_width, screen_hight))
pygame.display.set_caption("3iem_conte's snake")
clock = pygame.time.Clock()

FPS = 60

if 1==1:
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Fullscreen Game")
    screen_width = screen.get_width()
    screen_hight = screen.get_height()

border = 50
appleamount = 1
snakelengh = 3
grid_size = 20
gamemode = "survival"
difficulty = "hard"

alive = True
coordinates = []
co_y = 1
gridcolor = (0,255,255)
width_width = 1
x = 0
y = 0
ia = 0
cordoutput = []
i = 1
color1 = (50,200,50)
color2 = (50,180,50)
color0 = (70,200,70)
black = (0,0,0)
screen.fill(color0)
co = []
coordinates = []
i = 1
co_y = 1
segcords = ""
def getcord(item):
    cordoutput=[]
    gc = item.split(",")
    cordoutput.append((int(int(gc[0])-1)*int(sizex)))
    cordoutput.append((int(int(gc[1])-1)*int(sizey)))
    return cordoutput

def drawsquare(x,y):
        rectangle = pygame.Rect(x*sizex+border,y*sizey+border,sizex,sizey)
        if int(y)%2 == 1:
            if int(x)%2 == 1 :
                color = color1
            else:
                color = color2
        else:
            if int(x)%2 == 1 :
                color = color2
            else:
                color = color1
        pygame.draw.rect(screen,(color), rectangle)

def drawgrid():
    for x in range(grid_size):
        for y in range (grid_size):
            rectangle = pygame.Rect(x*sizex+border,y*sizey+border,sizex,sizey)
            if int(y)%2 == 1:
                if int(x)%2 == 1 :
                    color = color1
                else:
                    color = color2
            else:
                if int(x)%2 == 1 :
                    color = color2
                else:
                    color = color1
            pygame.draw.rect(screen,(color), rectangle)   

def drawpic(picture,cords):
    str(picture)
    picture = pygame.image.load(picture)
    if picture == "apple.png":
        pic = pygame.transform.scale(picture,(sizex-width_width*2,sizey-width_width*2))
        screen.blit(pic,(getcord(cords)[0]+border+width_width,getcord(cords)[1]+border+width_width))
    else :
        pic = pygame.transform.scale(picture,(sizex,sizey))
        screen.blit(pic,(getcord(cords)[0]+border,getcord(cords)[1]+border))

def drawsnake(methode):
    drawpic("snake.middle.medium.png",snake[-1])
    if methode == "whole":
        for a in range(len(snake)):
            drawpic("snake.middle.medium.png",snake[a])
            segment=[]
            if a < len(snake)-1:
                seg1 = getcord(snake[a])
                seg2 = getcord(snake[a+1])
                segment = [int((seg1[0]-seg2[0])/int(sizex)),int((seg1[1]-seg2[1])/int(sizey))]
            match segment:
                case[0,-1]:
                    drawpic("snake.down.png",snake[a])
                    drawpic("snake.up.png",snake[a+1])
                case[0,1]:
                    drawpic("snake.up.png",snake[a])
                    drawpic("snake.down.png",snake[a+1])
                case[-1,0]:
                    drawpic("snake.right.png",snake[a])
                    drawpic("snake.left.png",snake[a+1])
                case[1,0]:
                    drawpic("snake.left.png",snake[a])
                    drawpic("snake.right.png",snake[a+1])
    else:
        drawpic("snake.middle.medium.png",snake[methode])
        seg1 = getcord(snake[methode])
        seg2 = getcord(snake[methode+1])
        segment = [int((seg1[0]-seg2[0])/int(sizex)),int((seg1[1]-seg2[1])/int(sizey))]
        match segment:
            case[0,-1]:
                drawpic("snake.down.png",snake[methode])
                drawpic("snake.up.png",snake[methode+1])
            case[0,1]:
                drawpic("snake.up.png",snake[methode])
                drawpic("snake.down.png",snake[methode+1])
            case[-1,0]:
                drawpic("snake.right.png",snake[methode])
                drawpic("snake.left.png",snake[methode+1])
            case[1,0]:
                drawpic("snake.left.png",snake[methode])
                drawpic("snake.right.png",snake[methode+1])

def delseg():
    segcords = snake[0]
    spsnake = getcord(snake[0])
    drawsquare(spsnake[0]/sizex,spsnake[1]/sizey)
    spsnake = getcord(snake[1])
    drawsquare(spsnake[0]/sizex,spsnake[1]/sizey)
    snake.pop(0)
    drawsnake(0)

def drawborder():
    rectangle = pygame.Rect(border-sizex,border-sizey,(grid_size+2)*sizex,sizey)
    pygame.draw.rect(screen,(color0), rectangle)

    rectangle = pygame.Rect(border-sizex,border-sizey,sizex,(grid_size+2)*sizey)
    pygame.draw.rect(screen,(color0), rectangle)
    
    rectangle = pygame.Rect((border-sizex)+((grid_size+1)*sizex),border-sizey,sizex,(grid_size+2)*sizey)
    pygame.draw.rect(screen,(color0), rectangle)

    rectangle = pygame.Rect(border-sizex,(border-sizey)+((grid_size+1)*sizey),(grid_size+2)*sizex,sizey)
    pygame.draw.rect(screen,(color0), rectangle)

def drawapple():
    for a in range(len(appleco)):
        drawpic("apple.png",appleco[a])

match difficulty:
    case "easy":
        speed = 0.1
        loop = True
    case "medium":
        speed = 0.07
        loop = False
    case "hard":
        speed = 0.05
        loop = False
    case "insane":
        speed = 0.03
        loop = False        
    case "what":
        speed = 0
        loop = True
        grid_size = 200
        appleamount = 2000
    case "custom":
        speed = 0.05
        loop = True

sizey = ((screen_hight-border*2)/grid_size)
sizex = ((screen_hight-border*2)/grid_size)
direction=""
appleco = []
drawgrid()
snakey = int(grid_size/2)
snakex = int(grid_size/2)
snake = [str(int(grid_size/2))+","+str(int(grid_size/2))]
for a in range(appleamount):
    applex = random.randint(1,grid_size)
    appley = random.randint(1,grid_size)
    while str(applex)+","+str(appley) in snake or str(applex)+","+str(appley) in appleco:
        applex = random.randint(1,grid_size)
        appley = random.randint(1,grid_size)
    appleco.append(str(applex)+","+str(appley))
    drawpic("apple.png",str(applex)+","+str(appley)
            )
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

        if event.type == pygame.KEYDOWN:
            key = event.key
            if snakex > 0 and snakey > 0 and snakex < grid_size+1 and snakey < grid_size+1:
                if inputthisframe == False:
                    if key == pygame.K_LEFT:
                        if not direction == "right":                
                            direction = "left"
                            inputthisframe = True
                    elif key == pygame.K_RIGHT:
                        if not direction == "left":
                            direction = "right"
                            inputthisframe = True
                    elif key == pygame.K_UP:
                        if not direction == "down":
                            direction = "up"
                            inputthisframe = True
                    elif key == pygame.K_DOWN:
                        if not direction == "up":
                            direction = "down"
                            inputthisframe = True
            if key == pygame.K_a:
                drawgrid()
                appleco = []
                for a in range(appleamount):
                    appleco.append(str(random.randint(1,grid_size-1))+","+str(random.randint(1,grid_size-1)))
                    drawpic("apple.png",appleco[a])
                snakey = int(grid_size/2)
                snakex = int(grid_size/2)
                snake = [str(int(grid_size/2))+","+str(int(grid_size/2))]
                direction=""
                snakelengh = 3
                alive = True
                print("uh")
                pygame.display.update()
    inputthisframe = False
    time.sleep(speed)
    if alive == True:
        match direction:
            case "up":
                if str(snakex)+","+str(snakey-1) in snake[1:]:
                    alive = False
                snakey -=1
                snake.append(str(snakex)+","+str(snakey))
            case "down":
                if str(snakex)+","+str(snakey+1) in snake[1:]:
                    alive = False
                snakey +=1
                snake.append(str(snakex)+","+str(snakey))
            case "right":
                if str(snakex+1)+","+str(snakey) in snake[1:]:
                   alive = False
                snakex +=1 
                snake.append(str(snakex)+","+str(snakey))
            case "left":
                if str(snakex-1)+","+str(snakey) in snake[1:]:
                    alive = False
                snakex -=1
                snake.append(str(snakex)+","+str(snakey))
        match loop:
            case False:        
                if snakex > grid_size or snakey > grid_size or snakex < 1 or snakey < 1:
                    alive = False
                    inputthisframe = False
            case True:
                if snakex > grid_size:
                    snakex = 0
                    drawpic("snake.left.png",str(snakex+1)+","+str(snakey))                    
                if snakey > grid_size:
                    snakey = 0
                    drawpic("snake.up.png",str(snakex)+","+str(snakey+1)) 
                if snakex < 1:
                    if direction == "left":
                        snakex = grid_size+1
                        drawpic("snake.right.png",str(snakex-1)+","+str(snakey)) 
                if snakey < 1:
                    if direction == "up":
                        snakey = grid_size+1
                        drawpic("snake.down.png",str(snakex)+","+str(snakey-1)) 
        if str(snakex)+","+str(snakey) in appleco :
            drawsquare(snakex-1,snakey-1)
            drawsnake(len(snake)-2)
            appleco.remove(str(snakex)+","+str(snakey))
            snakelengh +=1
            applex = random.randint(1,grid_size-1)
            appley = random.randint(1,grid_size-1)
            while str(applex)+","+str(appley) in snake or str(applex)+","+str(appley) in appleco:
                applex = random.randint(1,grid_size)
                appley = random.randint(1,grid_size)
            appleco.append(str(applex)+","+str(appley))
            drawpic("apple.png",str(applex)+","+str(appley))
        if len(snake) > snakelengh :
            delseg()
        sizey = ((screen_hight-border*2)/grid_size)
        sizex = ((screen_hight-border*2)/grid_size)
        if 1 == 0:
            grid_size += 1
            t1 = threading.Thread(target=drawgrid, args=())
            t1.start()
            t1.join()
            drawsnake("whole")
            drawapple()
        t2 = threading.Thread(target=drawsnake, args=((len(snake)-2),))
        t2.start()
        t2.join()
        drawborder()
    pygame.display.update()
pygame.quit()