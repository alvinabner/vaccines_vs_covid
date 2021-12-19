from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
# Koordinat x dan y untuk posisi kapal
pos_x = 0
pos_y = 0
# Warna Kotak
hijau = 0
biru = 0
merah = 0
virus_x = 0

temp_x = -720
temp_y = 250

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

class Virus:
    def virus():
        global virus_x
        glColor3ub(0, 255, 8)
        glBegin(GL_POLYGON)
        glVertex2f(-700 + virus_x, 300)
        glVertex2f(-650 + virus_x, 300)
        glVertex2f(-650 + virus_x, 250)
        glVertex2f(-700 + virus_x, 250)
        glEnd()

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
    # Dokter.kotak()
    player()
    virus()
    Virus.virus()
    GarisRumput()
    Rumput()
    glPopMatrix()
    glFlush()

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
    global pos_x, pos_y
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
