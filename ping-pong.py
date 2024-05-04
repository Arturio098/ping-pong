from pygame import *
from random import randint
from time import time as tm 
#создай окно игры

# number = input('Какая сложность')

window = display.set_mode((800,400))
display.set_caption('ping pong ')
win_picture = transform.scale(image.load('tab.jpg'), (800, 400))


clock = time.Clock()



class Game_Sprite(sprite.Sprite):
    def __init__(self , player_image , player_x , player_y , w , h , player_speed):
        sprite.Sprite.__init__(self)

        self.image = transform.scale(image.load(player_image), (w , h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image , (self.rect.x, self.rect.y))

class Pplayer(Game_Sprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[ K_a ] and self.rect.x > 5:
            self.rect.x  -= self.speed
        if key_pressed[ K_d ] and self.rect.x < 730:
            self.rect.x  += self.speed
    def fiire(self):
        bullet = Bullet('zhurnal.jpg', self.rect.centerx, self.rect.top, 30, 20, -15)
        bullets.add(bullet)

scorp = 0
lost = 0

class Enemy(Game_Sprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > 500:
            self.rect.x = randint(80,720)
            self.rect.y = 0
            lost += 1

class Port_Enemy(Game_Sprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > 500:
            self.rect.x = randint(80,720)
            self.rect.y = 0


font.init()
font = font.Font(None, 70)

win = font.render( ' YOU SAVE THE PEINCESS ' , True , (255,0,0))
not_win = font.render( ' YOU DIE ' , True , (255,0,0))


game = True
finish = False
while game:
    
    
    for i in event.get():
        if i.type == QUIT:
            game = False 



    if finish != True:

        window.blit(win_picture,(0,0))



    display.update()
    clock.tick(60)
