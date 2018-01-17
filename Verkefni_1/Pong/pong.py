# coding=UTF-8
import pygame

pygame.init()
window_size = window_width, window_height = 640, 480
window = pygame.display.set_mode(window_size)

pygame.display.set_caption('PONG')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

image=pygame.image.load("man.png")

x_position = 580
y_position = 230
x_position2=20
y_position2=230

x_bolti=320
y_bolti=0

x_bolti_velocity=4
y_bolti_velocity=2
y_velocity2=0
y_velocity = 0
window.fill(BLACK)

clock = pygame.time.Clock()

running = True
player1_stig=0
player2_stig=0

#texti
pygame.font.init()
myfont = pygame.font.SysFont('Algerian', 40)
while running:
    #player movement
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_velocity = -8
                if player1_stig-5>=player2_stig:
                    y_velocity=-10
            elif event.key == pygame.K_DOWN:
                y_velocity = 8
                if player1_stig-5>=player2_stig:
                    y_velocity=10
            elif event.key == pygame.K_w:
                y_velocity2 = -8
                if player2_stig-5>=player1_stig:
                    y_velocity2=-10
            elif event.key == pygame.K_s:
                y_velocity2 = 8
                if player2_stig-5>=player1_stig:
                    y_velocity2=10
        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_UP:
                y_velocity=0
            elif event.key == pygame.K_DOWN:
                y_velocity = 0
            elif event.key==pygame.K_w:
                y_velocity2 = 0
            elif event.key == pygame.K_s:
                y_velocity2 = 0

    y_position += y_velocity
    y_position2 += y_velocity2
    x_bolti+=x_bolti_velocity
    y_bolti+=y_bolti_velocity

    window.fill(BLACK)
    #Hlutir
    player1=pygame.draw.rect(window, RED, pygame.Rect(x_position, y_position, 20, 100))
    player2=pygame.draw.rect(window, GREEN, pygame.Rect(x_position2, y_position2, 20, 100))
    window.blit(image,(x_bolti,y_bolti))
    textsurface = myfont.render(str(player1_stig) , True, WHITE)
    textsurface2 = myfont.render(str(player2_stig), True, WHITE)
    textsurface3=myfont.render("|", True, WHITE)
    window.blit(textsurface, (300, 0))
    window.blit(textsurface2, (340, 0))
    window.blit(textsurface3, (320, 0))

    if y_position > 380:
        y_position = 380
    elif y_position < 0:
        y_position=0
    if y_position2 > 380:
        y_position2 = 380
    elif y_position2 < 0:
        y_position2=0

    if y_bolti >460 or y_bolti<0:
        y_bolti_velocity*=-1
        y_bolti_velocity *= 1.1
    elif x_bolti > 640 :
        x_bolti=320
        x_bolti_velocity = -4
        y_bolti_velocity = -2
        player1_stig+=1
    elif x_bolti < 0:
        x_bolti = 320
        x_bolti_velocity = 4
        y_bolti_velocity = 2
        player2_stig += 1
    if y_bolti>y_position and y_bolti<y_position+100 and x_bolti<x_position and x_bolti>x_position-20:
        x_bolti_velocity*=-1.2
    elif y_bolti>y_position2 and y_bolti<y_position2+100 and x_bolti>x_position2 and x_bolti<x_position2+20:
        x_bolti_velocity*=-1
    pygame.display.update()
    clock.tick(60)
pygame.quit()
