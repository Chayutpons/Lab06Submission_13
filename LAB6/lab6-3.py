import sys
import pygame as pg

pg.init()
win_x, win_y = 800, 600
screen = pg.display.set_mode((win_x, win_y))

COLOR_INACTIVE = pg.Color('lightskyblue3') # ตั้งตัวแปรให้เก็บค่าสี เพื่อนำไปใช้เติมสีให้กับกล่องข้อความตอนที่คลิกที่กล่องนั้นๆอยู่
COLOR_ACTIVE = pg.Color('dodgerblue2')     # ^^^
FONT = pg.font.Font(None, 32)

class InputBox:

    def __init__(self, x, y, w, h, m, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
        self.mode = m

    def handle_event(self, event):
        
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE # เปลี่ยนสีของ InputBox
            
        if event.type == pg.KEYDOWN:
            key = event.key
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if self.mode:
                        if chr(event.key).isnumeric():
                            self.text += event.unicode
                    else:
                        self.text += event.unicode
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)

class SubmitBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                text_box5.text = 'Hello ' + input_box1.text + ' ' +  input_box2.text + ' You are ' + input_box3.text + ' years old '
                text_box5.txt_surface = FONT.render(text_box5.text, True, text_box5.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)

text1 = FONT.render('Name :', True, pg.Color("black"))
text1Rect = text1.get_rect()
text1Rect.center = (200, 100)
text2 = FONT.render('Surname :', True, pg.Color("black"))
text2Rect = text1.get_rect()
text2Rect.center = (200, 200)
text3 = FONT.render('Age :', True, pg.Color("black"))
text3Rect = text1.get_rect()
text3Rect.center = (200, 300)
input_box1 = InputBox(300, 100 - 15, 140, 32, False) # สร้าง InputBox1
input_box2 = InputBox(300, 200- 15, 140, 32, False) # สร้าง InputBox2
input_box3 = InputBox(300, 300- 15, 140, 32, True) # สร้าง InputBox2
text_box5 = InputBox(300, 500- 15, 140, 32, False)

text_box4 = SubmitBox(300, 350, 40, 50, 'Submit')

input_boxes = [input_box1, input_box2, input_box3, text_box4, text_box5] # เก็บ InputBox ไว้ใน list เพื่อที่จะสามารถนำไปเรียกใช้ได้ง่าย
run = True

while run:
    screen.fill((255, 255, 255))

    screen.blit(text1, text1Rect)
    screen.blit(text2, text2Rect)
    screen.blit(text3, text3Rect)
    for box in input_boxes: # ทำการเรียก InputBox ทุกๆตัว โดยการ Loop เข้าไปยัง list ที่เราเก็บค่า InputBox ไว้
        box.update() # เรียกใช้ฟังก์ชัน update() ของ InputBox
        box.draw(screen) # เรียกใช้ฟังก์ชัน draw() ของ InputBox เพื่อทำการสร้างรูปบน Screen
        
    for event in pg.event.get():
        for box in input_boxes:
            box.handle_event(event)
        if event.type == pg.QUIT:
            pg.quit()
            run = False

    pg.time.delay(1)
    pg.display.update()