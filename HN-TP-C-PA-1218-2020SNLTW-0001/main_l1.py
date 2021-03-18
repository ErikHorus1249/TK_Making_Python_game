# import module
import pygame 


pygame.init()


window = pygame.display.set_mode((600,300))

window.fill((182,249,230))

pygame.display.set_caption("the first lesson")

icon = pygame.image.load("./img/icon.png")
bg = pygame.image.load("./img/bg.jpg")
menu = pygame.image.load("./img/menu.png")
menu = pygame.transform.scale(menu,(200,150))


window.blit(bg,(0,0))
window.blit(menu,(200,90))
pygame.display.set_icon(icon)

active = True


while active :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
    pygame.display.update() 