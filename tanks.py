import pygame
import math
import random
import create_df 
import time as t

# pygame.init()

#print(Multicapa.getpred([[39.0, 46.0]]))
pygame.font.init()
win = pygame.display.set_mode((960, 540))
tank = pygame.image.load('./source/tank.png')
parkbg = pygame.image.load('./source/southpark_bg.png')
kenny = pygame.image.load('./source/kenny.png')
kenny = pygame.transform.scale(kenny, (64, 74))

pygame.display.set_caption("Redes Neuronales")
myfont = pygame.font.SysFont('arial', 35)

frame_time = 0.004

#myfont = pygame.font.Font(pygame.font.get_default_font(), 35)

n = 0



# pygame.font.get_fonts()


class ball(object):
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self, win):
        pygame.draw.circle(win, (0, 0, 0), (self.x, self.y), self.radius)
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius-1)

    @staticmethod
    def ballPath(startx, starty, power, ang, time):
        velx = math.cos(angle) * power
        vely = math.sin(angle) * power

        distX = velx * time
        distY = (vely*time) + ((-4.9 * (time)**2)/2)

        newx = round(distX + startx)
        newy = round(starty-distY)
        return(newx, newy)


def redrawWindow():

    win.fill((64, 64, 64))
    win.blit(parkbg, (0, 0))

    golfBall.draw(win)
    #pygame.draw.line(win, (255, 255, 255), line[0], line[1])
    win.blit(tank, (120, 420))
    win.blit(kenny, (700, 410))
    
    pygame.display.update()




golfBall = ball(181, 435, 5, (255, 255, 255))
x = 0
y = 0
time = 0
power = 0
angle = 0
shoot = False
p = []
a = []
out = []
count = 0
pred = ""
run = True
while run:
    
    
    
    if shoot:
        if golfBall.y < 460 - golfBall.radius:
            # time += 0.05
            time += 0.5
            po = ball.ballPath(x, y, power, angle, time)
            golfBall.x = po[0]
            golfBall.y = po[1]
        else:
            xmax = golfBall.x
            
            count += 1
            shoot = False
            golfBall.y = 435
            golfBall.x = 181
            if count == 1000:
                break
            # if n < 9:
            #     n += 1

    # pos = pygame.mouse.get_pos()
    # line = [(golfBall.x, golfBall.y), pos]


    redrawWindow()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pass

    if shoot == False:
        shoot = True
        
        x = golfBall.x
        y = golfBall.y
        time = 0

        power = random.randrange(0,60)
        angle = random.randrange(0,365)
        # power = 50.84673662094747
        # angle = 0.696626848077909
        
        p.append(power)
        a.append(angle)
        
        # angle = angle *math.pi/180
        print("power = ", power, " angle = ", angle)
    t.sleep(frame_time)


    
pygame.quit()
