from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

pos_x = 0
pos_y = 0

hijau = 0
biru = 0
merah = 0

virus_x = 0

temp_x = -720
temp_y = 250

temp_y_virus_1 = 1200
temp_y_virus_2 = 620
temp_y_virus_3 = 690
temp_y_virus_4 = 1020
temp_y_virus_5 = 800
temp_y_virus_6 = 500
temp_y_virus_7 = 700
temp_y_virus_8 = 840
temp_y_virus_9 = 900
temp_y_virus_10 = 1400
temp_y_virus_11 = 1080
temp_y_virus_12 = 2800
temp_y_virus_13 = 1100

kecepatan_virus1 = 1.2
kecepatan_virus2 = 2
kecepatan_virus3 = 1.6
kecepatan_virus4 = 1.3
kecepatan_virus5 = 1.7
kecepatan_virus6 = 1.46
kecepatan_virus7 = 1.38
kecepatan_virus8 = 1.8
kecepatan_virus9 = 1.12
kecepatan_virus10 = 1.4
kecepatan_virus11 = 2
kecepatan_virus12 = 1.72
kecepatan_virus13 = 1.8

peluru_x = 0
peluru_y = 0
kecepatan_peluru = 10

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-720.0, 720.0, -500.0, 500.0)

def player():
    #sepatu
    glColor3ub(0 , 220 ,200)
    glBegin(GL_QUADS)
    glVertex2f(30 + pos_x, -300)
    glVertex2f(20 + pos_x, -290)
    glVertex2f(10 + pos_x, -290)
    glVertex2f(10 + pos_x, -300)
    glEnd()
    glColor3ub(0 , 220 ,200)
    glBegin(GL_QUADS)
    glVertex2f(-10 + pos_x, -300)
    glVertex2f(-30 + pos_x, -300)
    glVertex2f(-20 + pos_x, -290)
    glVertex2f(-10 + pos_x, -290)
    glEnd()
    #kaki
    glColor3ub(255, 255, 255)
    glBegin(GL_POLYGON)
    glVertex2f(20 + pos_x, -290)
    glVertex2f(20 + pos_x, -280)
    glVertex2f(10 + pos_x, -280)
    glVertex2f(10 + pos_x, -290)
    glEnd()
    glColor3ub(255, 255, 255)
    glBegin(GL_POLYGON)
    glVertex2f(-20 + pos_x, -280)
    glVertex2f(-10 + pos_x, -280)
    glVertex2f(-10 + pos_x, -290)
    glVertex2f(-20 + pos_x, -290)
    glEnd()
    #badan
    glColor3ub(255, 255, 255)
    glBegin(GL_POLYGON)
    glVertex2f(30 + pos_x, -280)
    glVertex2f(-30 + pos_x, -280)
    glVertex2f(-30 + pos_x, -250)
    glVertex2f(30 + pos_x, -250)
    glEnd()
    glColor3ub(255, 255, 255)
    glBegin(GL_POLYGON)
    glVertex2f(-30 + pos_x, -210)
    glVertex2f(30 + pos_x, -210)
    glVertex2f(30 + pos_x, -250)
    glVertex2f(-30 + pos_x, -250)
    glEnd()
    #sabuk
    glColor3ub(0, 26, 255)
    glBegin(GL_POLYGON)
    glVertex2f(-30 + pos_x, -255)
    glVertex2f(30 + pos_x, -255)
    glVertex2f(30 + pos_x, -250)
    glVertex2f(-30 + pos_x, -250)
    glEnd()
    glColor3ub(0, 26, 255)
    glBegin(GL_POLYGON)
    glVertex2f(-2 + pos_x, -280)
    glVertex2f(-2 + pos_x, -210)
    glVertex2f(2 + pos_x, -210)
    glVertex2f(2 + pos_x, -280)
    glEnd()
    #tangan
    glColor3ub(255, 255, 255)
    glBegin(GL_POLYGON)
    glVertex2f(30 + pos_x, -210)
    glVertex2f(30 + pos_x, -220)
    glVertex2f(50 + pos_x, -220)
    glVertex2f(40 + pos_x, -210)
    glEnd()
    glColor3ub(255, 255, 255)
    glBegin(GL_POLYGON)
    glVertex2f(40 + pos_x, -210)
    glVertex2f(50 + pos_x, -220)
    glVertex2f(50 + pos_x, -190)
    glVertex2f(40 + pos_x, -190)
    glEnd()
    glColor3ub(255, 255, 255)
    glBegin(GL_POLYGON)
    glVertex2f(-30 + pos_x, -210)
    glVertex2f(-30 + pos_x, -220)
    glVertex2f(-40 + pos_x, -220)
    glVertex2f(-50 + pos_x, -210)
    glEnd()
    glColor3ub(255, 255, 255)
    glBegin(GL_POLYGON)
    glVertex2f(-50 + pos_x, -210)
    glVertex2f(-40 + pos_x, -220)
    glVertex2f(-40 + pos_x, -250)
    glVertex2f(-50 + pos_x, -250)
    glEnd()
    #leher
    glColor3ub(255, 255, 255)
    glBegin(GL_POLYGON)
    glVertex2f(-10 + pos_x, -210)
    glVertex2f(10 + pos_x, -210)
    glVertex2f(10 + pos_x, -200)
    glVertex2f(-10 + pos_x, -200)
    glEnd()
    #kepala
    glColor3ub(255, 255, 255)
    glBegin(GL_POLYGON)
    glVertex2f(-25 + pos_x, -160)
    glVertex2f(25 + pos_x, -160)
    glVertex2f(25 + pos_x, -200)
    glVertex2f(-25 + pos_x, -200)
    glEnd()
    #muka
    glColor3ub(207, 150, 107)
    glBegin(GL_POLYGON)
    glVertex2f(-20 + pos_x, -165)
    glVertex2f(20 + pos_x, -165)
    glVertex2f(20 + pos_x, -195)
    glVertex2f(-20 + pos_x, -195)
    glEnd()
    #suntik
    glColor3ub(201, 201, 201)
    glBegin(GL_POLYGON)
    glVertex2f(35 + pos_x, -190)
    glVertex2f(55 + pos_x, -190)
    glVertex2f(50 + pos_x, -185)
    glVertex2f(40 + pos_x, -185)
    glEnd()
    glColor3ub(201, 201, 201)
    glBegin(GL_LINES)
    glVertex2f(45 + pos_x, -185)
    glVertex2f(45 + pos_x, -180)
    glEnd()
    glColor3ub(201, 201, 201)
    glBegin(GL_POLYGON)
    glVertex2f(40 + pos_x, -180)
    glVertex2f(50 + pos_x, -180)
    glVertex2f(50 + pos_x, -160)
    glVertex2f(45 + pos_x, -155)
    glVertex2f(40 + pos_x, -160)
    glEnd()
    glColor3ub(201, 201, 201)
    glBegin(GL_LINES)
    glVertex2f(45 + pos_x, -155)
    glVertex2f(45 + pos_x, -150)
    glEnd()

