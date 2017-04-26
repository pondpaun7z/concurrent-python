import pygame
import random
display_width = 800
display_height = 600
white = (255, 255, 255)
black = (0, 0, 0)
red = (200, 0, 0)
green = (0, 200, 0)
s = 0
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
pygame.init()
gamedisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Fap Fap Fap')
clock = pygame.time.Clock()

main = pygame.image.load('1/indexBG.png')
play = pygame.image.load('1/playButton.png')


joinbg = pygame.image.load('2/joinGameBG.png')
join = pygame.image.load('2/joinRoomButton.png')

playbg = pygame.image.load('3/playBG.png')

ped = pygame.image.load('3/pedpro.png')

img_drink = ['3/player1/drink1.png', '3/player1/drink2.png',
             '3/player1/drink3.png', '3/player1/drink4.png','3/player1/drink5.png']
img_eat = ['3/player1/eat1.png', '3/player1/eat2.png',
           '3/player1/eat3.png', '3/player1/eat4.png']
img_drink2 = ['3/player2/drink1P2.png', '3/player2/drink2P2.png',
             '3/player2/drink3P3.png', '3/player2/drink4P4.png','3/player2/drink5P5.png']
img_eat2 = ['3/player2/eat1P2.png', '3/player2/eat2P2.png',
           '3/player2/eat3P2.png', '3/player2/eat4P2.png']


class player(object):
    """docstring for player"""

    def __init__(self, imgd, imge, x, y):
        super(player, self).__init__()
        self.eat1 = imge
        self.drink1 = imgd
        self.x = x
        self.y = y
        self.all_imge = {}
        self.all_imgd = {}
        self.loadimg()

    def loadimg(self):
        for img in self.eat1:
            self.all_imge[img] = pygame.image.load(img)
        for img in self.drink1:
            self.all_imgd[img] = pygame.image.load(img)

    def eat(self):
        print("ee")
        for img in self.all_imge:
            gamedisplay.blit(self.all_imge[img], (x, y))
        return 5

    def drink(self):
        print("dd")
        for img in self.all_imgd:
            gamedisplay.blit(self.all_imgd[img], (x, y))
        return 3
    # def show(self):
    #     img = self.all_imge[:0]
    #     gamedisplay.blit(self.all_imge[img], (x, y))


def playbutton(x, y, action=None):

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    sizeplay = play.get_rect().size
    # print(click)
    print(sizeplay)
    if x + sizeplay[0] > mouse[0] > x and y + sizeplay[1] > mouse[1] > y:
        # pygame.draw.rect(gamedisplay,ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()
    # pygame.draw.rect(gamedisplay,ic,(x,y,w,h))

    gamedisplay.blit(play, (x, y))


