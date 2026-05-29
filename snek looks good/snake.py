import pygame
import random
import sys
import time
import threading

# Initialize Pygame
pygame.init()

screen_width = 1000
screen_hight = 1000
# Set up the game window
screen = pygame.display.set_mode((screen_width, screen_hight))
pygame.display.set_caption("Hello Pygame")
clock = pygame.time.Clock()

FPS = 60

if 1==0:
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Fullscreen Game")
    screen_width = screen.get_width()
    screen_hight = screen.get_height()



grid_size = 20
coordinates = []
co_y = 1
gridcolor = (0,255,255)
width_width = 1


sizey = (screen_hight/grid_size)
sizex = (screen_hight/grid_size)
x = 0
y = 0
ia = 0
cordoutput = []
i = 1

color1 = (50,200,50)
color2 = (50,180,50)



co = []
coordinates = []
i = 1
co_y = 1
def createco():
#if 1 == 1:

    i=1
    co_y = 1
    co = []

    for f in range(grid_size*grid_size):
        if i == grid_size+1:
            co_y += 1
            i = 1
        co.append(str(i)+","+str(co_y))
        i += 1
    return co

coordinates = createco()

def getcord(item):
    cordoutput=[]
    gc = item.split(",")
    cordoutput.append((int(int(gc[0])-1)*int(sizex)))
    cordoutput.append((int(int(gc[1])-1)*int(sizey)))
    return cordoutput

def drawgrid():
    for i in range(grid_size*grid_size):
        x = getcord(coordinates[i])[0]
        y = getcord(coordinates[i])[1]

        rectangle = pygame.Rect(x,y,sizex,sizey)
        print(rectangle)
        if int(y/sizey)%2 == 1:
            if int(x/sizex)%2 == 1 :
                color = color1
            else:
                color = color2
        else:
            if int(x/sizex)%2 == 1 :
                color = color2
            else:
                color = color1
        print(color)
        pygame.draw.rect(screen,(color), rectangle)


        #pygame.draw.rect(screen,(gridcolor), rectangle, width_width)





    
def drawpic(picture,cords):

    str(picture)
    picture = pygame.image.load(picture)
    if picture == "apple.png":


        pic = pygame.transform.scale(picture,(sizex-width_width*2,sizey-width_width*2))

        screen.blit(pic,(getcord(cords)[0]+width_width,getcord(cords)[1]+width_width))
    else :
        pic = pygame.transform.scale(picture,(sizex,sizey))
  
        screen.blit(pic,(getcord(cords)[0],getcord(cords)[1]))

def drawsnake():

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

drawgrid()

snakey = int(grid_size/2)
snakex = int(grid_size/2)
snake = [str(int(grid_size/2))+","+str(int(grid_size/2))]
snakelengh = 100


direction=""
#game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    time.sleep(0.0)    
    if event.type == pygame.KEYDOWN:
        key = event.key
        if key == pygame.K_LEFT:
            direction = "left"
        if key == pygame.K_RIGHT:
            direction = "right"
        if key == pygame.K_UP:
            direction = "up"
        if key == pygame.K_DOWN:
            direction = "down"


 #   print(direction)
  #  print(snake)
    match direction:
        case "up":
            snakey -=1
            snake.append(str(snakex)+","+str(snakey))
        case "down":
            snakey +=1
            snake.append(str(snakex)+","+str(snakey))
        case "right":
            snakex +=1 
            snake.append(str(snakex)+","+str(snakey))
        case "left":
            snakex-=1
            snake.append(str(snakex)+","+str(snakey))
    if len(snake) > snakelengh :
        snake.pop(0)

    sizey = (screen_hight/grid_size)
    sizex = (screen_hight/grid_size)





#    grid_size+=1
#    coordinates = createco()





#    screen.fill((0, 0, 0))
#    drawpic("apple.png",str(random.randint(1,grid_size))+","+str(random.randint(1,grid_size)))
#    drawgrid()

    t1 = threading.Thread(target=drawgrid, args=())
    t1.start()
    t1.join()
    drawpic("apple.png",str(5)+","+str(5))
    t2 = threading.Thread(target=drawsnake, args=())
    t2.start()
    t2.join()


#    drawsnake()
    pygame.display.update()



# Quit Pygame
pygame.quit()