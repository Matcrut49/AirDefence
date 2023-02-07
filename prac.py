import pygame
import random
import time
from math import *
def rotate(surface, angle, pivot, offset): 
    rotated_image = pygame.transform.rotozoom(surface, -angle, 1)  
    rotated_offset = offset.rotate(angle) 
    rect = rotated_image.get_rect(center=pivot+rotated_offset)
    return rotated_image, rect 

class BULLET():
    def __init__(self, x, y, speedx, sppedy) -> None:
         self.x = x
         self.y = y
         self.speedx = speedx
         self.speedy = sppedy
    def spawn(self):
        pygame.draw.circle(screen, "WHITE", (self.x, self.y), 25)
    def move(self):
        self.x += self.speedx; self.y += self.speedy

class PVOBULLET():
        def __init__(self, x, y, speedx, sppedy) -> None:
         self.x = x
         self.y = y
         self.speedx = speedx
         self.speedy = sppedy
        def spawn(self):
            pygame.draw.circle(screen, "WHITE", (self.x, self.y), 10)
        def move(self):
            self.x += self.speedx; self.y += self.speedy
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
BG_COLOR = (250, 100, 50)
PADDLE_COLOR = (20, 20, 20)
GUN_COLOR = (250, 250, 250)
STAND_COLOR = (46, 102, 159)

field = pygame.Rect(0, SCREEN_HEIGHT - 100,  SCREEN_WIDTH, 100)
stand = pygame.Rect((SCREEN_WIDTH / 2 - 35),SCREEN_HEIGHT - 140 , 70, 40)

offset = pygame.math.Vector2(0, -25)
pivot = [(SCREEN_WIDTH / 2), SCREEN_HEIGHT - 100]
angle = 0


player_img = pygame.image.load("gun1.png")
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("AirDefense")
bulet1 = BULLET(700, 300, -3, 3)
run = True
BULLET.x = random.randint(100, 1500); BULLET.y = random.randint(50, 500)

print((SCREEN_WIDTH / 2 + (sin(radians(90 + angle)) * 120)), (SCREEN_HEIGHT -  (100 + (cos((radians(90 + angle)) * 120)))))
while run:
    bullet2 = PVOBULLET((SCREEN_WIDTH / 2 + (sin(radians(angle)) * 120)), (SCREEN_HEIGHT - (100 + (cos((radians(angle)) * 120)))), 3, 3)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d] and angle <= 75:
            angle += 5
    elif keys[pygame.K_a] and angle >= -75:
            angle -= 5

    rotated_image, rect = rotate(player_img, angle, pivot, offset)
    screen.fill(BG_COLOR)
    bulet1.move()
    bulet1.spawn()
    bullet2.spawn()
    screen.blit(rotated_image, rect)
    pygame.draw.rect(screen, PADDLE_COLOR, field)
    pygame.draw.rect(screen, STAND_COLOR, stand)
  
    if bulet1.y >= 800:
        bulet1.x = random.randint(100, 1500)
        bulet1.y = random.randint(50, 500)
        bulet1.speedx = random.randint(-3, 3)
        bulet1.speedy = random.randint(0, 3)
        continue
    clock.tick(60)
    print(cos((radians(angle)) * 120))
    pygame.display.flip()