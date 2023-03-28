import pygame
import random
import math
from pygame import mixer
import time

pygame.init()
running =True
screen=pygame.display.set_mode((800,600))
green=(0,255,0)
gray=(119,118,110)
white=(255,255,255)
red=(255,0,0)
bright_green=(127,255,0)
bright_red=(255,69,0)
bright_blue=(39,64,139)
blue=(0,0,250)
clock=pygame.time.Clock()


bg_image=pygame.image.load("background.jpg")
intro_background=pygame.image.load("introimage.jpg")

home1_image=pygame.image.load("home1.png")
home2_image=pygame.image.load("home2.png")
home3_image=pygame.image.load("home3.png")
home4_image=pygame.image.load("home4.png")
home5_image=pygame.image.load("home5.png")
tree1_image=pygame.image.load("tree1.png")
tree2_image=pygame.image.load("tree2.png")
grass_image=pygame.image.load("grass.png")
cloud_image=pygame.image.load("cloud.png")

pygame.display.set_caption("shooting game")
icon=pygame.image.load("icon.png")
pygame.display.set_icon(icon)
mixer.music.load("BossSong.mp3")
mixer.music.play(-1)
#rocket
rocket_image=pygame.image.load("rocket.png")
rocket_x = 370
rocket_y = 480
rocket_x_change = 0

virus_image = []
virus_x = []
virus_y = []
virus_x_change = []
virus_y_change = []
no_of_enemies = 7



# enemy
for i in range(no_of_enemies):
    virus_image.append(pygame.image.load("cartoon.png"))
    virus_x.append(random.randint(0, 736))
    virus_y.append(random.randint(50, 120))
    virus_x_change.append(2)
    virus_y_change.append(20)




#bullet
bullet_image = pygame.image.load("bullet.png")

#score
score_value = 0
bullet_x = 0
bullet_y = 480
bullet_x_change = 0
bullet_y_change = 50

text_x = 10
text_y = 10

over=pygame.font.Font("freesansbold.ttf",50)
village=pygame.font.Font("freesansbold.ttf",50)
font = pygame.font.Font("freesansbold.ttf", 30)

def show_score(text_x,text_y) :
    score=font.render("Score : " + str(score_value),True ,((0,0,0)))
    screen.blit(score,(text_x,text_y))
def game_over_text():
    over_text=font.render("                             GAME OVER !  ",True ,(0,0,0))
    screen.blit(over_text,(50,250))
def village_font():
    village_text=font.render("      PLAY AGAIN ",True,(0,0,0))
    screen.blit(village_text,(250,300))

def rocket(rocket_x, rocket_y):
        screen.blit(rocket_image, (rocket_x, rocket_y))
def virus(virus_x, virus_y, i):
    screen.blit(virus_image[i], (virus_x, virus_y))
def fire_bullet(bullet_x, bullet_y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_image, (bullet_x + 16, bullet_y + 10))
def iscollision(virus_x, virus_y, bullet_x, bullet_y):
    distance = math.sqrt((math.pow(virus_x - bullet_x, 2)) + (math.pow(virus_y - bullet_y, 2)))
    if distance < 30:
        return True
    else:
        return False
bullet_state = "ready"
running = True

while running:
    screen.fill((0, 0, 0))
    screen.blit(bg_image, (0, 0))
    screen.blit(home1_image, (20, 460))
    screen.blit(home2_image, (200, 460))
    screen.blit(home3_image, (340, 460))
    screen.blit(home4_image, (660, 460))
    screen.blit(home5_image, (480, 460))
    screen.blit(tree1_image, (140, 490))
    screen.blit(tree2_image, (600, 490))
    screen.blit(grass_image, (630, 550))
    screen.blit(grass_image, (600, 550))
    screen.blit(grass_image, (130, 555))
    screen.blit(grass_image, (162, 555))
    screen.blit(cloud_image, (50, 40))
    screen.blit(cloud_image, (340, 20))
    screen.blit(cloud_image, (600, 35))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rocket_x_change = -9  # rocket speed
            if event.key == pygame.K_RIGHT:
                rocket_x_change = 9  # rocket speed
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sound = mixer.Sound("laser.wav.wav")
                    bullet_sound.play()
                    bullet_x = rocket_x
                    fire_bullet(bullet_x, bullet_y)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                rocket_x_change = 0
    rocket_x += rocket_x_change
    if rocket_x <= 0:
        rocket_x = 0
    elif rocket_x >= 736:
        rocket_x = 736
    for i in range(no_of_enemies):
        if virus_y[i] > 400:
            for k in range(no_of_enemies):
                virus_y[k] = 3000
            game_over_text()
            village_font()
            break
        virus_x[i] += virus_x_change[i]
        if virus_x[i] <= 0:
            virus_x_change[i] = 5  # corona speed
            virus_y[i] += virus_y_change[i]
        elif virus_x[i] >= 736:
            virus_x_change[i] = -5  # corona speed
            virus_y[i] += virus_y_change[i]
            # collisions
        collision = iscollision(virus_x[i], virus_y[i], bullet_x, bullet_y)
        if collision:
            explosion_sound = mixer.Sound("explosion.wav")
            explosion_sound.play()
            bullet_y = 480
            bullet_state = "ready"
            score_value -=10
            virus_x[i] = random.randint(0, 736)
            virus_y[i] = random.randint(50, 120)
        virus(virus_x[i], virus_y[i], i)

    # bullet movement
    if bullet_y <= 0:
        bullet_y = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    rocket(rocket_x, rocket_y)
    show_score(text_x, text_y)
    pygame.display.update()




















