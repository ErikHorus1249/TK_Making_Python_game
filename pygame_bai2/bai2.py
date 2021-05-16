import pygame

# khoi tao 
pygame.init()

# chieu dai va chieu rong 
Width, Height = 800, 400

# tao khung tro choi - comment
window = pygame.display.set_mode((Width,Height))

# image loading 
background = pygame.image.load("./img/bg.jpg")
# transform -> scale() , scale2x
background = pygame.transform.scale(background, (Width,Height))

# character image loading
# character = pygame.image.load("./img/chac.png")
# character = pygame.transform.scale(character, (100,70))
left = pygame.transform.scale(pygame.image.load("./img/left.png"),(100,70))
right = pygame.transform.scale(pygame.image.load("./img/right.png"),(100,70))

di_chuyen = 0
x_character = 400
y_character = 300
window.blit(left, (x_character, y_character))
character = left
# event : sự kiện : -quit , keyup , keydown 
while True:
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            pygame.quit()
        # chuyen dong 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                di_chuyen = -1
                character = left
                print("left")
            if event.key == pygame.K_d:
                di_chuyen = 1
                character = right
                print("right")

        if event.type == pygame.KEYUP:
            di_chuyen = 0
        
    window.blit(background, (0,0))

    # x_character = x_character + di_chuyen
    x_character += di_chuyen

    if x_character <= 0 :
        x_character = 0
    if x_character >= Width-70:
        x_character = Width-70

    # cap nhat toa do moi neu si chuyen 
    window.blit(character,(x_character, y_character))
    # hien thi  nhan vat 
    
    # update status 
    pygame.display.update()


# infinty loop 
# nhan vat tai thoi diem hien tai : 5 
# sau bam D -> sang phai -> thay doi toa do -> cap nhat toa do 
# circle
# khoi tao -> vong lap -> update

# them anh 
# nhan vat : 
# tao hinh 
# chuyen dong(game play) AWDS 

