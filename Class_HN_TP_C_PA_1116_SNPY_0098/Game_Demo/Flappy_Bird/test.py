import pygame , sys, random

pygame.init()

WITH, HEIGHT = 600,700
clock = pygame.time.Clock()

gravity = 0.05

FPS = 225
screen = pygame.display.set_mode((WITH, HEIGHT))

bg_surface = pygame.transform.scale(pygame.image.load('img/background-day.png').convert(),(WITH, HEIGHT))
floor_surface = pygame.image.load('img/base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0

bird_surface = pygame.image.load("img/bluebird-midflap.png").convert()
bird_surface = pygame.transform.scale2x(bird_surface)
bird_rect = bird_surface.get_rect(center = (150,200))
bird_movement = 0

pipe_surface = pygame.image.load("img/pipe-green.png").convert()
pipe_list = []
XuatHien = pygame.USEREVENT
pipe_surface = pygame.transform.scale2x(pipe_surface)
pygame.time.set_timer(XuatHien,1800)

def creat_newpipe():

    pipe_height = [400, 450, 350]
    random_height = random.choice(pipe_height)
    bottom_pipe = bird_surface.get_rect(midtop = (600,random_height))
    top_pipe = bird_surface.get_rect(midbottom = (600, random_height - 200))
    return bottom_pipe, top_pipe
    # return bottom_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 1
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        print(pipe.bottom)
        if pipe.bottom <= 350:
            screen.blit(pipe_surface, pipe)
        # else:
        #     pipe_flip = pygame.transform.flip(pipe_surface,False,True)
        #     screen.blit(pipe_flip,pipe)

def draw_floor():
    screen.blit(floor_surface, (floor_x_pos, HEIGHT - 100))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.Quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 5
            # if event.key == pygame.K_SPACE and game_active == False:
            #     game_active = True
            #     pipe_list.clear()
            #     bird_rect = bird_surface.get_rect(center=(110,200))
            #     bird_movement = 0
        if event.type == XuatHien:
            pipe_list.extend(creat_newpipe())
            # print(pipe_list)

    screen.blit(bg_surface,(0,0))

    bird_movement += gravity
    bird_rect.centery += bird_movement
    screen.blit(bird_surface,bird_rect)

    pipe_list = move_pipes(pipe_list)
    draw_pipes(pipe_list)

    # if game_active:
    #     game_active = check_collistion(pipe_list)

    bird_movement += gravity

    bird_rect.centery += bird_movement

    # draw_bird()

    pipe_list = move_pipes(pipe_list)
    draw_pipes(pipe_list)


    floor_x_pos -= 1

    draw_floor()

    if(floor_x_pos < -70):
        floor_x_pos = 0

    pygame.display.update()
    clock.tick(FPS)

