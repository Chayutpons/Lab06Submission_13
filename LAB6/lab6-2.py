import sys
import pygame as pg

pg.init()

WIN_X, WIN_Y = 800, 400
screen = pg.display.set_mode((WIN_X,WIN_Y))

class Rectangle:
    def __init__(self, x=0, y=0, w=0, h=0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    def draw(self,screen):
        pg.draw.rect(screen,(100,100,100),(self.y, self.x, self.w, self.h))

obj = Rectangle(100,100,100,100)

while(True):
    screen.fill((255,255,255))
    obj.draw(screen)
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

        if event.type == pg.KEYDOWN and event.key == pg.K_w:
            obj.x -= 10
        if event.type == pg.KEYDOWN and event.key == pg.K_a:
            obj.y -= 10
        if event.type == pg.KEYDOWN and event.key == pg.K_s:
            obj.x += 10
        if event.type == pg.KEYDOWN and event.key == pg.K_d:
            obj.y += 10
