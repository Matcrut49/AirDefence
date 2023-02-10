import pygame
import random
import time
from math import *
import itertools
def rotate(surface, angle, pivot, offset): 
    rotated_image = pygame.transform.rotozoom(surface, -angle, 1)  
    rotated_offset = offset.rotate(angle) 
    rect = rotated_image.get_rect(center=pivot+rotated_offset)
    return rotated_image, rect 
a = 120
speed = -500
score = 0
class BULLET():
    def __init__(self, x, y, speed) -> None:
         self.x = x
         self.y = y
         self.speedx = speed *sin(atan((SCREEN_WIDTH / 2 + random.randint(400, 500) - x) / (SCREEN_HEIGHT - 170 - y)))
         self.speedy = speed * cos((atan((SCREEN_WIDTH / 2 + random.randint(400, 500) - x) / (SCREEN_HEIGHT - 170 - y))))
    def spawn(self):
        pygame.draw.circle(screen, "WHITE", (self.x, self.y), 25)
    def move(self):
        self.x += self.speedx; self.y += self.speedy
    def despawn(self):
            self.x = -100
            self.y = -100
            self.spawn()

class PVOBULLET():
        def __init__(self, x, y, speedx, sppedy, angle) -> None:
         self.x = x
         self.y = y
         self.speedx = speedx
         self.speedy = sppedy
         self.angle = angle
        def spawn(self):
            pygame.draw.circle(screen, "WHITE", (self.x, self.y), 10)
        def update(self):
            self.speedy += 3
            self.x += ((self.speedx) * cos(radians(self.angle))) / 60; self.y += ((self.speedy) * sin(radians(self.angle)) + 30 ) / 60
        def despawn(self):
            self.x = -100
            self.y = -100
            self.spawn()
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
BG_COLOR = (250, 100, 50)
PADDLE_COLOR = (20, 20, 20)
STAND_COLOR = (46, 102, 159)
HOME_COLOR = (30, 250, 17)
HOME_COLOR1 = (255, 0 , 0)

field = pygame.Rect(0, SCREEN_HEIGHT - 100,  SCREEN_WIDTH, 100)
stand = pygame.Rect((SCREEN_WIDTH / 2 - 100),SCREEN_HEIGHT - 140 , 200, 40)
home =  pygame.Rect((SCREEN_WIDTH / 2 + 400),SCREEN_HEIGHT - 170 , 100, 70)

offset = pygame.math.Vector2(0, -25)
pivot = [(SCREEN_WIDTH / 2), SCREEN_HEIGHT - 120]
angle = 0

massive1 = [BULLET(random.randint(200 , 1400), -100, random.randint(1, 3)) for i in range(2)]
massive2 = [None for i in range(3)]
player_img = pygame.image.load("gun3.png")
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("AirDefense")
run = True
BULLET.x = random.randint(100, 1500); BULLET.y = random.randint(50, 500)
#print((SCREEN_WIDTH / 2 + (sin(radians(90 + angle)) * 120)), (SCREEN_HEIGHT -  (100 + (cos(radians(90 + angle)) * 120))))
while run:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d] and angle <= 75:
            angle += 1
    elif keys[pygame.K_a] and angle >= -75:
            angle -= 1
    if keys [pygame.K_SPACE]:    
        for i in range(len(massive2)):
            if massive2[i] == None and a >= 120:
                a = 0
                massive2[i] = PVOBULLET((SCREEN_WIDTH / 2 + (sin(radians(angle)) * 120)), (SCREEN_HEIGHT - (120 + cos(radians(angle)) * 120)),speed, speed, angle + 90)
                print(massive2)
                break
    a += 1
    rotated_image, rect = rotate(player_img, angle, pivot, offset)
    screen.fill(BG_COLOR)
    screen.blit(rotated_image, rect)
    pygame.draw.rect(screen, PADDLE_COLOR, field)
    pygame.draw.rect(screen, STAND_COLOR, stand)
    pygame.draw.rect(screen, HOME_COLOR, home)
    for bulet1, bulllet2 in itertools.product (massive1, massive2):

        if bulllet2 != None and bulet1 != None: 
            if ((abs(bulllet2.x - bulet1.x) <= 25) and(abs(abs(bulllet2.y - bulet1.y) <= 25))):
                print(True) 
                bulllet2.despawn()
                bulllet2 = None
                bulet1.despawn()
                bulet1 = None
                score += 1
        

    for bulet1 in range(len(massive1)):
            if massive1[bulet1] == None:
                massive1[bulet1] = BULLET(random.randint(200 , 1400), 100, random.randint(5 ,7))
            if massive1[bulet1] != None and (massive1[bulet1].y >= 800 or massive1[bulet1].x <= 0 or massive1[bulet1].x >= 1600):
                b = massive1.index(massive1[bulet1])
                massive1[bulet1] = None
            if massive1[bulet1] != None:
                massive1[bulet1].spawn()
                massive1[bulet1].move()
            if massive1[bulet1] != None and(massive1[bulet1].x >= ((SCREEN_WIDTH / 2 + 400) and massive1[bulet1].x <= (SCREEN_WIDTH / 2 + 330)) and (massive1[bulet1].y >= (SCREEN_HEIGHT - 170) and massive1[bulet1].y <= (SCREEN_HEIGHT - 100))):
                massive1[bulet1] = None
                pygame.draw.rect(screen, HOME_COLOR1, home)
                score -= 1
    for bulllet2 in range(len(massive2)):
        
            if massive2[bulllet2] != None:
                massive2[bulllet2].spawn()
                massive2[bulllet2].update()  
            if massive2[bulllet2] != None and (massive2[bulllet2].y >= 800 or massive2[bulllet2].x <= 0 or massive2[bulllet2].x >= 1600):
                massive2[bulllet2] = None
    font1 = pygame.font.SysFont('arialmt.ttf', 50)
    text1 = font1.render(str(score), True, (0, 255, 0))
    textRect1 = text1.get_rect()
    textRect1.center = (50, 50)
    screen.blit(text1, textRect1)
    clock.tick(60)
    #print(cos(radians(angle)))
    pygame.display.flip()
