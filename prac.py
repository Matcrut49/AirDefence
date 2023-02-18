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
speed = -700
score = 0
b = 0

class BULLET():
    def __init__(self, x, y, speed) -> None:
         self.x = x
         self.y = y
         self.speedx = speed *sin(atan((Shirina / 2 + random.randint(400, 500) - x) / (Height - 170 - y)))
         self.speedy = speed * cos((atan((Shirina / 2 + random.randint(400, 500) - x) / (Height - 170 - y))))
    def spawn(self):
        pygame.draw.circle(movie, (8, 46, 161), (self.x, self.y), 25)
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
            pygame.draw.circle(movie, "Black", (self.x, self.y), 10)
        def update(self):
            self.speedy += 3
            self.x += ((self.speedx) * cos(radians(self.angle))) / 60; self.y += ((self.speedy) * sin(radians(self.angle)) + 30 ) / 60
        def despawn(self):
            self.x = -100
            self.y = -100
            self.spawn()
Shirina = 1600
Height = 900
ColorBg = (230, 173, 233)
ZemlaColor = (20, 20, 20)
Podstacka = (46, 1, 159)
Hme = (30, 250, 17)
Home1 = (255, 0 , 0)

field = pygame.Rect(0, Height - 100,  Shirina, 100)
stand = pygame.Rect((Shirina / 2 - 100),Height - 140 , 200, 40)
home =  pygame.Rect((Shirina / 2 + 400),Height - 170 , 100, 70)

offset = pygame.math.Vector2(0, -25)
pivot = [(Shirina / 2), Height - 120]
angle = 0

massive1 = [BULLET(random.randint(200 , 1400), -100, random.randint(1, 2)) for i in range(2)]
massive2 = [None for i in range(10)]
player_img = pygame.image.load("gun3.png")
pygame.init()
clock = pygame.time.Clock()
movie = pygame.display.set_mode((Shirina, Height))
pygame.display.set_caption("AirDefense")
run = True
vivod = [[] for i in range(len(massive1))]
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
            if massive2[i] == None and a >= 30:
                a = 0
                massive2[i] = PVOBULLET((Shirina / 2 + (sin(radians(angle)) * 120)), (Height - (120 + cos(radians(angle)) * 120)),speed, speed, angle + 90)
                break
    a += 1
    rotated_image, rect = rotate(player_img, angle, pivot, offset)
    movie.fill(ColorBg)
    movie.blit(rotated_image, rect)
    if b >= 0:
            pygame.draw.rect(movie, Home1, home)
            b -= 1
    else:
        pygame.draw.rect(movie, Hme, home)
    pygame.draw.rect(movie, ZemlaColor, field)
    pygame.draw.rect(movie, Podstacka, stand)
    for bulet1, bulllet2 in itertools.product (massive1, massive2):
        if bulllet2 != None and bulet1 != None: 
            if ((abs(bulllet2.x - bulet1.x) <= 25) and(abs(abs(bulllet2.y - bulet1.y) <= 25))):
                bulllet2.despawn()
                bulllet2 = None
                bulet1.despawn()
                bulet1 = None
                score += 1
        

    for bulet1 in range(len(massive1)):
        if massive1[bulet1] != None:
            vivod[bulet1].append(bulet1)
            vivod[bulet1].append((round(abs((Shirina / 2  - massive1[bulet1].x) ** 2 + (Height - 100 - massive1[bulet1].y ** 2)) ** 0.5)))
            vivod[bulet1].append((round(degrees(atan((Shirina / 2  - massive1[bulet1].x) / (Height - 100 - massive1[bulet1].y))))))
        else:
            vivod[bulet1] = [bulet1, None]
        if massive1[bulet1] == None:
            massive1[bulet1] = BULLET(random.randint(200 , 1400), 100, random.randint(5 ,7))
        if massive1[bulet1] != None and (massive1[bulet1].y >= 800 or massive1[bulet1].x <= 0 or massive1[bulet1].x >= 1600):
            b = massive1.index(massive1[bulet1])
            massive1[bulet1] = None
        if massive1[bulet1] != None:
            massive1[bulet1].spawn()
            massive1[bulet1].move()
        if massive1[bulet1] != None and(massive1[bulet1].x >= ((Shirina / 2 + 400) and massive1[bulet1].x <= (Shirina / 2 + 330)) and (massive1[bulet1].y >= (Height - 170) and massive1[bulet1].y <= (Height - 100))):
            massive1[bulet1] = None
            score -= 1
            b = 60
    for bulllet2 in range(len(massive2)):        
            if massive2[bulllet2] != None:
                massive2[bulllet2].spawn()
                massive2[bulllet2].update()  
            if massive2[bulllet2] != None and (massive2[bulllet2].y <= 0 or massive2[bulllet2].y >= 800 or massive2[bulllet2].x <= 0 or massive2[bulllet2].x >= 1600):
                massive2[bulllet2] = None
    font1 = pygame.font.SysFont('arialmt.ttf', 50)
    text1 = font1.render(str(score), True, (0, 255, 0))
    textRect1 = text1.get_rect()
    textRect1.center = (50, 50)
    viv = []
    for i in vivod:
        viv.append(''.join(str(i)))
    print('SCANNING', ''.join(str(viv)))
    vivod = [[] for i in range(len(massive1))]
    movie.blit(text1, textRect1)
    clock.tick(60)
    pygame.display.flip()
