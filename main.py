import pygame
import math

# pygame.init()

win = pygame.display.set_mode((960, 540))
tank = pygame.image.load('./source/tank.png')
parkbg = pygame.image.load('./source/southpark_bg.png')
kenny = pygame.image.load('./source/kenny.png')
kenny = pygame.transform.scale(kenny, (64, 74))
pygame.display.set_caption("Tanks")


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
        distY = (vely*time) + ((-9.81 * (time)**2)/2)

        newx = round(distX + startx)
        newy = round(starty-distY)
        return(newx, newy)


def redrawWindow():

    win.fill((64, 64, 64))
    win.blit(parkbg, (0, 0))
    golfBall.draw(win)
    pygame.draw.line(win, (255, 255, 255), line[0], line[1])
    win.blit(tank, (120, 420))
    win.blit(kenny, (700, 410))
    pygame.display.update()


def findAngle(pos):
    sX = golfBall.x
    sY = golfBall.y
    try:
        angle = math.atan((sY-pos[1])/(sX - pos[0]))
    except:
        angle = math.pi/2

    if pos[1] < sY and pos[0] > sX:
        angle = abs(angle)
    elif pos[1] < sY and pos[0] < sX:
        angle = math.pi - angle
    elif pos[1] > sY and pos[0] < sX:
        angle = math.pi + abs(angle)
    elif pos[1] > sY and pos[0] > sX:
        angle = (math.pi*2) - angle
    return angle


golfBall = ball(181, 435, 5, (255, 255, 255))
x = 0
y = 0
time = 0
power = 0
angle = 0
shoot = False

run = True
while run:

    if shoot:
        if golfBall.y < 460 - golfBall.radius:
            # time += 0.05
            time += 0.05
            po = ball.ballPath(x, y, power, angle, time)
            golfBall.x = po[0]
            golfBall.y = po[1]
        else:
            shoot = False
            golfBall.y = 435
            golfBall.x = 181
    pos = pygame.mouse.get_pos()
    line = [(golfBall.x, golfBall.y), pos]
    redrawWindow()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:

            if shoot == False:
                shoot = True
                x = golfBall.x
                y = golfBall.y
                time = 0
                power = (math.sqrt(
                    (line[1][1] - line[0][1])**2 + (line[1][0]-line[0][0])**2))/8
                # power = 50
                # print(power)
                angle = findAngle(pos)
                # angle = 1
                print("power = ", power, " angle = ", angle)
                #print(pos[0], pos[1])


pygame.quit()