def virus():
    glColor3ub(201, 201, 201)
    glBegin(GL_POLYGON)
    glVertex2f(-110.4, 65.4)
    glVertex2f(-117.3, 77.8)
    glVertex2f(-121.5, 65.4)
    glVertex2f(-132.5, 72.8)
    glVertex2f(-130, 60)
    glVertex2f(-143, 63.4)
    glVertex2f(-136, 52.7)
    glVertex2f(-149, 47.6)
    glVertex2f(-136, 42.8)
    glVertex2f(-143.9, 32)
    glVertex2f(-131.5, 32.7)
    glVertex2f(-132.8, 21)
    glVertex2f(-121.5, 27.5)
    glVertex2f(-115.8, 15.9)
    glVertex2f(-110.4, 27.5)
    glVertex2f(-100, 20)
    glVertex2f(-102.7, 32.7)
    glVertex2f(-89.6, 32)
    glVertex2f(-97.9, 42.2)
    glVertex2f(-85.8, 46)
    glVertex2f(-97.9, 51)
    glVertex2f(-91.3, 63.2)
    glVertex2f(-103, 60)
    glVertex2f(-100.7, 72.8)
    glVertex2f(-110.4, 65.4)
    glVertex2f(-117.3, 77.8)
    glEnd()

def gedung():
    #gedung1
    glColor3ub(201, 201, 201)
    glBegin(GL_LINE_LOOP)
    glVertex2f(-620, 200)
    glVertex2f(-620, -300)
    glVertex2f(-450, -300)
    glVertex2f(-450, 200)
    glEnd()
    #jendela1
    glColor3ub(201, 201, 201)
    glBegin(GL_LINE_LOOP)
    glVertex2f(-600, -270)
    glVertex2f(-570, -270)
    glVertex2f(-570, 150)
    glVertex2f(-600, 150)
    glEnd()
    #jendela2
    glColor3ub(201, 201, 201)
    glBegin(GL_LINE_LOOP)
    glVertex2f(-550, -270)
    glVertex2f(-520, -270)
    glVertex2f(-520, 150)
    glVertex2f(-550, 150)
    glEnd()
    #jendela3
    glColor3ub(201, 201, 201)
    glBegin(GL_LINE_LOOP)
    glVertex2f(-500, -270)
    glVertex2f(-470, -270)
    glVertex2f(-470, 150)
    glVertex2f(-500, 150)
    glEnd()
    #gedung2
    glColor3ub(201, 201, 201)
    glBegin(GL_LINE_LOOP)
    glVertex2f(-450, -300)
    glVertex2f(-280, -300)
    glVertex2f(-280, 300)
    glVertex2f(-475, 300)
    glVertex2f(-475, 200)
    glVertex2f(-450, 200)
    glVertex2f(-450, -300)
    glVertex2f(-370, -300)
    glVertex2f(-370, 260)
    glVertex2f(-370, 300)
    glVertex2f(-475, 300)
    glVertex2f(-475, 260)
    glVertex2f(-280, 260)
    glVertex2f(-280, -300)
    glEnd()
    #pucuk
    glColor3ub(201, 201, 201)
    glBegin(GL_LINE_LOOP)
    glVertex2f(-400, 300)
    glVertex2f(-345, 300)
    glVertex2f(-370, 400)
    glEnd()
    #gedung3
    glColor3ub(201, 201, 201)
    glBegin(GL_LINE_LOOP)
    glVertex2f(-170, -300)
    glVertex2f(0, -300)
    glVertex2f(0, 30)
    glVertex2f(-170, 30)
    glEnd()
    #jendela1
    glColor3ub(201, 201, 201)
    glBegin(GL_LINE_LOOP)
    glVertex2f(-140, -200)
    glVertex2f(-20, -200)
    glVertex2f(-20, -170)
    glVertex2f(-140, -170)
    glEnd()
    #jendela2
    glColor3ub(201, 201, 201)
    glBegin(GL_LINE_LOOP)
    glVertex2f(-140, -150)
    glVertex2f(-20, -150)
    glVertex2f(-20, -120)
    glVertex2f(-140, -120)
    glEnd()
    #jendela3
    glColor3ub(201, 201, 201)
    glBegin(GL_LINE_LOOP)
    glVertex2f(-140, -100)
    glVertex2f(-20, -100)
    glVertex2f(-20, -70)
    glVertex2f(-140, -70)
    glEnd()
    #jendela4
    glColor3ub(201, 201, 201)
    glBegin(GL_LINE_LOOP)
    glVertex2f(-140, -50)
    glVertex2f(-20, -50)
    glVertex2f(-20, -20)
    glVertex2f(-140, -20)
    glEnd()
    #gedung4
    glColor3ub(201, 201, 201)
    glBegin(GL_LINE_LOOP)
    glVertex2f(0, -300)
    glVertex2f(170, -300)
    glVertex2f(170, 200)
    glVertex2f(0, 150) 
    glEnd()
    #jendela1
    glColor3ub(201, 201, 201)
    glBegin(GL_LINE_LOOP)
    glVertex2f(33, -200)
    glVertex2f(77, -200)
    glVertex2f(77, -40)
    glVertex2f(33, -40)
    glEnd()
    #jendela2
    glColor3ub(201, 201, 201)
    glBegin(GL_LINE_LOOP)
    glVertex2f(100, -200)
    glVertex2f(140, -200)
    glVertex2f(140, -40)
    glVertex2f(100, -40)
    glEnd()
    #jendela3
    glColor3ub(201, 201, 201)
    glBegin(GL_LINE_LOOP)
    glVertex2f(33,0)
    glVertex2f(77, 0)
    glVertex2f(77, 110)
    glVertex2f(33, 110)
    glEnd()
    #jendela4
    glColor3ub(201, 201, 201)
    glBegin(GL_LINE_LOOP)
    glVertex2f(100, 0)
    glVertex2f(140, 0)
    glVertex2f(140, 110)
    glVertex2f(100, 110)
    glEnd()
    #gedung5
    #kiri
    glColor3ub(201, 201, 201)
    glBegin(GL_LINE_LOOP)
    glVertex2f(170, -300)
    glVertex2f(350, -300)
    glVertex2f(350, 160)
    glVertex2f(300, 160)
    glVertex2f(300, 90)
    glVertex2f(240, 90)
    glVertex2f(240, 40)
    glVertex2f(170, 40)
    glEnd()
    #jendela1
    glColor3ub(201, 201, 201)
    glBegin(GL_LINE_LOOP)
    glVertex2f(200, -250)
    glVertex2f(250, -250)
    glVertex2f(250, -200)
    glVertex2f(200, -200)
    glEnd()
    #jendela2
    glColor3ub(201, 201, 201)
    glBegin(GL_LINE_LOOP)
    glVertex2f(200, -150)
    glVertex2f(250, -150)
    glVertex2f(250, -100)
    glVertex2f(200, -100)
    glEnd()
    #jendela3
    glColor3ub(201, 201, 201)
    glBegin(GL_LINE_LOOP)
    glVertex2f(200, -50)
    glVertex2f(250, -50)
    glVertex2f(250, 0)
    glVertex2f(200, 0)
    glEnd()
    #jendela4
    glColor3ub(201, 201, 201)
    glBegin(GL_LINE_LOOP)
    glVertex2f(280, -250)
    glVertex2f(325, -250)
    glVertex2f(325, -200)
    glVertex2f(280, -200)
    glEnd()
    #jendela5
    glColor3ub(201, 201, 201)
    glBegin(GL_LINE_LOOP)
    glVertex2f(280, -150)
    glVertex2f(325, -150)
    glVertex2f(325, -100)
    glVertex2f(280, -100)
    glEnd()
    #jendela6
    glColor3ub(201, 201, 201)
    glBegin(GL_LINE_LOOP)
    glVertex2f(280, -50)
    glVertex2f(325, -50)
    glVertex2f(325, 0)
    glVertex2f(280, 0)
    glEnd()
    #jendela7
    glColor3ub(201, 201, 201)
    glBegin(GL_LINE_LOOP)
    glVertex2f(280, 50)
    glVertex2f(325, 50)
    glVertex2f(325, 70)
    glVertex2f(280, 70)
    glEnd()
    #kanan
    glColor3ub(201, 201, 201)
    glBegin(GL_LINE_LOOP)
    glVertex2f(400, -300)
    glVertex2f(600, -300)
    glVertex2f(600, 40)
    glVertex2f(520, 40)
    glVertex2f(520, 90)
    glVertex2f(460, 90)
    glVertex2f(460, 160)
    glVertex2f(400, 160)
    glEnd()
    #jendela1
    glColor3ub(201, 201, 201)
    glBegin(GL_LINE_LOOP)
    glVertex2f(510, -250)
    glVertex2f(560, -250)
    glVertex2f(560, -200)
    glVertex2f(510, -200)
    glEnd()
    #jendela2
    glColor3ub(201, 201, 201)
    glBegin(GL_LINE_LOOP)
    glVertex2f(430, -250)
    glVertex2f(480, -250)
    glVertex2f(480, -200)
    glVertex2f(430, -200)
    glEnd()
    #jendela3
    glColor3ub(201, 201, 201)
    glBegin(GL_LINE_LOOP)
    glVertex2f(510, -150)
    glVertex2f(560, -150)
    glVertex2f(560, -100)
    glVertex2f(510, -100)
    glEnd()
    #jendela4
    glColor3ub(201, 201, 201)
    glBegin(GL_LINE_LOOP)
    glVertex2f(430, -150)
    glVertex2f(480, -150)
    glVertex2f(480, -100)
    glVertex2f(430, -100)
    glEnd()
    #jendela5
    glColor3ub(201, 201, 201)
    glBegin(GL_LINE_LOOP)
    glVertex2f(430, -50)
    glVertex2f(480, -50)
    glVertex2f(480, 0)
    glVertex2f(430, 0)
    glEnd()
    #jendela6
    glColor3ub(201, 201, 201)
    glBegin(GL_LINE_LOOP)
    glVertex2f(430, 50)
    glVertex2f(480, 50)
    glVertex2f(480, 70)
    glVertex2f(430, 70)
    glEnd()
    #jendela7
    glColor3ub(201, 201, 201)
    glBegin(GL_LINE_LOOP)
    glVertex2f(510, -50)
    glVertex2f(560, -50)
    glVertex2f(560, 0)
    glVertex2f(510, 0)
    glEnd()
    #gedung6
    glColor3ub(201, 201, 201)
    glBegin(GL_LINE_LOOP)
    glVertex2f(-85, 30)
    glVertex2f(-85, 200)
    glVertex2f(40, 200)
    glVertex2f(40, 160)
    glVertex2f(0, 150)
    glVertex2f(0, -300)
    glVertex2f(-170,-300)
    glVertex2f(-170, 30)
    glEnd()
    #gedung7
    glColor3ub(201, 201, 201)
    glBegin(GL_LINE_LOOP)
    glVertex2f(260, 90)
    glVertex2f(260, 250)
    glVertex2f(285, 310)
    glVertex2f(310, 250)
    glVertex2f(310, 160)
    glVertex2f(350, 160)
    glVertex2f(350, -300)
    glVertex2f(170, -300)
    glVertex2f(170, 40)
    glVertex2f(240, 40)
    glVertex2f(240, 90)
    glEnd()

