import pygame as pg

pg.init()
screen = pg.display.set_mode((1440, 720))
clock = pg.time.Clock()
running = True
player1_pos = pg.Vector2(screen.get_width() -25, screen.get_height() / 2)
player2_pos = pg.Vector2(25, screen.get_height() / 2)
bullet1_pos = pg.Vector2(player1_pos.x, player1_pos.y)


player_pos = pg.Vector2(screen.get_width() -25, screen.get_height() / 2)
bullet_pos = pg.Vector2(player_pos.x, player_pos.y)

dt = 0


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

        hits = pg.sprite.spritecollide(self, bullet_group, True)
        if hits: #kollar om man har blivit träffad
            if self.number == 1:
                self.hp = self.hp - 1
                if self.hp == 0:
                    self.kill()
                    
            elif self.number == 2:
                self.hp -= 1
                if self.hp  == 0:
                    self.kill()

        key = pg.key.get_pressed()  
        if key[pg.K_UP]:
            self.rect.y -= 5
        if key[pg.K_DOWN]:
            self.rect.y += 5
        if key[pg.K_SPACE] and dt1 > 1000:
            dt1 = 0
            bullet_group.add(player.shoot())

    def shoot(self):
        return Bullet(self.rect.x, self.rect.y)

class Bullet(pg.sprite.Sprite):
    def __init__(self, x, y, number):
        super().__init__()
        self.image = pg.Surface((50,10))
        self.image.fill("red")
        self.number = number
        if number == 1:
            self.rect = self.image.get_rect(center = (x-13, y+50))
        elif number == 2:
            self.rect = self.image.get_rect(center = (x+114, y+50))

        if self.rect.x < 0 or self.rect.x > 1440: #despawnar kulorna
            self.kill()

    def update(self):
        if self.number == 1:
            self.rect.x -= 700 * dt
        elif self.number == 2:
            self.rect.x += 700 * dt
    
player1 = Player(1)
player2 = Player(2)
player_group = pg.sprite.Group()
player_group.add(player1, player2)
bullet_group = pg.sprite.Group()

    
dt1 = 0
while running:
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            

    screen.fill("black")
    bullet_group.draw(screen)
    player_group.draw(screen)
    player_group.update()
    bullet_group.update()
    

        

    pg.display.flip()




    pg.display.flip()

    dt = clock.tick(60) / 1000

pg.quit()