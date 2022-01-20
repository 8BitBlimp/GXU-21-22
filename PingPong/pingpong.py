from ast import parse
import pygame
from pygame.locals import (
    K_LEFT,
    K_RIGHT,
    KEYDOWN,
    KEYUP
)

pygame.init()

X = 600
Y = 500

screen = pygame.display.set_mode([600, 500])

#font = pygame.font.Font('freesansbold.ttf', 20)
#text = font.render(pointS, True, (0,255,0), (0,0,128))
textRect = text.get_rect()

kPosX = 200
kPosY = 300

kSpeed = 0.10

sPosX = 250
sPosY = 400

sRetHoejre = False
sRetVenstre = False

sSpeed = 0.20

retHoejre = True
retNed = True

point = 0



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                sRetVenstre = True
            if event.key == K_RIGHT:
                sRetHoejre = True
        if event.type == KEYUP:
            if event.key == K_LEFT:
                sRetVenstre = False
            if event.key == K_RIGHT:
                sRetHoejre = False



    #pointS = str((point))

    
    #textRect.center = (X // 2, Y // 2 )

    #screen.blit(text, textRect)

    
                                
                
    if sRetHoejre == True:
        sPosX = sPosX + sSpeed
    if sRetVenstre == True:
        sPosX = sPosX - sSpeed
    

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

   
    if slider.colliderect(roed):
        sRetVenstre = False
    if slider.colliderect(blaa):
        sRetHoejre = False

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
        pygame.quit()


    if(kasse.colliderect(chikane1)):
        retNed = False
    if(kasse.colliderect(chikane2)):
        retHoejre = False
    if(kasse.colliderect(chikane3)):
        retNed = True
    if(kasse.colliderect(chikane4)):
        retHoejre = True


    

    if(kasse.colliderect(slider)):
        retNed = False
        point = point + 1
   
    pygame.display.flip()

pygame.quit()