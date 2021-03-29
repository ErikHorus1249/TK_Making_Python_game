# import module
import pygame 

# using method init()
pygame.init()

# using set_mode to set Width and Height for the screen
# 3:4
window = pygame.display.set_mode((600,300))

# load anh trong game
gamepad_icon = pygame.image.load("icon.png")
# load background
bg = pygame.image.load("bg.jpg")
bg = pygame.transform.scale(bg,(600,300))

pygame.display.set_icon(gamepad_icon)
pygame.display.set_caption("Game for idiots")

# bien trang thai cua game game status
active = True


window.blit(bg,(0,0))
# event : su kien nhan vat di chuyen - thao tac  
while active :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
    pygame.display.update() 