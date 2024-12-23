import pygame
from pygame.locals import *
import sys
import random
import asyncio

pygame.init()

FPS = pygame.time.Clock()

white = pygame.Color(255,255,255)
black = pygame.Color(0,0,0)
gray = pygame.Color(128,128,128)
red = pygame.Color(255,0,0)
green = pygame.Color(0,255,0)
blue = pygame.Color(0,0,255)



font = pygame.font.SysFont(None, 36)


DISPLAYSURF = pygame.display.set_mode((1000,700))
DISPLAYSURF.fill(white)
pygame.display.set_caption("Dodge the red")


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        self.radius = 15
        self.x = random.randint(30, 970)
        self.y = 0

    def move(self):
        self.y += random.randint(-2,7)
        self.x += random.randint(-7, 7)
        if self.y - 15 > 700:
            self.y = 0
            self.x = random.randint(30, 970)
            return True
        return False
        pygame.time.delay(10)
    
    def draw(self, surface):
        pygame.draw.circle(surface, red, (self.x, self.y), self.radius)

class You(pygame.sprite.Sprite):
    def __init__(self):
        self.radius = 20
        self.x = 500
        self.y = 500
    def draw(self, surface):
        pygame.draw.circle(surface, black, (self.x, self.y), self.radius)
    
    def moveRight(self, pixels):
        self.x += pixels
    def moveLeft(self, pixels):
        self.x -= pixels
    def moveUp(self, pixels):
        self.y -= pixels
    def moveDown(self, pixels):
        self.y += pixels


enemies = [Enemy()]
P1 = You()
speed = 2


async def main():
    FPS = pygame.time.Clock()

    white = pygame.Color(255,255,255)
    black = pygame.Color(0,0,0)
    gray = pygame.Color(128,128,128)
    red = pygame.Color(255,0,0)
    green = pygame.Color(0,255,0)
    blue = pygame.Color(0,0,255)
    score = 0
    run = True
    font = pygame.font.SysFont(None, 36)
    speed = 2
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            P1.moveLeft(speed)
        if keys[pygame.K_RIGHT]:
            P1.moveRight(speed)
        if keys[pygame.K_UP]:
            P1.moveUp(speed)
        if keys[pygame.K_DOWN]:
            P1.moveDown(speed)

        DISPLAYSURF.fill(gray)
        P1.draw(DISPLAYSURF)

        for enemy in enemies[:]:
            if enemy.move():
                enemies.append(Enemy())
                score += 1
            enemy.draw(DISPLAYSURF)


        for enemy in enemies:
            distance = ((P1.x - enemy.x) ** 2 + (P1.y - enemy.y) ** 2) ** 0.5
            if distance < P1.radius + enemy.radius:
                print("Collision Detected!\nGame Over!")
                Game_Over_Text = font.render("GAME OVER!", True, red)
                DISPLAYSURF.blit(Game_Over_Text, (400,350))
                pygame.display.update()
                pygame.time.delay(2000)
                run = False


        score_text = font.render(f"Score: {score}", True, white)
        DISPLAYSURF.blit(score_text, (10,10))


        pygame.display.update()
        FPS.tick(60)
        await asyncio.sleep(0)
asyncio.run(main())
