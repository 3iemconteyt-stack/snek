import pygame
import random
import sys
import time
import threading
pygame.init()
pygame.font.init()
"""screen_width = 1000
screen_hight = 1000
screen = pygame.display.set_mode((screen_width, screen_hight))
pygame.display.set_caption("3iem_conte's snake")
clock = pygame.time.Clock()"""

FPS = 60

if 1==1:
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Snake By 3iem_conte")
    screen_width = screen.get_width()
    screen_hight = screen.get_height()

border = 50
appleamount = 1
snakelengh = 3
grid_size = 20
gamemode = "survival"
difficulty = "easy"

difficultylist =["easy","medium","hard","insane"]
difficultylistindex = 0
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
money = 0
my_font = pygame.font.SysFont('Bauhaus 93', 45)
picsize = 50
settingsx = (screen_width-70)-70
settingsy = picsize
settingsize = 70
def getcord(item):
    cordoutput=[]
    gc = item.split(",")
    cordoutput.append((int(int(gc[0])-1)*int(sizex)))
    cordoutput.append((int(int(gc[1])-1)*int(sizey)))
    return cordoutput

def drawsquare(x,y):
        rectangle = pygame.Rect((x*sizex+border),(y*sizey+border),(sizex),(sizey))
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
            drawsquare(x,y)
            """rectangle = pygame.Rect(x*sizex+border,y*sizey+border,sizex,sizey)
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
            pygame.draw.rect(screen,(color), rectangle)"""

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

    #lastseg= 2
    #while True:
    #    if snake[0] in snake[lastseg:]:
    #        drawsnake(snake.index(snake[0],lastseg))
    #        if snake.index(snake[0],lastseg)-1 != len(snake):
    #            drawsnake(snake.index(snake[0],lastseg)-1)
    #        lastseg = snake.index(snake[0],lastseg)+1
    #    else:
    #        break

    snake.pop(0)
    drawsnake(0)

def drawborder():
    rectangle = pygame.Rect(0,0,(grid_size+2)*sizex,border)
    pygame.draw.rect(screen,(color0), rectangle)

    rectangle = pygame.Rect(0,0,border,(grid_size+2)*sizey)
    pygame.draw.rect(screen,(color0), rectangle)
    
    rectangle = pygame.Rect((border-sizex)+((grid_size+1)*sizex),0,screen_width,screen_width)
    pygame.draw.rect(screen,(color0), rectangle)

    rectangle = pygame.Rect(0,(border-sizey)+((grid_size+1)*sizey),screen_width,screen_hight)
    pygame.draw.rect(screen,(color0), rectangle)

def drawapple():
    for a in range(len(appleco)):
        drawpic("apple.png",appleco[a])

def drawtext(text,x,y,color):
    text_surface = my_font.render(text, False, color)
    screen.blit(text_surface, (x,y))

def drawpicture(picture,xa,ya,size):
    str(picture)
    picture = pygame.image.load(picture)
    pic = pygame.transform.scale(picture,(size,size))
    screen.blit(pic,(xa,ya))

def checkmousecolision(corner1x, corner1y, corner2x, corner2y):
    if mousex > corner1x and mousey > corner1y and mousex < corner2x and mousey < corner2y:
        return True
    else:
        return False

def restart():
                    global speed
                    global loop
                    global colision 
                    global snake
                    global snakelengh
                    global snakex
                    global snakey
                    global direction
                    global alive
                    global difficulty
                    global difficultylist
                    global difficultylistindex
                    global appleamount
                    global appleco
                    global grid_size
                    global sizex
                    global sizey
                    sizey = int((screen_hight-border*2)/grid_size)
                    sizex = int((screen_hight-border*2)/grid_size)
                    if difficultylistindex < 0:
                        difficultylistindex = len(difficultylist)-1
                    if difficultylistindex > len(difficultylist)-1:
                        difficultylistindex =0
                    difficulty = difficultylist[difficultylistindex]

                    match difficulty:
                        case "easy":
                            speed = 0.1
                            loop = True
                            colision = True
                        case "medium":
                            speed = 0.07
                            loop = False
                            colision = True
                        case "hard":
                            speed = 0.05
                            loop = False
                            colision = True
                        case "insane":
                            speed = 0.03
                            loop = False    
                            colision = True
                        case "what":
                            speed = 0
                            loop = True
                            colision = False
                            grid_size = 200
                            appleamount = 16000
                        case "custom":
                            speed = 0.01
                            loop = True
                            colision = False
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
                    pygame.display.update()    