def againbutton(x, y, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    size = play.get_rect().size
    if x + size[0] > mouse[0] > x and y + size[1] > mouse[1] > y:
        if click[0] == 1 and action != None:
            action()
            # print(5)
    gamedisplay.blit(play, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()


def gameStart():
    pass


def gameintro():
    intro = True

    while (intro):
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gamedisplay.blit(main, (0, 0))
        # largeText = pygame.font.Font('Nithan.ttf', 115)
        # TextSurf, TextRect = text_objects("Fap Fap Fap", largeText)
        # TextRect.center = ((display_width / 2), (display_height / 2))
        # gamedisplay.blit(TextSurf, TextRect)
        # pygame.draw.rect(gamedisplay, green,(150,450,100,50))
        # pygame.draw.rect(gamedisplay, red,(550,450,100,50))

        # mouse = pygame.mouse.get_pos()
        playbutton(348, 310, gameloop)

        pygame.display.update()
        clock.tick(15)


# def eat():
#     all_imge = {}
#     for img in img_eat:
#         all_imge[img] = pygame.image.load(img)
#     for img in all_imge:
#         print(img)
#         gamedisplay.blit(all_imge[img], (150, 200))


# def drink():
#     all_imge = {}
#     for img in img_drink:
#         all_imge[img] = pygame.image.load(img)
#     for img in all_imge:
#         print(img)
#         gamedisplay.blit(all_imge[img], (150, 200))


def gameloop():
    counter1 = 0
    counter2 = 0
    lock_water = False
    time = 60
    start = pygame.time.get_ticks()
    progress = 1
    progress2 = 1
    p1_water = 40
    p2_water = 40
    done = False
    all_imge = []
    all_imgd = []
    all_imge2 = []
    all_imgd2 = []
    for img in range(len(img_eat)):
        all_imge2.append(pygame.image.load(img_eat2[img]))
    for img in range(len(img_drink)):
        all_imgd2.append(pygame.image.load(img_drink2[img]))
    for img in range(len(img_eat)):
        all_imge.append(pygame.image.load(img_eat[img]))
    for img in range(len(img_drink)):
        all_imgd.append(pygame.image.load(img_drink[img]))
    eat = False
    drink = False
    img = 0
    img2 = 0
    img3 = 0
    img4 = 0
    p1 = all_imge[img2]
    p2 = all_imge2[img3]
    while(not done):
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    progress = progress + 5
                    p2 = all_imge2[img3]
                    gamedisplay.blit(p2, (400, 310))
                    img3 = img3 + 1
                    img3 = img3 % 4
                if counter2 <= 0:
	                if event.key == pygame.K_LEFT:
	                    lock_water = True
	                    if counter1 < 5 and lock_water:
	                        counter1 += 1
	                    elif counter1 == 5:
	                        lock_water = False
	                        counter1 = 0
	                        progress = progress - p1_water
	                        continue
	                    lock_water = True
	                    p2 = all_imgd2[img4]
	                    gamedisplay.blit(p2, (400, 310))
	                    img4 = img4 + 1
	                    img4 = img4 % 5
                if event.key == pygame.K_z:
                    progress2 = progress2 + 5
                    p1 = all_imge[img2]
                    gamedisplay.blit(p1, (348, 310))
                    img2 = img2 + 1
                    img2 = img2 % 4
                if counter1 <= 0: 
                	lock_water = True
	                if event.key == pygame.K_x:
	                    if counter2 < 5 and lock_water:
	                        counter2 += 1
	                    elif counter2 == 5:
	                        lock_water = False
	                        progress2 = progress2 - p2_water
	                        counter2 = 0
	                        continue
	                    lock_water = True
	                    p1 = all_imgd[img]
	                    gamedisplay.blit(p1, (348, 310))
	                    img = img + 1
	                    img = img % 5	

        # print(event)
        t = time - ((pygame.time.get_ticks() - start) / 1000)
        # print(time-((pygame.time.get_ticks()-start)/1000))
        gamedisplay.blit(playbg, (0, 0))
        text = pygame.font.Font('Nithan.ttf', 40)
        TextSurf, TextRect1 = text_objects("press z to eat", text)
        TextSurf2, TextRect2 = text_objects("press x to drink", text)
        TextSurf3, TextRect3 = text_objects("press right arrow  to eat", text)
        TextSurf4, TextRect4 = text_objects("press letf arrow to drink", text)
        TextSurf5, TextRect5 = text_objects(str(int(t)), text)
        TextRect1.center = (150, 530)
        TextRect2.center = (150, 500)
        TextRect3.center = (600, 530)
        TextRect4.center = (600, 500)
        TextRect5.center = (400, 80)
        gamedisplay.blit(TextSurf, TextRect1)
        gamedisplay.blit(TextSurf2, TextRect2)
        gamedisplay.blit(TextSurf3, TextRect3)
        gamedisplay.blit(TextSurf4, TextRect4)
        gamedisplay.blit(TextSurf5, TextRect5)
        gamedisplay.blit(p1, (240, 270))
        gamedisplay.blit(p2, (370, 270))

        # p1.show()
        # if pygame.key.get_focused()[pygame.K_z] != 0:
        #     progress2 = progress2 + 5
        #     p1 = all_imge[img2]
        #     gamedisplay.blit(all_imge[img2], (120, 220))
        #     img2 = img2 % 4
        #     img2 = img2 + 1
        #     pygame.time.delay(10)
        # if pygame.key.get_pressed()[pygame.K_c] != 0:
        #     if progress2 - 10 > 0:
        #         progress2 = progress2 - p2_water

        #     p1 = all_imgd[img]
        #     gamedisplay.blit(all_imgd[img], (120, 220))
        #     img = img % 3
        #     img = img + 1
        #     pygame.time.delay(10)
        # if pygame.key.get_pressed()[pygame.K_LEFT] != 0:
        #     progress = progress + 5
        #     p2 = all_imge[img3]
        #     gamedisplay.blit(all_imge[img3], (500, 220))
        #     img3 = img3 % 4
        #     img3 = img3 + 1
        #     pygame.time.delay(10)
        # if pygame.key.get_pressed()[pygame.K_RIGHT] != 0:
        #     if progress - 10 > 0:
        #         progress = progress - p1_water

        #     p2 = all_imgd[img4]
        #     gamedisplay.blit(all_imgd[img4], (500, 220))
        #     img4 = img4 % 3
        #     img4 = img4 + 1
        #     pygame.time.delay(10)

        if progress <= 0 or progress2 <= 0 or t <= 0:
        	done = True
        	continue

        if((progress / 2) < 100 and (progress2 / 2) < 100):
            time_count = (random.randint(1, 1))

            # progress
            pygame.draw.rect(gamedisplay, green, [463, 123, 204, 49])
            pygame.draw.rect(gamedisplay, black, [464, 124, 202, 47])

            # progress2zz
            pygame.draw.rect(gamedisplay, green, [123, 123, 204, 49])
            pygame.draw.rect(gamedisplay, black, [124, 124, 202, 47])

            # progress2
            if (progress2 / 2) > 100:
                pygame.draw.rect(gamedisplay, green, [125, 125, 200, 45])
            else:
                pygame.draw.rect(gamedisplay, green, [125, 125, progress2, 45])
            # progress
            if (progress / 2) > 100:
                pygame.draw.rect(gamedisplay, green, [465, 125, 200, 45])
            else:
                pygame.draw.rect(gamedisplay, green, [465, 125, progress, 45])
            pygame.display.flip()
        else:
            done = True

        progress += 0.4
        progress2 += 0.4

        pygame.display.update()
        clock.tick(60)

    if t == 0:
        if progress > progress2:
            print('player 1 win')
            result(0)
        else:
            print('player 2 win')
            result(1)
    elif progress >= 200 or progress <= 0:
        print('player 2 die')
        result(0)
    elif progress2 >= 200 or progress2 <= 0:
        print('player 1 die')
        result(1)


def result(status):
    img = ['winner/P1winBG.png', 'winner/P2winBG.png']
    all_img = []
    sta = status
    for im in range(len(img)):
        all_img.append(pygame.image.load(img[im]))
    result = True
    while (result):
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gamedisplay.blit(all_img[sta], (0, 0))
        againbutton(350,445,gameloop)
        pygame.display.update()


# if __name__ == '__main__':
gameintro()
joingame()
gameloop()
result()
pygame.quit()
quit()
