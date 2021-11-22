import pygame

pygame.init()

screen = pygame.display.set_mode([500, 500])

kPosX = 200
kPosY = 300

kSpeed = 0.05

retHoejre = True
retNed = True

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    roed = pygame.draw.rect(screen, (255,0,0), (50,50,2,400))
    groen = pygame.draw.rect(screen, (0,255, 0), (50,50,400,2))
    blaa = pygame.draw.rect(screen, (0,0,255), (450,50,2,400))
    sort = pygame.draw.rect(screen, (0,0,0),  (50,450,400,2))
    kasse = pygame.draw.rect(screen, (50,50,50), (kPosX,kPosY,30,30))

    chikane1 = pygame.draw.rect(screen, (100,0,0),  (150,245,200,10))

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
        retNed = False


    pygame.display.flip()

pygame.quit()