def virus1():
    global temp_y_virus_1, kecepatan_virus1

    if temp_y_virus_1 <= -500:
        temp_y_virus_1 = 500

    temp_y_virus_1 -= kecepatan_virus1

    glPushMatrix()
    glTranslated(-400, temp_y_virus_1 , 0)

    glColor3ub(82, 235, 0)
    glBegin(GL_POLYGON)
    glVertex2f(-110.4, 65.4)
    glVertex2f(-117.3, 77.8)
    glVertex2f(-121.5, 65.4)
    glVertex2f(-132.5, 72.8)
    glVertex2f(-130, 60)
    glVertex2f(-143, 63.4)
    glVertex2f(-136, 52.7)
    glVertex2f(-149, 47.6)
    glVertex2f(-136, 42.8)
    glVertex2f(-143.9, 32)
    glVertex2f(-131.5, 32.7)
    glVertex2f(-132.8, 21)
    glVertex2f(-121.5, 27.5)
    glVertex2f(-115.8, 15.9)
    glVertex2f(-110.4, 27.5)
    glVertex2f(-100, 20)
    glVertex2f(-102.7, 32.7)
    glVertex2f(-89.6, 32)
    glVertex2f(-97.9, 42.2)
    glVertex2f(-85.8, 46)
    glVertex2f(-97.9, 51)
    glVertex2f(-91.3, 63.2)
    glVertex2f(-103, 60)
    glVertex2f(-100.7, 72.8)
    glVertex2f(-110.4, 65.4)
    glVertex2f(-117.3, 77.8)
    glEnd()
    glPopMatrix()

