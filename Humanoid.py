#Generate Humanoid using heirarchical modelling
#Made By:- Vandit Sheth

import random
import time
from sys import exit
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

#Values that are used in the code and can change are declared
rotate = [0.0, 90.0, 0.0, 90.0, 0.0, 180.0, 0.0, 180.0, 0.0]
temp = [0.0, 0.0, 0.0, 0.0]
depth = 0
up = 0
m=0.0
n=0.0
dance=0
handshake=0

def display():
  global depth, handshake

  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

  #Setting up the screen view.
  glMatrixMode(GL_PROJECTION)
  glLoadIdentity()
  gluPerspective(20, 1.0, 1.0, 200.0)

  glMatrixMode(GL_MODELVIEW)
  
  glLoadIdentity()
  gluLookAt(0.0 , 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
  glTranslatef(0.0, up, depth)
  glColor3f(0.0, 0.0, 1.0)
  #Calling the function to make robot
  glPushMatrix()
  robot()
  glPopMatrix()

def robot():
  global depth
  #Fragement for generating body. It can rotate wrt head(rotate[0]) as well as wrt screen(m and n)
  glRotatef(rotate[0], 0.0, 1.0, 0.0)
  glRotatef(m, 1.0, 0.0, 0.0)
  glRotatef(n, 0.0, 0.0, 1.0)
  glPushMatrix();
  glColor3f(0.5, 0.5, 0.5)
  glTranslatef(0.0, 0.2, 0.0)
  glScalef(0.2, 0.4, 0.15)
  glutSolidCube(1.0)
  glPopMatrix();

  #Fragement for generating head. The head is stationary under all conditions
  glPushMatrix();
  glColor3f(0.5, 0.5, 0.5)
  glTranslatef(0.0, 0.49 , 0.0)
  glutSolidSphere(0.09, 100, 100)
  glPopMatrix();
  
  #Fragement for generating Left Upper Arm. It can be rotated around the body as well as around its axis.
  glPushMatrix()
  glColor3f(0.0, 0.0, 1.0)
  glTranslatef(-0.125, 0.39, 0.0)
  glRotatef(rotate[1], 1.0, 0.0, 0.0)
  glRotatef(temp[0], 0.0, 1.0, 0.0)
  glPushMatrix()
  glTranslatef(0.0, 0.1, 0.0)
  glScalef(0.05, 0.2, 0.05)
  glutSolidCube(1.0)
  glPopMatrix()

  #Fragement for generating Left Lower Arm. It can be rotated wrt upper arm.
  glColor3f(1.0, 1.0, 0.0)
  glTranslatef(0.0, 0.2, 0.0)
  glRotatef(rotate[2], 1.0, 0.0, 0.0)
  glPushMatrix()
  glTranslatef(0.0, 0.1, 0.0)
  glScalef(0.05, 0.2, 0.05)
  glutSolidCube(1.0)
  glPopMatrix()
  glPopMatrix()

  #Fragement for generating Right Upper Arm. It can be rotated wrt body as well as on its axis.
  glPushMatrix()
  glColor3f(0.0, 0.0, 1.0)
  glTranslatef(0.125, 0.39, 0.0)
  glRotatef(rotate[3], 1.0, 0.0, 0.0)
  glRotatef(temp[1], 0.0, 1.0, 0.0)
  glPushMatrix()
  glTranslatef(0.0, 0.1, 0.0)
  glScalef(0.05, 0.2, 0.05)
  glutSolidCube(1.0)
  glPopMatrix()

  #Fragement for generating Right Lower Arm. It can be rotated wrt upper arm.
  glColor3f(1.0, 1.0, 0.0)
  glTranslatef(0.0, 0.2, 0.0)
  glRotatef(rotate[4], 1.0, 0.0, 0.0)
  glPushMatrix()
  glTranslatef(0.0, 0.1, 0.0)
  glScalef(0.05, 0.2, 0.05)
  glutSolidCube(1.0)
  glPopMatrix()
  glPopMatrix()

  #Fragement for generating Left Upper Leg. It can be rotated wrt body as well as on its axis.
  glPushMatrix()
  glColor3f(1.0, 0.0, 0.0)
  glTranslatef(-0.06, 0.0, 0.0)
  glRotatef(rotate[5], 1.0, 0.0, 0.0)
  glRotatef(temp[2], 0.0, 1.0, 0.0)
  glPushMatrix()
  glTranslatef(0.0, 0.1, 0.0)
  glScalef(0.08, 0.2, 0.07)
  glutSolidCube(1.0)
  glPopMatrix()

  #Fragement for generating Left Lower Leg. It can be rotated wrt upper leg.
  glColor3f(0.0, 1.0, 1.0)
  glTranslatef(0.0, 0.2, 0.0)
  glRotatef(rotate[6], 1.0, 0.0, 0.0)
  glPushMatrix()
  glTranslatef(0.0, 0.1, 0.0)
  glScalef(0.08, 0.2, 0.07)
  glutSolidCube(1.0)
  glPopMatrix()
  glPopMatrix()
  
  #Fragement for generating Right Upper Leg. It can be rotated wrt body as well as on its axis.
  glPushMatrix()
  glColor3f(1.0, 0.0, 0.0)
  glTranslatef(0.06, 0.0, 0.0)
  glRotatef(rotate[7], 1.0, 0.0, 0.0)
  glRotatef(temp[3], 0.0, 1.0, 0.0)
  glPushMatrix()
  glTranslatef(0.0, 0.1, 0.0)
  glScalef(0.08, 0.2, 0.07)
  glutSolidCube(1.0)
  glPopMatrix()

  #Fragement for generating Right Lower Leg. It can be rotated wrt upper leg.
  glColor3f(0.0, 1.0, 1.0)
  glTranslatef(0.0, 0.2, 0.0)
  glRotatef(rotate[8], 1.0, 0.0, 0.0)
  glPushMatrix()
  glTranslatef(0.0, 0.1, 0.0)
  glScalef(0.08, 0.2, 0.07)
  glutSolidCube(1.0)
  glPopMatrix()
  glPopMatrix()
  
  glFlush()
  
def keyboard(key, x, y):
  global rotate, depth, up, temp, m, n, dance, handshake

  if handshake==0 and dance==0:
    #Body rotation around head
    if key=='w':
      rotate[0] = rotate[0] + 10.0

    elif key=='W':
      rotate[0] = rotate[0] - 10.0

    #Left Upper Arm rotation around body
    elif key=='a':
      rotate[1] = rotate[1] + 10.0

    elif key=='A':
      rotate[1] = rotate[1] - 10.0

    #Left Lower Arm rotation around upper arm
    elif key=='s':
      rotate[2] = rotate[2] + 10.0

    elif key=='S':
      rotate[2] = rotate[2] - 10.0

    #Right Upper Arm rotation around body
    elif key=='d':
      rotate[3] = rotate[3] + 10.0

    elif key=='D':
      rotate[3] = rotate[3] - 10.0

    #Right Lower Arm rotation around upper arm
    elif key=='f':
      rotate[4] = rotate[4] + 10.0
      
    elif key=='F':
      rotate[4] = rotate[4] -10.0
      
    #Left Upper Leg rotation around body
    elif key=='z':
      rotate[5] = rotate[5] + 10.0

    elif key=='Z':
      rotate[5] = rotate[5] - 10.0

    #Left Lower Leg rotation around upper leg    
    elif key=='x':
      rotate[6] = rotate[6] + 10.0
      
    elif key=='X':
      rotate[6] = rotate[6] -10.0

    #Left Upper Leg rotation around body    
    elif key=='c':
      rotate[7] = rotate[7] + 10.0
      
    elif key=='C':
      rotate[7] = rotate[7] - 10.0

    #Right Lower Leg rotation around upper leg    
    elif key=='v':
      rotate[8] = rotate[8] + 10.0
      
    elif key=='V':
      rotate[8] = rotate[8] - 10.0

    #Left arm rotation around its axis
    elif key=='u':
      temp[0] = temp[0] + 10.0

    elif key=='U':
      temp[0] = temp[0] - 10.0

    #Right arm rotation around its axis
    elif key=='i':
      temp[1] = temp[1] + 10.0

    elif key=='I':
      temp[1] = temp[1] - 10.0

    #Left leg rotation around its axis
    elif key=='o':
      temp[2] = temp[2] + 10.0

    elif key=='O':
      temp[2] = temp[2] - 10.0

    #Right leg rotation around its axis
    elif key=='p':
      temp[3] = temp[3] + 10.0

    elif key=='P':
      temp[3] = temp[3] - 10.0

    #Humanoid rotation wrt screen
    elif key=='m':
      m = m + 10.0

    elif key=='M':
      m = m - 10.0

    #Humanoid rotation wrt screen
    elif key=='n':
      n = n + 10.0

    elif key=='N':
      n = n - 10.0

    #Humanoid depth wrt screen
    elif key=='e':
      depth += 1.0

    elif key=='E':
      depth -= 1.0

    #Humanoid going up wrt screen
    elif key=='r':
      up += 0.2

    elif key=='R':
      up -= 0.2

  #Reset the humanoid
  if key=='q':
    rotate = [0.0, 90.0, 0.0, 90.0, 0.0, 180.0, 0.0, 180.0, 0.0]
    temp = [0.0, 0.0, 0.0, 0.0]
    depth = 0
    up = 0
    m=0.0
    n=0.0
    handshake=0
    dance=0

  #Initiate dance (only if handshake is not going on)
  elif key=='j' and handshake==0:
    rotate = [0.0, 90.0, 0.0, 90.0, 0.0, 180.0, 0.0, 180.0, 0.0]
    temp = [0.0, 0.0, 0.0, 0.0]
    depth = 0
    up = 0
    m=0.0
    n=0.0
    dance=1

  #Stop Dance
  elif key=='J':
    dance=0

  #Initiate handshake (only if dance is not going on)
  elif key=='k' and dance==0:
    rotate = [0.0, 90.0, 0.0, 90.0, 0.0, 180.0, 0.0, 180.0, 0.0]
    temp = [0.0, 0.0, 0.0, 0.0]
    depth = 0
    up = 0
    m=0.0
    n=0.0
    handshake=1

  #Stop Handshake
  elif key=='K':
    handshake=0

  #To Quit using Esc
  elif key==chr(27):
    sys.exit()

  glutPostRedisplay()

#Timer Function to keep the dance and handshake ON till key press
def TimerFunc(value):
  global dance, rotate
  
  #Random dance moves by randomizing rotate values
  if dance==1:
    rotate = random.sample(range(360),9)

  #Intiate hanshake algorithm
  if handshake==1:
    #Rotate body
    if rotate[0]<90.0:
      rotate[0]=rotate[0]+30.0
    #Bring arms to side
    elif rotate[3]>=90.0 and rotate[3]<180.0 and rotate[4]<180:
      rotate[3]=rotate[3]+18.0
      rotate[1]=rotate[1]+18.0
    #Hand up for handshake
    elif rotate[4]>-108:
      rotate[4]=rotate[4]-18.0
    #Hand down for handshake
    else:
      rotate[4]=rotate[4]+18.0
  glutPostRedisplay()
  glutTimerFunc(500,TimerFunc,1)  

glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0,0)
glutCreateWindow('Humanoid')
glutTimerFunc(500,TimerFunc,1)
glutDisplayFunc(display)
glutKeyboardFunc(keyboard)

glClearColor(0.0, 0.0, 0.0, 0.0)
glutMainLoop()
