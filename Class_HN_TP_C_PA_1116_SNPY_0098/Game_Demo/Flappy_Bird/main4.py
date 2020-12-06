import pygame, sys, random

# khoi tao pygame
pygame.init()

# thong so cho khung canvas
WIDTH, HEIGHT = 400, 600
clock = pygame.time.Clock()
gravity = 0.25
# Trang thai cua game
game_active = False

# bien FPS
FPS = 120

# hien thi khung canvas
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# anh cho background
bg_surface = pygame.transform.scale(pygame.image.load('img/background-day.png').convert(), (WIDTH, HEIGHT))

# anh cho phan nen
floor_surface = pygame.image.load('img/base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0

# con chim
# Tao ba hinh anh trang thai cho chim khi bay
bird_downflap = pygame.image.load('img/bluebird-downflap.png').convert_alpha()
bird_midflap = pygame.image.load('img/bluebird-midflap.png').convert_alpha()
bird_upflap = pygame.image.load('img/bluebird-upflap.png').convert_alpha()
bird_frames = [bird_downflap, bird_midflap, bird_upflap]
# chi so de xac dinh hinh dang chim
bird_index = 1
# tao dien mao cua chim dua tren viec chon trang thai khi bay
bird_surface = bird_frames[bird_index]
bird_rect = bird_surface.get_rect(center=(110, 200))
bird_movement = 0
# Tao mot su kien chim vo canh va dat thoi gian cho lan xuat hien (set_timer)
VoCanh = pygame.USEREVENT + 1
pygame.time.set_timer(VoCanh,100)


# Ong
pipe_surface = pygame.image.load('img/pipe-green.png').convert()
# pipe_surface = pygame.transform.scale2x(pipe_serface)
pipe_list = []
XuatHien = pygame.USEREVENT
pygame.time.set_timer(XuatHien, 1200)

# Ham tao ong nuoc moi
def creat_newpipe():
    pipe_height = [300, 200, 320]
    random_height = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop=(400, random_height))
    # print(random_height, bottom_pipe.bottom)
    top_pipe = pipe_surface.get_rect(midbottom=(400, random_height - 150))
    return bottom_pipe, top_pipe
    # return  bottom_pipe

# Ham dich chuyen vi tri ong nuoc
def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 1
    return pipes

# Ham dung ve ra ong
def draw_pipes(pipes):
    for pipe in pipes:
        # print(pipe.bottom)
        if pipe.bottom > 400:
            screen.blit(pipe_surface, pipe)
        else:
            pipe_flip = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(pipe_flip, pipe)


# kiem tra va cham
def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return False

    if bird_rect.top <= 0 or bird_rect.bottom >= 500:
        return False

    return True

# Ham xoay con chim
def rotate_bird(bird):
    new_bird = pygame.transform.rotozoom(bird, -bird_movement*6,1)
    return  new_bird
# Ham chuyen dong canh cua chim
def bird_animation():
    new_bird = bird_frames[bird_index]
    new_bird_rect = new_bird.get_rect(center=(110,bird_rect.centery))
    return  new_bird, new_bird_rect

# chuyen dong nen dat
def draw_floor():
    screen.blit(floor_surface, (floor_x_pos, HEIGHT - 100))
    screen.blit(floor_surface, (floor_x_pos + 300, HEIGHT - 100))

def draw_bird():
    screen.blit(rotated_bird, bird_rect)

# Vong lap chinh cua game
while True:
    # thiet lap thoat game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active == True:
                bird_movement = 0
                bird_movement -= 5
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                pipe_list.clear()
                # Dat lai vi tri va toc do roi cho con chim
                # bird_rect = bird_surface.get_rect(center=(110, 200))
                # bird_movement = 0

        # Su kien ong xuat hien
        if event.type == XuatHien:
            pipe_list.extend(creat_newpipe())
            # print(pipe_list)
        # Su kien vo canh cua chim
        if event.type == VoCanh:
            # Neu so thu tu canh van nho hon 2 tiep tuc tang stt
            if(bird_index < 2):
                bird_index += 1
            # Neu so thu tu bang 2 thi reset lai hinh 0
            else: bird_index = 0
            # Tra ve hinh dang cua chim bang ham animation()
            bird_surface, bird_rect = bird_animation()

    # Hien thi hinh nen (back ground)
    screen.blit(bg_surface, (0, 0))
    # Kiem tra trang thai cua game_active de hien thi cac thanh phan cua game nhu ong va con chim
    if game_active:

        # Xac dinh gia tri cua game_active dua theo kiem tra va cham
        game_active = check_collision(pipe_list)

        # Van toc cua chim duoc cong lien tiep voi trong luc
        bird_movement += gravity

        # quay hinh con chim su dung ham rotozoom()
        rotated_bird = rotate_bird(bird_surface)

        # Thay doi gia tri y cua con chim
        bird_rect.centery += bird_movement

        # Hien thi hinh anh cua con chim
        draw_bird()

        # ong
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)

    # hieu ung chuyen dong nen
    floor_x_pos -= 1
    draw_floor()
    # neu nhu thanh nen chay het ra ngoai canvas thi reset lai vi tri
    if (floor_x_pos < -500):
        floor_x_pos = 0

    # update
    pygame.display.update()
    # FPS
    clock.tick(FPS)