def virus2():
    global temp_y_virus_2, kecepatan_virus2

    if temp_y_virus_2 <= -500:
        temp_y_virus_2 = 500

    temp_y_virus_2 -= kecepatan_virus2

    glPushMatrix()
    glTranslated(170, temp_y_virus_2, 0)

    glColor3ub(82, 235, 0)
    glBegin(GL_POLYGON)
    glVertex2f(-110.4, 65.4)
    glVertex2f(-117.3, 77.8)
    glVertex2f(-121.5, 65.4)
    glVertex2f(-132.5, 72.8)
    glVertex2f(-130, 60)
    glVertex2f(-143, 63.4)
    glVertex2f(-136, 52.7)
    glVertex2f(-149, 47.6)
    glVertex2f(-136, 42.8)
    glVertex2f(-143.9, 32)
    glVertex2f(-131.5, 32.7)
    glVertex2f(-132.8, 21)
    glVertex2f(-121.5, 27.5)
    glVertex2f(-115.8, 15.9)
    glVertex2f(-110.4, 27.5)
    glVertex2f(-100, 20)
    glVertex2f(-102.7, 32.7)
    glVertex2f(-89.6, 32)
    glVertex2f(-97.9, 42.2)
    glVertex2f(-85.8, 46)
    glVertex2f(-97.9, 51)
    glVertex2f(-91.3, 63.2)
    glVertex2f(-103, 60)
    glVertex2f(-100.7, 72.8)
    glVertex2f(-110.4, 65.4)
    glVertex2f(-117.3, 77.8)
    glEnd()
    glPopMatrix()

