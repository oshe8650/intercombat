import pygame as pg

pg.init()
screen = pg.display.set_mode((1440, 720))
clock = pg.time.Clock()
running = True
player_pos = pg.Vector2(screen.get_width() -25, screen.get_height() / 2)
bullet_pos = pg.Vector2(player_pos.x, player_pos.y)
dt = 0

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((100, 100))
        self.image.fill("white")
        self.rect = self.image.get_rect(center = (screen.get_width() - 25, screen.get_height()/2))

    def update(self):
        key = pg.key.get_pressed()  
        if key[pg.K_UP]:
            self.rect.y -= 5
        if key[pg.K_DOWN]:
            self.rect.y += 5
        if key[pg.K_SPACE]:
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
        
    
player = Player()
player_group = pg.sprite.Group()
player_group.add(player)
bullet_group = pg.sprite.Group()

    

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

    dt = clock.tick(60) / 1000

pg.quit()