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
        print(type(self.d))
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
        if (self.event.type == 33 and E.client_type == self.WM_PROTOCOLS):
            fmt, data = E.data
            if fmt == 32 and data[0] == self.WM_DELETE_WINDOW: pass 
        #elif (self.event.type == 33 and E.xclient.message_type == XInternAtom(display, "XdndDrop", false)): self.event.type=34 
        elif (self.event.type==33): self.event.type = 0
        if (self.event.type == 4 or self.event.type == 5): self.event.button = E.detail
        if (self.event.type == 4 or self.event.type == 5 or self.event.type == 6):
            self.event.x=E.root_x 
            self.event.y=E.root_y

        if (self.event.type == 2 or self.event.type == 3):
             self.event.keycode = XKeycodeToKeysym(display,E.xkey.keycode,1); 
             self.event.key=XKeysymToString(event.keycode)
        else:
            self.event.keycode = 0 
            self.event.key=""

    def isPressed(self, key):
        pass
    def close(self):
        self.display.close()
    def clear(self):
        #XClearWindow(self.display,self.d)
        pass

root = None

def CircleCollidePoint(c,p):
    testX, testY = c.x, c.y
    if (c.x < p.x):testX = p.x  
    elif (c.x > p.x+1): testX = p.x+1
    if (c.y < p.y): testY = p.y
    elif (c.y > p.y+1): testY = p.y+1 
  	return sqrt(((c.x-testX)*(c.x-testX))+((c.y-testY)*(c.y-testY))) <= c.radius
def CircleCollideRect(c, r):
    testX, testY = c.x, c.y

    if (c.x < r.x): testX = r.x  
    elif (c.x > r.x+r.width): testX = r.x+r.width
    if (c.y < r.y): testY = r.y 
    elif (c.y > r.y+r.length): testY = r.y+r.length 
  
    return (sqrt( ( (c.x-testX) * (c.x-testX) ) + ( (c.y-testY) *(c.y-testY) ) )  <= c.radius)
    
def CircleCollide(cir1,cir2):
    distanceBetweenCircles = sqrt(
	    (cir2.x - cir.x) * (cir2.x - cir.x) + 
        (cir2.y - cir.y) * (cir2.y - cir.y))
    if (distanceBetweenCircles > cir.radius + cir2.radius): 
        return 0 
    return 1
def RectCollidePoint(r, p):
    if (p.x >= r.x and  p.x <= r.x + r.width and p.y >= r.y and p.y <= r.y + r.length): return 1
    return 0
def RectCollideRect(r, r2):
    if(r.x + r.width >= r2.x and r.x <= r2.x + r2.width and r.y + r.length >= r2.y and r.y <= r2.y + r2.length): return 1
    return 0
def PointCollide(p, p2):
    if (p.x == p2.x and p.y == p2.y): return 1
    return 0

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
    RSGL.drawRect(RSGL.rect(p.x,p.y,1,1),RSGL.color(c.r,c.g,c.b),False)

def drawLine(p1,p2, c,width=1):
    passa

def drawRect(r,c,fill=True,win=root):
    XSetForeground(win.display,XDefaultGC(win.display,XDefaultScreen(win.display)),
    RSGLRGBTOHEX(c.r,c.g,c.b))
    if (fill):
        r = root.display.screen().root
        gc = r.create_gc()
        r.fill_rectangle(gc, 100, 100, 500, 500)
    else{
        RSGL::drawLine({r.x,r.y},{r.x,r.y+r.length},c);
        RSGL::drawLine({r.x+r.width,r.y},{r.x+r.width,r.y+r.length},c);
        RSGL::drawLine({r.x,r.x},{r.x+r.width,r.y},c);
        RSGL::drawLine({r.x,r.y+r.length},{r.x+r.width,r.y+r.length},c);
      }
     
    
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