def virus3():
    global temp_y_virus_3, kecepatan_virus3

    if temp_y_virus_3 <= -500:
        temp_y_virus_3 = 500

    temp_y_virus_3 -= kecepatan_virus3

    glPushMatrix()
    glTranslated(-150, temp_y_virus_3, 0)

    glColor3ub(82, 235, 0)
    glBegin(GL_POLYGON)
    glVertex2f(-110.4, 65.4)
    glVertex2f(-117.3, 77.8)
    glVertex2f(-121.5, 65.4)
    glVertex2f(-132.5, 72.8)
    glVertex2f(-130, 60)
    glVertex2f(-143, 63.4)
    glVertex2f(-136, 52.7)
    glVertex2f(-149, 47.6)
    glVertex2f(-136, 42.8)
    glVertex2f(-143.9, 32)
    glVertex2f(-131.5, 32.7)
    glVertex2f(-132.8, 21)
    glVertex2f(-121.5, 27.5)
    glVertex2f(-115.8, 15.9)
    glVertex2f(-110.4, 27.5)
    glVertex2f(-100, 20)
    glVertex2f(-102.7, 32.7)
    glVertex2f(-89.6, 32)
    glVertex2f(-97.9, 42.2)
    glVertex2f(-85.8, 46)
    glVertex2f(-97.9, 51)
    glVertex2f(-91.3, 63.2)
    glVertex2f(-103, 60)
    glVertex2f(-100.7, 72.8)
    glVertex2f(-110.4, 65.4)
    glVertex2f(-117.3, 77.8)
    glEnd()
    glPopMatrix()

def virus4():
    global temp_y_virus_4, kecepatan_virus4

    if temp_y_virus_4 <= -500:
        temp_y_virus_4 = 500

    temp_y_virus_4 -= kecepatan_virus4

    glPushMatrix()
    glTranslated(260, temp_y_virus_4, 0)

    glColor3ub(82, 235, 0)
    glBegin(GL_POLYGON)
    glVertex2f(-110.4, 65.4)
    glVertex2f(-117.3, 77.8)
    glVertex2f(-121.5, 65.4)
    glVertex2f(-132.5, 72.8)
    glVertex2f(-130, 60)
    glVertex2f(-143, 63.4)
    glVertex2f(-136, 52.7)
    glVertex2f(-149, 47.6)
    glVertex2f(-136, 42.8)
    glVertex2f(-143.9, 32)
    glVertex2f(-131.5, 32.7)
    glVertex2f(-132.8, 21)
    glVertex2f(-121.5, 27.5)
    glVertex2f(-115.8, 15.9)
    glVertex2f(-110.4, 27.5)
    glVertex2f(-100, 20)
    glVertex2f(-102.7, 32.7)
    glVertex2f(-89.6, 32)
    glVertex2f(-97.9, 42.2)
    glVertex2f(-85.8, 46)
    glVertex2f(-97.9, 51)
    glVertex2f(-91.3, 63.2)
    glVertex2f(-103, 60)
    glVertex2f(-100.7, 72.8)
    glVertex2f(-110.4, 65.4)
    glVertex2f(-117.3, 77.8)
    glEnd()
    glPopMatrix()

def virus5():
    global temp_y_virus_5, kecepatan_virus5

    if temp_y_virus_5 <= -500:
        temp_y_virus_5 = 500

    temp_y_virus_5 -= kecepatan_virus5

    glPushMatrix()
    glTranslated(510, temp_y_virus_5, 0)

    glColor3ub(82, 235, 0)
    glBegin(GL_POLYGON)
    glVertex2f(-110.4, 65.4)
    glVertex2f(-117.3, 77.8)
    glVertex2f(-121.5, 65.4)
    glVertex2f(-132.5, 72.8)
    glVertex2f(-130, 60)
    glVertex2f(-143, 63.4)
    glVertex2f(-136, 52.7)
    glVertex2f(-149, 47.6)
    glVertex2f(-136, 42.8)
    glVertex2f(-143.9, 32)
    glVertex2f(-131.5, 32.7)
    glVertex2f(-132.8, 21)
    glVertex2f(-121.5, 27.5)
    glVertex2f(-115.8, 15.9)
    glVertex2f(-110.4, 27.5)
    glVertex2f(-100, 20)
    glVertex2f(-102.7, 32.7)
    glVertex2f(-89.6, 32)
    glVertex2f(-97.9, 42.2)
    glVertex2f(-85.8, 46)
    glVertex2f(-97.9, 51)
    glVertex2f(-91.3, 63.2)
    glVertex2f(-103, 60)
    glVertex2f(-100.7, 72.8)
    glVertex2f(-110.4, 65.4)
    glVertex2f(-117.3, 77.8)
    glEnd()
    glPopMatrix()

