import math
import random
import create_df 
import time as t

n = 0





class ball(object):
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    # def draw(self, win):
    #     pygame.draw.circle(win, (0, 0, 0), (self.x, self.y), self.radius)
    #     pygame.draw.circle(win, self.color, (self.x, self.y), self.radius-1)

    @staticmethod
    def ballPath(startx, starty, power, ang, time):
        velx = math.cos(angle) * power
        vely = math.sin(angle) * power

        distX = velx * time
        distY = (vely*time) + ((-4.9 * (time)**2)/2)

        newx = round(distX + startx)
        newy = round(starty-distY)
        return(newx, newy)







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
            delta = abs(700 - xmax)
            if delta < 50 :
                out.append(0)
            elif delta < 200:
                out.append(1)
            elif  delta <500:
                out.append(2)
            else:
                out.append(3)
            
            count += 1
            shoot = False
            golfBall.y = 435
            golfBall.x = 181
            if count == 7000:
                break
            # if n < 9:
            #     n += 1

    # pos = pygame.mouse.get_pos()
    # line = [(golfBall.x, golfBall.y), pos]


    
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

    
