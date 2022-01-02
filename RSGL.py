from Xlib import X, display, Xutil, threaded
import os

def RSGLRGBTOHEX(r, g, b): return ((r << 16) + (g << 8) + b)

KeyPressed=2 # a key has been pressed
KeyReleased=3 # a key has been released
MouseButtonPressed=4 # a mouse button has been pressed (left,middle,right)
MouseButtonReleased=5 # a mouse button has been released (left,middle,right)
MousePosChanged=6 # the position of the mouse has been changed
quit = 33 # the user clicked the quit button
dnd = 34 # a file has been dropped into the window

class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

class rect:
    def __init__(self,x,y,width,length):
        self.x=x
        self.y=y
        self.width=width
        self.length=length

class circle:
    def __init__(self,x,y,radius):
        self.x=x
        self.y=y
        self.radius=radius

class area:
    def __init__(self,width,length):
        self.width=width
        self.length=length

class color:
    def __init__(self,r,g,b,a=100):
        self.r=r
        self.g=g
        self.b=b
        self.a=a

class drawable:
    def __init__(self,r,display,d,color):
        self.r = r
        self.display = display
        self.d = None
        self.color = color
    def loadArea(self,dsrc,r,p):
        self.r = r
        self.display = display
        self.d = dsrc.d
        self.color = color
        pass

class pixmap:
    def __init__(self,dr,a):
        pass
    
class window:
    class Event:
        def __init__(self):
            self.type = None
            self.button = None
            self.x, self.y = None, None
            self.keycode = None
            self.key = None
            self.ledState = None

    def __init__(self,name,rect,color,resize=False):
        self.event = self.Event()
        self.r = rect
        self.display = display.Display()
        self.color = color
        self.d = XCreateSimpleWindow(display, parent, winrect.x,winrect.y,winrect.width,winrect.length, 0,0,  RSGLRGBTOHEX(c.r,c.g,c.b))
        self.dbuffer = pixmap(self.d,(rect.length,rect.width))
        self.keyboard = []
    def checkEvents(self):
        pass
    def isPressed(self, key):
        pass
    def close(self):
        self.display.close()
    def clear(self):
        pass

root = None

def CircleCollidePoint(c,p):
    pass
def CircleCollideRect(c, r):
    pass
def CircleCollide(cir1,cir2):
    pass
def RectCollidePoint(r, p):
    pass
def RectCollideRect(r, r2):
    pass
def PointCollide(p, p2):
    pass

class Text:
    def __init__(self,rect,c,text,f,d=root,draw=True):
        self.rect = rect
        self.c = c
        self.text = text
        self.f = f
        self.d=d
    
def drawText(text, font, c,d=root):
    pass
    
def drawPoint( p,  c, win=root):
    pass
    
def drawRect(r,c,fill=True,win=root):
    pass
    
def drawLine(p1,p2, c,width=1):
    pass
    
def drawCircle(c,col,fill=True):
    pass
    
def drawImage(fileName, r, resize=True, d=root):
    pass
    
def resizeImage(image,newSize,ogsize):
    pass
    
def fileDialog(title,multiple=False,save=False,directory=False):
    pass
    
def notifiy(title, content ,image=""):
    pass
    
def messageBox(message,question=False,error=False):
    pass