def virus6():
    global temp_y_virus_6, kecepatan_virus6

    if temp_y_virus_6 <= -500:
        temp_y_virus_6 = 500

    temp_y_virus_6 -= kecepatan_virus6

    glPushMatrix()
    glTranslated(-260, temp_y_virus_6, 0)

    glColor3ub(82, 235, 0)
    glBegin(GL_POLYGON)
    glVertex2f(-110.4, 65.4)
    glVertex2f(-117.3, 77.8)
    glVertex2f(-121.5, 65.4)
    glVertex2f(-132.5, 72.8)
    glVertex2f(-130, 60)
    glVertex2f(-143, 63.4)
    glVertex2f(-136, 52.7)
    glVertex2f(-149, 47.6)
    glVertex2f(-136, 42.8)
    glVertex2f(-143.9, 32)
    glVertex2f(-131.5, 32.7)
    glVertex2f(-132.8, 21)
    glVertex2f(-121.5, 27.5)
    glVertex2f(-115.8, 15.9)
    glVertex2f(-110.4, 27.5)
    glVertex2f(-100, 20)
    glVertex2f(-102.7, 32.7)
    glVertex2f(-89.6, 32)
    glVertex2f(-97.9, 42.2)
    glVertex2f(-85.8, 46)
    glVertex2f(-97.9, 51)
    glVertex2f(-91.3, 63.2)
    glVertex2f(-103, 60)
    glVertex2f(-100.7, 72.8)
    glVertex2f(-110.4, 65.4)
    glVertex2f(-117.3, 77.8)
    glEnd()
    glPopMatrix()

def virus7():
    global temp_y_virus_7, kecepatan_virus7

    if temp_y_virus_7 <= -500:
        temp_y_virus_7 = 500

    temp_y_virus_7 -= kecepatan_virus7

    glPushMatrix()
    glTranslated(80, temp_y_virus_7, 0)

    glColor3ub(82, 235, 0)
    glBegin(GL_POLYGON)
    glVertex2f(-110.4, 65.4)
    glVertex2f(-117.3, 77.8)
    glVertex2f(-121.5, 65.4)
    glVertex2f(-132.5, 72.8)
    glVertex2f(-130, 60)
    glVertex2f(-143, 63.4)
    glVertex2f(-136, 52.7)
    glVertex2f(-149, 47.6)
    glVertex2f(-136, 42.8)
    glVertex2f(-143.9, 32)
    glVertex2f(-131.5, 32.7)
    glVertex2f(-132.8, 21)
    glVertex2f(-121.5, 27.5)
    glVertex2f(-115.8, 15.9)
    glVertex2f(-110.4, 27.5)
    glVertex2f(-100, 20)
    glVertex2f(-102.7, 32.7)
    glVertex2f(-89.6, 32)
    glVertex2f(-97.9, 42.2)
    glVertex2f(-85.8, 46)
    glVertex2f(-97.9, 51)
    glVertex2f(-91.3, 63.2)
    glVertex2f(-103, 60)
    glVertex2f(-100.7, 72.8)
    glVertex2f(-110.4, 65.4)
    glVertex2f(-117.3, 77.8)
    glEnd()
    glPopMatrix()
    
def virus8():
    global temp_y_virus_8, kecepatan_virus8

    if temp_y_virus_8 <= -500:
        temp_y_virus_8 = 500

    temp_y_virus_8 -= kecepatan_virus8

    glPushMatrix()
    glTranslated(-80, temp_y_virus_8, 0)

    glColor3ub(82, 235, 0)
    glBegin(GL_POLYGON)
    glVertex2f(-110.4, 65.4)
    glVertex2f(-117.3, 77.8)
    glVertex2f(-121.5, 65.4)
    glVertex2f(-132.5, 72.8)
    glVertex2f(-130, 60)
    glVertex2f(-143, 63.4)
    glVertex2f(-136, 52.7)
    glVertex2f(-149, 47.6)
    glVertex2f(-136, 42.8)
    glVertex2f(-143.9, 32)
    glVertex2f(-131.5, 32.7)
    glVertex2f(-132.8, 21)
    glVertex2f(-121.5, 27.5)
    glVertex2f(-115.8, 15.9)
    glVertex2f(-110.4, 27.5)
    glVertex2f(-100, 20)
    glVertex2f(-102.7, 32.7)
    glVertex2f(-89.6, 32)
    glVertex2f(-97.9, 42.2)
    glVertex2f(-85.8, 46)
    glVertex2f(-97.9, 51)
    glVertex2f(-91.3, 63.2)
    glVertex2f(-103, 60)
    glVertex2f(-100.7, 72.8)
    glVertex2f(-110.4, 65.4)
    glVertex2f(-117.3, 77.8)
    glEnd()
    glPopMatrix()

