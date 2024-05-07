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
    def update_l(self):
        key_pressed = key.get_pressed()
        if key_pressed[ K_w ] and self.rect.y > 5:
            self.rect.y  -= self.speed
        if key_pressed[ K_s ] and self.rect.y < 350:
            self.rect.y  += self.speed
    def update_r(self):
        key_pressed = key.get_pressed()
        if key_pressed[ K_UP ] and self.rect.y > 5:
            self.rect.y  -= self.speed
        if key_pressed[ K_DOWN ] and self.rect.y < 350:
            self.rect.y  += self.speed


scorp = 0
lost = 0

r_raketa = Pplayer('raketa.png',750, 50, 50, 80, 10)
l_raketa = Pplayer('raketa.png',0, 50, 50, 80, 10)
ball = Game_Sprite('ball.jpg',350, 150, 50, 50, 10)


font.init()
font = font.Font(None, 70)

win = font.render( ' YOU SAVE THE PEINCESS ' , True , (255,0,0))
not_win = font.render( ' YOU DIE ' , True , (255,0,0))

speed_x = 3
speed_y = 3

game = True
finish = False
while game:
    
    
    for i in event.get():
        if i.type == QUIT:
            game = False 



    if finish != True:

        window.blit(win_picture,(0,0))

        r_raketa.update_r()
        l_raketa.update_l()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        
        r_raketa.reset()
        l_raketa.reset()
        ball.reset()

        
        if ball.rect.y > 350 or ball.rect.y < 0:
            speed_y *= -1
            
        if sprite.collide_rect(l_raketa, ball) or sprite.collide_rect(r_raketa, ball):
            speed_x *= -1

    display.update()
    clock.tick(60)
