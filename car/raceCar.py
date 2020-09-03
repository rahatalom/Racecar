import pygame
import time
import random
pygame.init()
crash_sound = pygame.mixer.Sound("Crash.wav")
display_width = 700
display_height = 550
win = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Race_Car")
car_img = pygame.image.load("car.png")
car_img_width = 67
car_img_height = 69
black = (0, 0, 0)
clock = pygame.time.Clock()


def blockz_Dodged(count):
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render('Dodged: {}'.format(Dodged), True, black)

    win.blit(text, (0, 0))
    pygame.display.update()


def crashedz():
    pygame.mixer.Sound.play(crash_sound)
    pygame.mixer.music.stop()
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('You Crashed!', True, (0, 255, 55))
    textRect = text.get_rect()
    textRect.center = ((display_width - 10) // 2, (display_height - 10) // 2)

    win.blit(text, textRect)
    pygame.display.update()


Dodged = 0


def blockZ(blockX, blockY, block_height, block_width, color):
    pygame.draw.rect(win, color, (blockX, blockY, block_width, block_height))


blockX = random.randrange(50, 550)
blockY = -100
block_height = 50
block_width = 50
color = (23, 53, 179)
block_velocity = 20


def heroz(q, z):
    win.blit(car_img, (q, z))


x = 550
y = 300

vel = 40


run = True
while run:

    pygame.mixer.music.load('C.wav')
    pygame.mixer.music.play()
    pygame.time.delay(10)

    win.fill((255, 255, 255))
    blockz_Dodged(Dodged)
    heroz(x, y)
    blockZ(blockX, blockY, block_height, block_width, black)
    blockY += block_velocity
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        car_img = pygame.image.load("car.png")
        win.blit(car_img, (x, y))
        block_velocity = 30

        x -= vel

    if keys[pygame.K_RIGHT]:
        car_img = pygame.image.load("car.png")
        win.blit(car_img, (x, y))
        block_velocity = 30

        x += vel

    if keys[pygame.K_UP]:
        car_img = pygame.image.load("carnorse.png")
        win.blit(car_img, (x, y))
        vel = 50
        block_velocity = 60

        y -= vel

    if keys[pygame.K_DOWN]:
        car_img = pygame.image.load("car.png")
        win.blit(car_img, (x, y))
        vel = 30
        block_velocity = 30

        y += vel
    if x > (display_width - car_img_width) or x < 0 or y > (display_height - car_img_height):
        crashedz()
        run = False

    if blockY > display_height:
        Dodged += 1
        block_height += 2
        block_width += 2

        blockX = random.randrange(50, 550)
        blockY = -30

    if y < (blockY + block_height) and y + car_img_height > blockY:
        if x > blockX and x < (blockX + block_width) or x + car_img_width > blockX and x + car_img_width < (blockX + block_width):
            crashedz()
            time.sleep(2)
            run = False
    clock.tick(10)


pygame.quit()
