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

def virus():
    global virus_x
    glColor3ub(0, 255, 8)
    glBegin(GL_POLYGON)
    glVertex2f(-700 + virus_x, 300)
    glVertex2f(-650 + virus_x, 300)
    glVertex2f(-650 + virus_x, 250)
    glVertex2f(-700 + virus_x, 250)
    glEnd()

class Dokter:
    def kotak():
        global pos_x, pos_y
        glColor3ub(186, 142, 84)
        glBegin(GL_POLYGON)
        glVertex2f(-50 + pos_x, -300 + pos_y)
        glVertex2f(50 + pos_x, -300 + pos_y)
        glVertex2f(50 + pos_x, -250 + pos_y)
        glVertex2f(-50 + pos_x, -250 + pos_y)
        glEnd()

class Virus:
    def badan():
        global pos_x, pos_y
        glColor3ub(48, 48, 48)
        glBegin(GL_POLYGON)
        # Kiri Atas
        glVertex2f(-50 + pos_x,0 + pos_y)
        # Kanan Atas
        glVertex2f(-100 + pos_x,40 + pos_y)
        # Kanan Bawah
        glVertex2f(-100 + pos_x,50 + pos_y)
        # Kiri Bawah
        glVertex2f(100 + pos_x,50 + pos_y)
        glVertex2f(100 + pos_x,40 + pos_y)
        glVertex2f(50 + pos_x,0 + pos_y)
        glEnd()

    def badanBawah():
        global pos_x, pos_y
        glColor3ub(148, 0, 0)
        glBegin(GL_POLYGON)
        glVertex2f(-60 + pos_x, 8 + pos_y)
        glVertex2f(60 + pos_x, 8 + pos_y)
        glVertex2f(50 + pos_x, 0 + pos_y)
        glVertex2f(-50 + pos_x, 0 + pos_y)
        glEnd()

    def tiangBendera():
        global pos_x, pos_y
        glColor3ub(48, 48, 48)
        glBegin(GL_POLYGON)
        glVertex2f(-5 + pos_x, 50 + pos_y)
        glVertex2f(5 + pos_x, 50 + pos_y)
        glVertex2f(5 + pos_x, 90 + pos_y)
        glVertex2f(-5 + pos_x, 90 + pos_y)
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
    Dokter.kotak()
    # Kapal.badan()
    # Kapal.tiangBendera()
    # Kapal.badanBawah()
    GarisRumput()
    Rumput()
    virus()
    glPopMatrix()
    glFlush()

def input_mouse(button, state, x, y):
    global hijau, biru, merah
    # Saat mengklik kanan warna kapal akan berubah menjadi warna biru dan merah
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
        # Saat mengklik kiri warna kapal akan berubah menjadi warna hijau dan hitam
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
    # Untuk mengubah posisi kapal
    # if key == GLUT_KEY_UP:
    #     pos_y += 5
    #     print("Tombol Atas ditekan ", "x : ", pos_x, " y : ", pos_y)
    # elif key == GLUT_KEY_DOWN:
    #     pos_y -= 5
    #     print("Tombol Bawah ditekan ", "x : ", pos_x, " y : ", pos_y)
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
    if pos_x < 0 and pos_y > 0:
        glClearColor(0.0, 1.0, 0.0, 1.0)
    if pos_x > 0 and pos_y > 0:
        glClearColor(0.0,0.0,1.0,1.0)
    if pos_x > 0 and pos_y < 0:
        glClearColor(1.0, 0.0, 0.0, 1.0)
    if pos_x < 0 and pos_y < 0:
        glClearColor(0.0,0.0,0.0,1.0)

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