def save():
    with open("snakesave.txt","w") as save:
        save.write(str(money)+"\n")
        save.write(str(difficultylistindex)+"\n")
        save.write(str(difficultylist)+"\n")
        save.write(str("1")+"\n")
        save.write(str("1")+"\n")

def load():
    global money
    global difficultylistindex
    global difficultylist
    with open("snakesave.txt","r") as save:
        lines = save.readlines()
        money = int((lines[0]).replace("\n",""))
        difficultylistindex = int((lines[1]).replace("\n",""))
        difficultylist = (lines[2]).replace("\n","").replace("[","").replace("]","").replace("'","") .split(",")
        print(difficultylist)   
#save()
load()
restart()
difficultybuttonposx = int((grid_size+2)*sizex+100)
difficultybuttonposy = 150

running = True
inputthisframe = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

        if event.type == pygame.KEYDOWN:
            key = event.key
            if snakex > 0 and snakey > 0 and snakex < grid_size+1 and snakey < grid_size+1:
                if inputthisframe == False:
                    if alive == True:
                        if key == pygame.K_LEFT or key == pygame.K_q or key == pygame.K_a:
                            if not direction == "right":                
                                direction = "left"
                                inputthisframe = True
                        elif key == pygame.K_RIGHT or key == pygame.K_d:
                            if not direction == "left":
                                direction = "right"
                                inputthisframe = True
                        elif key == pygame.K_UP or key == pygame.K_z or key == pygame.K_w:
                            if not direction == "down":
                                direction = "up"
                                inputthisframe = True
                        elif key == pygame.K_DOWN or key == pygame.K_s:
                            if not direction == "up":
                                direction = "down"
                            inputthisframe = True
            if key == pygame.K_SPACE:
                restart()
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                mousex, mousey = pygame.mouse.get_pos()
                if checkmousecolision(difficultybuttonposx,difficultybuttonposy,difficultybuttonposx+picsize,difficultybuttonposy+picsize):
                    difficultylistindex -= 1
                    restart()
                if checkmousecolision(difficultybuttonposx+300,difficultybuttonposy,difficultybuttonposx+300+picsize,difficultybuttonposy+picsize):
                    difficultylistindex += 1
                    restart()

    inputthisframe = False
    time.sleep(speed)
    if alive == True:
        match direction:
            case "up":
                if str(snakex)+","+str(snakey-1) in snake[1:] and colision:
                    alive = False
                snakey -=1
                snake.append(str(snakex)+","+str(snakey))
            case "down":
                if str(snakex)+","+str(snakey+1) in snake[1:] and colision:
                    alive = False
                snakey +=1
                snake.append(str(snakex)+","+str(snakey))
            case "right":
                if str(snakex+1)+","+str(snakey) in snake[1:] and colision:
                    alive = False
                snakex +=1 
                snake.append(str(snakex)+","+str(snakey))
            case "left":
                if str(snakex-1)+","+str(snakey) in snake[1:] and colision:
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
            money += 1
            if len(snake) + len(appleco) < grid_size*grid_size:
                applex = random.randint(1,grid_size-1)
                appley = random.randint(1,grid_size-1)
                while str(applex)+","+str(appley) in snake or str(applex)+","+str(appley) in appleco:
                    applex = random.randint(1,grid_size)
                    appley = random.randint(1,grid_size)
                appleco.append(str(applex)+","+str(appley))
                drawpic("apple.png",str(applex)+","+str(appley))
        if len(snake) > snakelengh :
            delseg()
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

    drawtext("score "+str(snakelengh),((grid_size+2)*sizex)/2,0,(0,0,0))   
    drawtext(": "+str(money),((grid_size+2)*sizex)+50+picsize,50,(0,0,0))
    drawpicture("apple.png",int((grid_size+2)*sizex+50),50,picsize)
    text_width, text_height = my_font.size(str(difficulty))

    drawpicture("arrow.left.png",difficultybuttonposx,difficultybuttonposy,picsize)
    drawtext(str(difficulty),(difficultybuttonposx+picsize)+((250/2-(text_width/2))),difficultybuttonposy,(0,0,0))
    drawpicture("arrow.right.png",difficultybuttonposx+300,difficultybuttonposy,picsize)

    drawpicture("setting.png",settingsx,settingsy,settingsize)    
    pygame.display.update()
pygame.quit()