"""
ctfv2

Description:
"""
# import libraries
import pygame
# import tsk

pygame.init()

# create the window
w = pygame.display.set_mode([500, 500])

# create the variables
run = True
# bgm = pygame.mixer.Sound("electronic_calm.mp3")
p1score = 0
p2score = 0
p1flag_alive = True
p2flag_alive = True
ls = pygame.Rect(0, 0, 500, 500)
rs = pygame.Rect(250, 0, 500, 500)
p1 = pygame.Rect(70, 240, 20, 20)
p2 = pygame.Rect(410, 240, 20, 20)

p1flag = pygame.Rect(20, 240, 15, 15)
p2flag = pygame.Rect(460, 240, 15, 15)


# functions
def draw_p1_flag(p1flag_present):
    global p1flag
    if p1flag_present == True:
        pygame.draw.ellipse(w, (255, 255, 0), p1flag)


def draw_p2_flag(p2flag_present):
    global p2flag
    if p2flag_present == True:
        pygame.draw.ellipse(w, (0, 255, 0), p2flag)


def whole_restart():
    global p1flag_alive
    global p2flag_alive
    global p1
    global p2
    p1.x = 70
    p1.y = 240
    p2.x = 410
    p2.y = 240
    p1flag_alive = True
    p2flag_alive = True


# Total number of games?
tnog = int(input("How many total games do you want? "))

# Game loop
while run:
    # # Set the refresh rate for the players
    # p1.image_animation_rate = 244
    # p2.image_animation_rate = 244

    # Fill the background
    w.fill((255, 255, 255))

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    # Draw the components

    pygame.draw.rect(w, (255, 0, 0), ls)
    pygame.draw.rect(w, (0, 0, 255), rs)
    pygame.draw.rect(w, (0, 0, 0), p1)
    pygame.draw.rect(w, (0, 0, 0), p2)
    draw_p1_flag(p1flag_alive)
    draw_p2_flag(p2flag_alive)

    p1flag_alive == False

    # Move the players
    if keys[pygame.K_UP]:
        p2.y -= 1
    if keys[pygame.K_DOWN]:
        p2.y += 1
    if keys[pygame.K_LEFT]:
        p2.x -= 1
    if keys[pygame.K_RIGHT]:
        p2.x += 1

    if keys[pygame.K_w]:
        p1.y -= 1
    if keys[pygame.K_s]:
        p1.y += 1
    if keys[pygame.K_a]:
        p1.x -= 1
    if keys[pygame.K_d]:
        p1.x += 1

    # Arena border
    if p1.x < 0:
        p1.x = 0
    if p1.x > 480:
        p1.x = 480
    if p1.y < 0:
        p1.y = 0
    if p1.y > 480:
        p1.y = 480

    if p2.x < 0:
        p2.x = 0
    if p2.x > 480:
        p2.x = 480
    if p2.y < 0:
        p2.y = 0
    if p2.y > 480:
        p2.y = 480

    # Collision with flags
    if p1.colliderect(p2flag):
        p2flag_alive = False

    if p2.colliderect(p1flag):
        p1flag_alive = False

    # Collisions within players

    if p1.colliderect(ls):
        if p1.colliderect(p2):
            p2.x = 410
            p2.y = 240
            if p1flag_alive == False:
                p1flag_alive = True
    if p2.colliderect(rs):
        if p2.colliderect(p1):
            p1.x = 70
            p1.y = 240
            if p2flag_alive == False:
                p2flag_alive = True

    # Add scores to either players
    if p2flag_alive == False:
        if p1.x <= 0:
            p1score += 1
            whole_restart()

    if p1flag_alive == False:
        if p2.x >= 480:
            p2score += 1
            whole_restart()

    if p1score == tnog:
        print("Player 1 is the winner")
        run = False
    if p2score == tnog:
        print("Player 2 is the winner")
        run = False

    pygame.display.flip()