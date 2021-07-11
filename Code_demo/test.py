import pygame 

# khoi tao 
pygame.init ()

width, height = 400, 300

# tao khug tro choi 
window = pygame.display.set_mode((width,height))

bg = pygame.image.load("img/bg.jpg")
bg = pygame.transform.scale(bg, (width, height))


# nhan vat 
nv = pygame.transform.scale(pygame.image.load("img/nv.png"), (100,100))
while True:
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            pygame.quit()

    window.blit(bg,(0,0))
    window.blit(nv,(200,180))
    pygame.display.update()



