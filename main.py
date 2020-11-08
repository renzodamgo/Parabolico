import pygame
import math
import evolution
import random
import create_df 
# pygame.init()


# pygame.font.init()
# win = pygame.display.set_mode((960, 540))
# tank = pygame.image.load('./source/tank.png')
# parkbg = pygame.image.load('./source/southpark_bg.png')
# kenny = pygame.image.load('./source/kenny.png')
# kenny = pygame.transform.scale(kenny, (64, 74))
# pygame.display.set_caption("Redes Neuronales")
# myfont = pygame.font.SysFont('arial', 35)


#myfont = pygame.font.Font(pygame.font.get_default_font(), 35)

#textsurface = myfont.render('Generación: ' + "0", True, (0, 0, 0))
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
    #win.blit(textsurface, (750, 10))
    pygame.display.update()


# def findAngle(pos):
#     sX = golfBall.x
#     sY = golfBall.y
#     try:
#         angle = math.atan((sY-pos[1])/(sX - pos[0]))
#     except:
#         angle = math.pi/2

#     if pos[1] < sY and pos[0] > sX:
#         angle = abs(angle)
#     elif pos[1] < sY and pos[0] < sX:
#         angle = math.pi - angle
#     elif pos[1] > sY and pos[0] < sX:
#         angle = math.pi + abs(angle)
#     elif pos[1] > sY and pos[0] > sX:
#         angle = (math.pi*2) - angle
#     return angle


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

run = True
while run:

    #textsurface = myfont.render('Generación: ' + str(e.gen), False, (0, 0, 0))

    if shoot:
        if golfBall.y < 460 - golfBall.radius:
            # time += 0.05
            time += 0.5
            po = ball.ballPath(x, y, power, angle, time)
            golfBall.x = po[0]
            golfBall.y = po[1]
        else:
            xmax = golfBall.x
            if 650<xmax<750:
                out.append(1)
            else:
                out.append(0)
            count += 1
            shoot = False
            golfBall.y = 435
            golfBall.x = 181
            if count == 1000000:
                break
            # if n < 9:
            #     n += 1

    # pos = pygame.mouse.get_pos()
    # line = [(golfBall.x, golfBall.y), pos]


    # redrawWindow()

    # for event in pygame.event.get():

    #     if event.type == pygame.QUIT:
    #         run = False

        # if event.type == pygame.MOUSEBUTTONDOWN:

    if shoot == False:
        shoot = True
        x = golfBall.x
        y = golfBall.y
        time = 0
        power = random.randrange(0,60)
        angle = random.randrange(0,90)

        p.append(power)
        a.append(angle)
        
        angle = angle *math.pi/180
create_df.savedf(p,a,out)

    
pygame.quit()
