import pygame

pygame.init()

screen = pygame.display.set_mode([500, 500])

kPosX = 200
kPosY = 300
sliderPosX = 300

kSpeed = 0.05

retHoejre = True
retNed = True

sliderRetHoejre = False
sliderRetVenstre = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                sliderRetHoejre = True
            if event.key == pygame.K_LEFT:
                sliderRetVenstre = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                sliderRetHoejre = False
            if event.key == pygame.K_LEFT:
                sliderRetVenstre = False


    screen.fill((255, 255, 255))

    roed = pygame.draw.rect(screen, (255,0,0), (50,50,2,400))
    groen = pygame.draw.rect(screen, (0,255, 0), (50,50,400,2))
    blaa = pygame.draw.rect(screen, (0,0,255), (450,50,2,400))
    sort = pygame.draw.rect(screen, (0,0,0),  (50,450,400,2))
    kasse = pygame.draw.rect(screen, (50,50,50), (kPosX,kPosY,30,30))

    chikaneovre = pygame.draw.rect(screen, (255,0,0),  (152,245,196,2))
    chikanenedre = pygame.draw.rect(screen, (255,0,0),  (152,255,196,2))
    chikanehoejre = pygame.draw.rect(screen, (0,255,0),  (349,246,2,10))
    chikanevenstre = pygame.draw.rect(screen, (0,255,0),  (150,246,2,10))

    slider = pygame.draw.rect(screen, (0,0,0),(sliderPosX,430,100,5))

    if(sliderRetHoejre):
        sliderPosX = sliderPosX + 0.1

    if(sliderRetVenstre):
        sliderPosX = sliderPosX - 0.1

    if(kasse.colliderect(slider)):
        retNed = False

    if(kasse.colliderect(chikaneovre)):
        retNed = False
    
    if(kasse.colliderect(chikanenedre)):
        retNed = True
    
    if(kasse.colliderect(chikanehoejre)):
        retHoejre = True
    
    if(kasse.colliderect(chikanevenstre)):
        retHoejre = False


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
        kSpeed = 0


    pygame.display.flip()

pygame.quit()