import pygame as pg
import random2 as r2

pg.init()

screen = pg.display.set_mode((750, 400))

x_dino = 50
y_dino = 255
width_dino = 70
height_dino = 75
dino = [pg.image.load('dino_1.png'), pg.image.load('dino_2.png'), pg.image.load('dino_1.png'), pg.image.load(
    'dino_2.png'), pg.image.load('dino_1.png'), pg.image.load('dino_2.png'), pg.image.load('dino_1.png'), pg.image.load('dino_2.png')]
dino_lay = [pg.image.load('dino_lay1.png'), pg.image.load('dino_lay2.png'), pg.image.load('dino_lay1.png'), pg.image.load(
    'dino_lay2.png'), pg.image.load('dino_lay1.png'), pg.image.load('dino_lay2.png'), pg.image.load('dino_lay1.png'), pg.image.load('dino_lay2.png')]

width_cactus = [45, 35, 70, 105]
height_cactus = [77, 50, 50, 50]
kind_of_cactus = [r2.randint(0, 3), r2.randint(
    0, 3), r2.randint(0, 3), r2.randint(0, 3)]
x_cactus = [1500, 0, 0, 0]
for i in range(0, 4):
    if i != 0:
        x_cactus[i] = x_cactus[i - 1] + r2.randint(200, 700)
    x_cactus[0] = 1500
    print(x_cactus[i])
y_cactus = [0, 0, 0, 0]

jump = False
jumping = -10
lay = False

score = 0
yes = 0
hight_score = 0

font = pg.font.SysFont('comicsansms', 27)
pg.font.Font('C:\WINDOWS\Fonts\comic.ttf', 30)
text1 = font.render('HI', 1, (0, 0, 0))

AnimCount = 0

cactus = [pg.image.load('big_cactus.png'), pg.image.load('little_cactus.png'), pg.image.load(
    'double_little_cactus.png'), pg.image.load('trible_little_cactus.png')]
jump_sound = pg.mixer.Sound('Jump.wav')
die_sound = pg.mixer.Sound('die.wav')

clock = pg.time.Clock()

pg.display.set_caption('Dino')

bg = [pg.image.load('background_1.jpg'), pg.image.load('background_2.jpg')]


def spawn_cactus():
    for i in range(0, 4):

        if kind_of_cactus[i] == 0:
            height_cactus[i] == 77
            y_cactus[i] = 248
            width_cactus[i] = 45
        elif kind_of_cactus[i] == 1:
            height_cactus[i] = 50
            y_cactus[i] = 275
            width_cactus[i] = 35
        elif kind_of_cactus[i] == 2:
            height_cactus[i] = 50
            y_cactus[i] = 275
            width_cactus[i] = 70
        else:
            height_cactus[i] = 50
            y_cactus[i] = 275
            width_cactus[i] = 70
spawn_cactus()

def DrawWindow():
    global AnimCount

    if AnimCount + 1 >= 30:
        AnimCount = 0
    screen.blit(bg[AnimCount // 15], (0, 0))
    AnimCount += 1

    if lay:
        screen.blit(dino_lay[AnimCount // 4], (x_dino, y_dino))
    else:
        screen.blit(dino[AnimCount // 4], (x_dino, y_dino))

    text2 = font.render(str(hight_score), 1, (0, 0, 0))
    text3 = font.render(str(score), 1, (0, 0, 0))

    screen.blit(text1, (550, 5))
    screen.blit(text2, (600, 5))
    screen.blit(text3, (675, 5))

    for i in range(0, 4):
        screen.blit(cactus[kind_of_cactus[i]], (x_cactus[i], y_cactus[i]))

speed = 13
run = True
while run:
    clock.tick(30)
    DrawWindow()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    keys = pg.key.get_pressed()

    if keys[pg.K_DOWN]:
        lay = True
    if lay:
        jump = False
        jumping = -10
        y_dino = 290
        width_dino = 87
        height_dino = 38
        lay = False

    else:
        if width_dino != 70:
            width_dino = 70
            height_dino = 75
            y_dino = 255
            lay = False
    if keys[pg.K_SPACE] or keys[pg.K_UP]:
        if not(jump):
            jump = True
            print('jump')
            jump_sound.play()
    if jump:
        if jumping < 0:
            y_dino -= (jumping**2) / 2
        elif jumping >= 0 and jumping <= 10:
            y_dino += (jumping**2) / 2
        else:
            jumping = -11
            jump = False
        jumping += 1

    if keys[pg.K_ESCAPE]:
        run = False

    for i in range(0, 4):
        x_cactus[i] -= speed
        if ((x_dino + width_dino >= x_cactus[i] and x_dino + width_dino <= x_cactus[i] + width_cactus[i]) or (x_dino >= x_cactus[i] and x_dino <= x_cactus[i] + width_cactus[i])) and (y_dino + height_dino >= y_cactus[i]):
            print('die')
            x_cactus = [0, 0, 0, 0]
            for j in range(0, 4):
                x_cactus[0] = 1500
                if j != 0:
                    x_cactus[i] = x_cactus[i - 1] + r2.randint(200, 700)
            kind_of_cactus = [r2.randint(0, 3), r2.randint(0, 3), r2.randint(0, 3), r2.randint(0, 3)]
            spawn_cactus()
            die_sound.play()
       
            if score > hight_score:
                hight_score = score
            score = 0
            speed = 13

        if x_cactus[i] + width_cactus[i] <= 0:
            x_cactus.pop(0)
            x_cactus.append(x_cactus[2] + r2.randint(200, 700))
            kind_of_cactus.pop(0)
            kind_of_cactus.append(r2.randint(0, 3))
            width_cactus.pop(0)
            height_cactus.pop(0)
            y_cactus.pop(0)

            if kind_of_cactus[3] == 0:
                height_cactus.append(77)
                y_cactus.append(248)
                width_cactus.append(45)
            elif kind_of_cactus[3] == 1:
	            height_cactus.append(50)
	            y_cactus.append(275)
	            width_cactus.append(35)
            elif kind_of_cactus[3] == 2:
	            height_cactus.append(50)
	            y_cactus.append(275)
	            width_cactus.append(70)
            else:
                height_cactus.append(50)
                y_cactus.append(275)
                width_cactus.append(105)

    speed += 0.0075
    if yes % 3 == 0:
        score += 1
    yes += 1
    pg.display.update()

pg.quit()
