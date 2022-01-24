from ast import parse
import math
import pygame
from pygame.locals import (
    K_LEFT,
    K_RIGHT,
    KEYDOWN,
    KEYUP,
    K_a,
    K_d
)

pygame.init()

X = 600
Y = 500

fps = 60
clock = pygame.time.Clock()

screen = pygame.display.set_mode([600, 500])

pygame.display.set_caption('test')

point = 0
font = pygame.font.Font('freesansbold.ttf', 20)


kPosX = 200
kPosY = 300


kSpeed = 2

sPosX = 250
sPosY = 400

sRetHoejre = False
sRetVenstre = False

srv = False
srh = False
spx = 250
spy = 350
ss = 2.5

sSpeed = 2.5

retHoejre = True
retNed = True


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_a:
                srv = True
            if event.key == K_d:
                srh = True
            if event.key == K_LEFT:
                sRetVenstre = True
            if event.key == K_RIGHT:
                sRetHoejre = True
        if event.type == KEYUP:
            if event.key == K_a:
                srv = False
            if event.key == K_d:
                srh = False
            if event.key == K_LEFT:
                sRetVenstre = False
            if event.key == K_RIGHT:
                sRetHoejre = False



  
                                
                
    if sRetHoejre == True:
        sPosX = sPosX + sSpeed
    if sRetVenstre == True:
        sPosX = sPosX - sSpeed
    if srh == True:
        spx = spx + ss
    if srv == True:
        spx = spx - ss

    screen.fill((255, 255, 255))

    roed = pygame.draw.rect(screen, (255,0,0), (50,50,2,400))
    groen = pygame.draw.rect(screen, (0,255, 0), (50,50,500,2))
    blaa = pygame.draw.rect(screen, (0,0,255), (550,50,2,400))
    sort = pygame.draw.rect(screen, (0,0,0),  (50,450,500,2))
    kasse = pygame.draw.rect(screen, (50,50,50), (kPosX,kPosY,30,30))

    chikane1 = pygame.draw.rect(screen, (100,200,0), (150,245,300,2))
    chikane2 = pygame.draw.rect(screen, (100,0,200), (149,247,2,8))
    chikane3 = pygame.draw.rect(screen, (200,0,0), (150,255,300,2))
    chikane4 = pygame.draw.rect(screen, (0,200,200), (449,247,2,8))

    slider = pygame.draw.rect(screen, (50,50,50), (sPosX,sPosY,100,5))
    slider2 = pygame.draw.rect(screen, (50,50,50), (spx, spy, 100, 5))


    rPoint = math.floor(point / 3)
    pointS = str(rPoint)
    text = font.render(pointS, True, (0,255,0))
    screen.blit(text, (250, 20))


    if slider.colliderect(roed):
        sRetVenstre = False
    if slider.colliderect(blaa):
        sRetHoejre = False
    if slider2.colliderect(roed):
        srv = False
    if slider2.colliderect(blaa):
        srh = False

    if(retHoejre):
        kPosX = kPosX + kSpeed
    else:
        kPosX = kPosX - kSpeed

    if(retNed):
        kPosY = kPosY + kSpeed
    else:
        kPosY = kPosY - kSpeed

    if(kasse.colliderect(roed)):
        retHoejre = True
    
    if(kasse.colliderect(groen)):
        retNed = True

    if(kasse.colliderect(blaa)):
        retHoejre = False

    if(kasse.colliderect(sort)):
        running = False


    if(kasse.colliderect(chikane1)):
        retNed = False
    if(kasse.colliderect(chikane2)):
        retHoejre = False
    if(kasse.colliderect(chikane3)):
        retNed = True
    if(kasse.colliderect(chikane4)):
        retHoejre = True


    

    if(kasse.colliderect(slider)):
        point = point + 1
        retNed = False
    if(kasse.colliderect(slider2)):
        point = point + 1
        retNed = False
        
        
   
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()