def virus9():
    global temp_y_virus_9, kecepatan_virus9

    if temp_y_virus_9 <= -500:
        temp_y_virus_9 = 500

    temp_y_virus_9 -= kecepatan_virus9

    glPushMatrix()
    glTranslated(380, temp_y_virus_9, 0)

    glColor3ub(82, 235, 0)
    glBegin(GL_POLYGON)
    glVertex2f(-110.4, 65.4)
    glVertex2f(-117.3, 77.8)
    glVertex2f(-121.5, 65.4)
    glVertex2f(-132.5, 72.8)
    glVertex2f(-130, 60)
    glVertex2f(-143, 63.4)
    glVertex2f(-136, 52.7)
    glVertex2f(-149, 47.6)
    glVertex2f(-136, 42.8)
    glVertex2f(-143.9, 32)
    glVertex2f(-131.5, 32.7)
    glVertex2f(-132.8, 21)
    glVertex2f(-121.5, 27.5)
    glVertex2f(-115.8, 15.9)
    glVertex2f(-110.4, 27.5)
    glVertex2f(-100, 20)
    glVertex2f(-102.7, 32.7)
    glVertex2f(-89.6, 32)
    glVertex2f(-97.9, 42.2)
    glVertex2f(-85.8, 46)
    glVertex2f(-97.9, 51)
    glVertex2f(-91.3, 63.2)
    glVertex2f(-103, 60)
    glVertex2f(-100.7, 72.8)
    glVertex2f(-110.4, 65.4)
    glVertex2f(-117.3, 77.8)
    glEnd()
    glPopMatrix()

def virus10():
    global temp_y_virus_10, kecepatan_virus10

    if temp_y_virus_10 <= -500:
        temp_y_virus_10 = 500

    temp_y_virus_10 -= kecepatan_virus10

    glPushMatrix()
    glTranslated(640, temp_y_virus_10, 0)

    glColor3ub(82, 235, 0)
    glBegin(GL_POLYGON)
    glVertex2f(-110.4, 65.4)
    glVertex2f(-117.3, 77.8)
    glVertex2f(-121.5, 65.4)
    glVertex2f(-132.5, 72.8)
    glVertex2f(-130, 60)
    glVertex2f(-143, 63.4)
    glVertex2f(-136, 52.7)
    glVertex2f(-149, 47.6)
    glVertex2f(-136, 42.8)
    glVertex2f(-143.9, 32)
    glVertex2f(-131.5, 32.7)
    glVertex2f(-132.8, 21)
    glVertex2f(-121.5, 27.5)
    glVertex2f(-115.8, 15.9)
    glVertex2f(-110.4, 27.5)
    glVertex2f(-100, 20)
    glVertex2f(-102.7, 32.7)
    glVertex2f(-89.6, 32)
    glVertex2f(-97.9, 42.2)
    glVertex2f(-85.8, 46)
    glVertex2f(-97.9, 51)
    glVertex2f(-91.3, 63.2)
    glVertex2f(-103, 60)
    glVertex2f(-100.7, 72.8)
    glVertex2f(-110.4, 65.4)
    glVertex2f(-117.3, 77.8)
    glEnd()
    glPopMatrix()

def virus11():
    global temp_y_virus_11, kecepatan_virus11

    if temp_y_virus_11 <= -500:
        temp_y_virus_11 = 500

    temp_y_virus_11 -= kecepatan_virus11

    glPushMatrix()
    glTranslated(740, temp_y_virus_11, 0)

    glColor3ub(82, 235, 0)
    glBegin(GL_POLYGON)
    glVertex2f(-110.4, 65.4)
    glVertex2f(-117.3, 77.8)
    glVertex2f(-121.5, 65.4)
    glVertex2f(-132.5, 72.8)
    glVertex2f(-130, 60)
    glVertex2f(-143, 63.4)
    glVertex2f(-136, 52.7)
    glVertex2f(-149, 47.6)
    glVertex2f(-136, 42.8)
    glVertex2f(-143.9, 32)
    glVertex2f(-131.5, 32.7)
    glVertex2f(-132.8, 21)
    glVertex2f(-121.5, 27.5)
    glVertex2f(-115.8, 15.9)
    glVertex2f(-110.4, 27.5)
    glVertex2f(-100, 20)
    glVertex2f(-102.7, 32.7)
    glVertex2f(-89.6, 32)
    glVertex2f(-97.9, 42.2)
    glVertex2f(-85.8, 46)
    glVertex2f(-97.9, 51)
    glVertex2f(-91.3, 63.2)
    glVertex2f(-103, 60)
    glVertex2f(-100.7, 72.8)
    glVertex2f(-110.4, 65.4)
    glVertex2f(-117.3, 77.8)
    glEnd()
    glPopMatrix()

def virus12():
    global temp_y_virus_12, kecepatan_virus12

    if temp_y_virus_12 <= -500:
        temp_y_virus_12 = 500

    temp_y_virus_12 -= kecepatan_virus12

    glPushMatrix()
    glTranslated(25, temp_y_virus_12, 0)

    glColor3ub(82, 235, 0)
    glBegin(GL_POLYGON)
    glVertex2f(-110.4, 65.4)
    glVertex2f(-117.3, 77.8)
    glVertex2f(-121.5, 65.4)
    glVertex2f(-132.5, 72.8)
    glVertex2f(-130, 60)
    glVertex2f(-143, 63.4)
    glVertex2f(-136, 52.7)
    glVertex2f(-149, 47.6)
    glVertex2f(-136, 42.8)
    glVertex2f(-143.9, 32)
    glVertex2f(-131.5, 32.7)
    glVertex2f(-132.8, 21)
    glVertex2f(-121.5, 27.5)
    glVertex2f(-115.8, 15.9)
    glVertex2f(-110.4, 27.5)
    glVertex2f(-100, 20)
    glVertex2f(-102.7, 32.7)
    glVertex2f(-89.6, 32)
    glVertex2f(-97.9, 42.2)
    glVertex2f(-85.8, 46)
    glVertex2f(-97.9, 51)
    glVertex2f(-91.3, 63.2)
    glVertex2f(-103, 60)
    glVertex2f(-100.7, 72.8)
    glVertex2f(-110.4, 65.4)
    glVertex2f(-117.3, 77.8)
    glEnd()
    glPopMatrix()

