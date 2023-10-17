import pygame as pg

pg.init()
screen = pg.display.set_mode((1440, 720))
clock = pg.time.Clock()
running = True
player_pos = pg.Vector2(screen.get_width() -25, screen.get_height() / 2)
bullet_pos = pg.Vector2(player_pos.x, player_pos.y)
dt = 10




while running:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill("black")

    pg.draw.circle(screen, "white", player_pos, 20)



    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
        player_pos.y -= 300 * dt
    if keys[pg.K_s]:
        player_pos.y += 300 * dt
    if keys[pg.K_SPACE]:
        bullet = pg.draw.circle(screen, "red", bullet_pos, 5)
    bullet_pos.x -= 300* dt



    pg.display.flip()

    dt = clock.tick(60) / 1000

pg.quit()