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
        self.screen = self.display.screen()
        self.d = self.screen.root.create_window(rect.x,rect.y,rect.width,rect.length,2,self.screen.root_depth,X.InputOutput,X.CopyFromParent,
        background_pixel = self.screen.white_pixel,
        event_mask = (X.ExposureMask | X.StructureNotifyMask | X.ButtonPressMask | X.ButtonReleaseMask | X.Button1MotionMask),
        colormap = X.CopyFromParent)
        self.WM_DELETE_WINDOW = self.display.intern_atom('WM_DELETE_WINDOW')
        self.WM_PROTOCOLS = self.display.intern_atom('WM_PROTOCOLS')

        self.d.set_wm_name(name)
        self.d.set_wm_icon_name(name)

        self.d.set_wm_protocols([self.WM_DELETE_WINDOW])
        self.d.set_wm_hints(flags = Xutil.StateHint,
                                 initial_state = Xutil.NormalState)

        self.d.set_wm_normal_hints(flags = (Xutil.PPosition | Xutil.PSize
                                                 | Xutil.PMinSize),
                                        min_width = 20,
                                        min_height = 20)

        self.d.map()
        self.dbuffer = pixmap(self.d,(rect.length,rect.width))
        self.keyboard = []
    def checkEvents(self):
        E = self.display.next_event()
        self.event.type = E.type
        if (self.event.type == 33 and E.xclient.data.l[0] == XInternAtom(display, "WM_DELETE_WINDOW", true)):
            pass 
        elif (self.event.type == 33 and E.xclient.message_type == XInternAtom(display, "XdndDrop", false)): self.event.type=34 
        elif (self.event.type==33): self.event.type = 0
        if (self.event.type == 4 or self.event.type == 5): self.event.button = E.xbutton.button
        if (self.event.type == 4 or self.event.type == 5 or self.event.type == 6):
            self.event.x=E.xbutton.x 
            self.event.y=E.xbutton.y
        if (self.event.type == 2 or self.event.type == 3):
            XQueryKeymap(display,keyboard)
        if (self.event.type == 2 or self.event.type == 3):
             self.event.keycode = XKeycodeToKeysym(display,E.xkey.keycode,1); 
             self.event.key=XKeysymToString(event.keycode)
        else:
            self.event.keycode = 0 
            self.event.key=""
        #XKeyboardState keystate
        #XGetKeyboardControl(display,&keystate)
        #event.ledState= keystate.led_mask

    def isPressed(self, key):
        pass
    def close(self):
        XDestroyWindow(self.display, self.d)
        self.display.close()
    def clear(self):
        #XClearWindow(self.display,self.d)
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
    com = "notify-send \"" + title +"\" \"" + content + "\" "
    if (image != ""):  com += "-i \"" + image + "\""
    os.system(com)

def messageBox(message,question=False,error=False):
    com = "zenity "
    if (question): com+="--question "
    elif (error): com+= "--error "
    else: com+="--warning "
    com += "--text \"" + message + "\""
    os.system(com)