def virus13():
    global temp_y_virus_13, kecepatan_virus13

    if temp_y_virus_13 <= -500:
        temp_y_virus_13 = 500

    temp_y_virus_13 -= kecepatan_virus13

    glPushMatrix()
    glTranslated(-500, temp_y_virus_13, 0)

    glColor3ub(82, 235, 0)
    glBegin(GL_POLYGON)
    glVertex2f(-110.4, 65.4)
    glVertex2f(-117.3, 77.8)
    glVertex2f(-121.5, 65.4)
    glVertex2f(-132.5, 72.8)
    glVertex2f(-130, 60)
    glVertex2f(-143, 63.4)
    glVertex2f(-136, 52.7)
    glVertex2f(-149, 47.6)
    glVertex2f(-136, 42.8)
    glVertex2f(-143.9, 32)
    glVertex2f(-131.5, 32.7)
    glVertex2f(-132.8, 21)
    glVertex2f(-121.5, 27.5)
    glVertex2f(-115.8, 15.9)
    glVertex2f(-110.4, 27.5)
    glVertex2f(-100, 20)
    glVertex2f(-102.7, 32.7)
    glVertex2f(-89.6, 32)
    glVertex2f(-97.9, 42.2)
    glVertex2f(-85.8, 46)
    glVertex2f(-97.9, 51)
    glVertex2f(-91.3, 63.2)
    glVertex2f(-103, 60)
    glVertex2f(-100.7, 72.8)
    glVertex2f(-110.4, 65.4)
    glVertex2f(-117.3, 77.8)
    glEnd()
    glPopMatrix()

# def bullet():
#     global peluru_y

#     if peluru_y >= 800:
#         peluru_y = 0

#     peluru_y += 10

#     if peluru_y in range(temp_x_virus_1, 300+1):
#         print('Kena')
#         # temp_x_virus_2 = 0
#         # game_over = True

#     glPushMatrix()
#     glTranslated(0, peluru_y, 0)
#     glColor3ub(153, 153, 153)
#     glBegin(GL_POLYGON)
#     glVertex2f(40 + pos_x, -180+10+peluru_y)
#     glVertex2f(50 + pos_x, -180+10+peluru_y)
#     glVertex2f(50 + pos_x, -160+10+peluru_y)
#     glVertex2f(45 + pos_x, -155+10+peluru_y)
#     glVertex2f(40 + pos_x, -160+10+peluru_y)
#     glEnd()
#     glPopMatrix()

def GarisRumput():
    glColor3f(1.0,1.0,1.)
    glBegin(GL_LINES)
    glVertex2f(-720.0, -300.0)
    glVertex2f(720.0, -300.0)
    glEnd()

def Rumput():
    glColor3ub(27, 110, 33)
    glBegin(GL_POLYGON)
    glVertex2f(-720.0, -300.0)
    glVertex2f(720.0, -300.0)
    glVertex2f(720.0, -500.0)
    glVertex2f(-720.0, -500.0)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glPushMatrix()

    gedung()
    player()

    virus1()
    virus2()
    virus3()
    virus4()
    virus5()
    virus6()
    virus7()
    virus8()
    virus9()
    virus10()
    virus11()
    virus12()
    virus13()

    GarisRumput()
    Rumput()

    glPopMatrix()
    glFlush()
    glutSwapBuffers()

def input_mouse(button, state, x, y):
    global hijau, biru, merah
    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        if biru< 1:
            hijau = 0
            biru = 1
            merah = 0
        elif merah < 1:
            hijau = 0
            biru = 0
            merah = 1
            print("Kanan", "(", x, ",", y, ")")
    elif button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        if hijau < 1:
            hijau = 1
            biru = 0
            merah = 0
        else:
            hijau = 0
            biru = 0
            merah = 0
    print("Kiri", "(", x, ",", y, ")")

def input_keyboard(key,x,y):
    global pos_x, pos_y, peluru_y
    if key == GLUT_KEY_RIGHT:
        if pos_x >= 660:
            pos_x += 0
        else:
            pos_x += 15
            print("Kanan", "x : ", pos_x, " y : ", pos_y)
    elif key == GLUT_KEY_LEFT:
        if key == GLUT_KEY_LEFT:
            if pos_x <= -660:
                pos_x -= 0  
            else:
                pos_x -= 15
                print("Kanan", "x : ", pos_x, " y : ", pos_y)

def update(value):
    glutPostRedisplay()
    glutTimerFunc(10,update,0)
    
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(720, 500)
    glutInitWindowPosition(100,100)
    glutCreateWindow("Vaccines vs Covid")
    glutDisplayFunc(display)
    glutSpecialFunc(input_keyboard)
    glutMouseFunc(input_mouse)
    glutTimerFunc(50, update, 0)
    init()
    glutMainLoop()
  
main()
