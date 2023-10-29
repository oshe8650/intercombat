import pygame as pg
from random import randint

pg.init()
screen = pg.display.set_mode((1440, 720))
clock = pg.time.Clock()
running = True
player1_pos = pg.Vector2(screen.get_width() -25, screen.get_height() / 2)
player2_pos = pg.Vector2(25, screen.get_height() / 2)

dt = 0
dt1 = 0
dt2 = 0
cooldown1 = 1000
cooldown2 = 1000
timer_change = 0
timer_power = 0

##Klasser
class Player(pg.sprite.Sprite):
    def __init__(self, number):
        super().__init__()
        self.number = number
        if number == 1:
            self.image = pg.Surface((100, 100))
            self.image.fill("white")
            self.rect = self.image.get_rect(center = player1_pos)
            self.hp = 5
        elif number == 2:
            self.image = pg.Surface((100, 100))
            self.image.fill("white")
            self.rect = self.image.get_rect(center = player2_pos)
            self.hp = 5

    def update(self):
        global dt1
        global dt2
        dt1 += clock.get_time()
        dt2 += clock.get_time()

        hits = pg.sprite.spritecollide(self, bullet_group1, True)
        hits1 = pg.sprite.spritecollide(self, bullet_group2, True)
        if hits or hits1: #kollar om man har blivit träffad
            if self.number == 1:
                self.hp = self.hp - 1
                if self.hp == 0:
                    self.kill()
                    
            elif self.number == 2:
                self.hp -= 1
                if self.hp  == 0:
                    self.kill()

        key = pg.key.get_pressed()
        if self.number == 1:  
            if key[pg.K_UP]: 
                if self.rect.y > 0:
                    self.rect.y -= 5
            if key[pg.K_DOWN]:
                if self.rect.y < 720 - 100:
                    self.rect.y += 5
            if key[pg.K_SPACE] and dt1 > cooldown2:
                dt1 = 0
                bullet_group1.add(player1.shoot(1))
        elif self.number == 2:  
            if key[pg.K_w]: 
                if self.rect.y > 0:
                    self.rect.y -= 5
            if key[pg.K_s]:
                if self.rect.y < 720 - 100:
                    self.rect.y += 5
            if key[pg.K_LSHIFT] and dt2 > cooldown1:
                dt2 = 0
                bullet_group2.add(player2.shoot(2))

    def shoot(self, number):
        return Bullet(self.rect.x, self.rect.y, number)

class Bullet(pg.sprite.Sprite):
    def __init__(self, x, y, number):
        super().__init__()
        self.image = pg.Surface((50,10))
        self.image.fill("red")
        self.number = number
        if number == 1:
            self.rect = self.image.get_rect(center = (x-14, y+50))
        elif number == 2:
            self.rect = self.image.get_rect(center = (x+114, y+50))

        if self.rect.x < 0 or self.rect.x > 1440: #despawnar kulorna
            self.kill()

    def update(self):
        if self.number == 1:
            self.rect.x -= 700 * dt
        elif self.number == 2:
            self.rect.x += 700 * dt


class Powerups(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((100, 50))
        self.image.fill("red")
        x = randint(300, 1000)
        y = randint(100, 620)
        self.rect = self.image.get_rect(center = (x, y))

    def update(self):
        hit1 = pg.sprite.spritecollide(self, bullet_group2, True)
        hit2 = pg.sprite.spritecollide(self, bullet_group1, True)
        global cooldown1
        global cooldown2
        if hit2: 
            self.kill()
            if cooldown2 == 1000:
                cooldown2 = cooldown2/2
        elif hit1: 
            self.kill()
            if cooldown1 == 1000:
                cooldown1 = cooldown1/2
         
    
player1 = Player(1)
player2 = Player(2)
player_group = pg.sprite.Group()
player_group.add(player1, player2)
bullet_group1 = pg.sprite.Group()
bullet_group2 = pg.sprite.Group()
power_group = pg.sprite.Group()

    
while running:
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            


    timer_change += pg.time.get_ticks()
    timer_power += pg.time.get_ticks()

    if timer_change%1257 == 0:
        timer_change = 0
        power_group.empty()
        power = Powerups()
        power_group.add(power)
        
        
    if timer_power%200 == 0:    
        cooldown1 = 1000
        cooldown2 = 1000
        timer_power = 0


    screen.fill("black")
    bullet_group1.draw(screen)
    bullet_group2.draw(screen)
    player_group.draw(screen)
    power_group.draw(screen)
    player_group.update()
    bullet_group1.update()
    bullet_group2.update()
    power_group.update()


    pg.display.flip()

    dt = clock.tick(60) / 1000

pg.quit()