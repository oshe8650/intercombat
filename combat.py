from typing import Any
import pygame as pg
from random import randint
pg.init()
screen = pg.display.set_mode((1440, 720))
clock = pg.time.Clock()
running = True

player_pos = pg.Vector2(screen.get_width() -25, screen.get_height() / 2)
bullet_pos = pg.Vector2(player_pos.x, player_pos.y)

dt = 0
dt1 = 0
cooldownP1 = 500
cooldownP2 = 5000

##Klasser
class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((100, 100))
        self.image.fill("white")
        self.rect = self.image.get_rect(center = (screen.get_width() - 25, screen.get_height()/2))

    def update(self):
        global dt1
        dt1 += clock.get_time()

        key = pg.key.get_pressed()  
        if key[pg.K_UP]:
            self.rect.y -= 5
        if key[pg.K_DOWN]:
            self.rect.y += 5
        if key[pg.K_SPACE] and dt1 > cooldownP1:
            dt1 = 0
            bullet_group.add(player.shoot())

    def shoot(self):
        return Bullet(self.rect.x, self.rect.y)

class Bullet(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.Surface((50,10))
        self.image.fill("red")
        self.rect = self.image.get_rect(center = (x, y))

    def update(self):
        self.rect.x -= 10
        
    def hit(self, x, y):
        if self.rect.x and self.rect.y == x and y:
            power_group.empty()
     

class Powerups(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((100, 50))
        self.image.fill("red")
        x = randint(300, 1000)
        y = randint(100, 620)
        self.rect = self.image.get_rect(center = (x, y))

    def hit(self):
        return Bullet.hit(self, self.rect.x, self.rect.y)
        

            
       
       
            
    
        

 

        
player = Player()
player_group = pg.sprite.Group()
player_group.add(player)
bullet_group = pg.sprite.Group()
power_group = pg.sprite.Group()

while running:
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    if clock.get_time()%10 == 0:
        power_group.empty()
        power = Powerups()
        power_group.add(power)
    
        
 
        
    

    screen.fill("black")
    power_group.draw(screen)
    bullet_group.draw(screen)
    player_group.draw(screen)
    player_group.update()
    bullet_group.update()
    power.hit()
    
    



    pg.display.flip()

    dt = clock.tick(60) / 1000

pg.quit()