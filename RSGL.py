from Xlib import X, display, Xutil, threaded
import os
from PIL import Image

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
    def initList(self,l):
        args=2
        if (type(l) != list): return l
        for i in range(args): 
            if(len(l) < i+1): l.insert(i+1,None)
        return point(l[0],l[1])


class rect:
    def __init__(self,x,y,width,length):
        self.x=x
        self.y=y
        self.width=width
        self.length=length
    def initList(self,l):
        args=4
        if (type(l) != list): return l
        for i in range(args): 
            if(len(l) < i+1): l.insert(i+1,None)
        return rect(l[0],l[1],l[2],l[3])


class circle:
    def __init__(self,x,y,radius):
        self.x=x
        self.y=y
        self.radius=radius
    def initList(self,l):
        args=3
        if (type(l) != list): return l
        for i in range(args): 
            if(len(l) < i+1): l.insert(i+1,None)
        return circle(l[0],l[1],l[2])

class area:
    def __init__(self,width,length):
        self.width=width
        self.length=length
    def initList(self,l):
        args=2
        if (type(l) != list): return l
        for i in range(args): 
            if(len(l) < i+1): l.insert(i+1,None)
        return area(l[0],l[1])


class color:
    def __init__(self,r,g,b,a=100):
        self.r=r
        self.g=g
        self.b=b
        self.a=a
    def initList(self,l):
        args=4
        if (type(l) != list): return l
        for i in range(args): 
            if(len(l) < i+1): l.insert(i+1,None)
        return color(l[0],l[1],l[2],l[3])


class drawable:
    def __init__(self,r,display,d,color):
        self.r = r
        self.display = display
        self.d = None
        self.color = color
    def initList(self,l):
        args=4
        if (type(l) != list): return l
        for i in range(args): 
            if(len(l) < i+1): l.insert(i+1,None)
        return drawable(l[0],l[1],l[2],l[3])

    def loadArea(self,dsrc,r,p):
        self.r = r
        self.display = display
        self.d = dsrc.d
        self.color = color
        pass

class pixmap:
    def __init__(self,dr,a):
        pass
    
root = None

class window:
    class Event:
        def __init__(self):
            self.type = None
            self.button = None
            self.x, self.y = None, None
            self.keycode = None
            self.key = None
            self.ledState = None

    def __init__(self,name,Rect,Color,resize=False):
        Rect = rect.initList(None,Rect)
        Color = color.initList(None,Color)
        self.event = self.Event()
        self.r = Rect
        self.display = display.Display()
        self.color = Color
        self.screen = self.display.screen()
        self.d = self.screen.root.create_window(Rect.x,Rect.y,Rect.width,Rect.length,2,self.screen.root_depth,X.InputOutput,X.CopyFromParent,
        background_pixel = RSGLRGBTOHEX(Color.r,Color.g,Color.b),
        foreground_pixel = RSGLRGBTOHEX(0,0,0),
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
        self.dbuffer = pixmap(self.d,(Rect.length,Rect.width))
        self.keyboard = []
        global root
        if (root==None): root=self
    
    def initList(self,l):
        args=4
        if (type(l) != list): return l
        for i in range(args): 
            if(len(l) < i+1): l.insert(i+1,None)
        return window(l[0],l[1],l[2],l[3])
    
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
        self.d.clear_area()

def CircleCollidePoint(c,p):
    c = circle.initList(None,c)
    p = point.initList(None,p)
    testX, testY = c.x, c.y
    if (c.x < p.x):testX = p.x  
    elif (c.x > p.x+1): testX = p.x+1
    if (c.y < p.y): testY = p.y
    elif (c.y > p.y+1): testY = p.y+1
    return sqrt(((c.x-testX)*(c.x-testX))+((c.y-testY)*(c.y-testY))) <= c.radius
def CircleCollideRect(c, r):
    c = circle.initList(None,c)
    r = rect.initList(None,r)
    testX, testY = c.x, c.y

    if (c.x < r.x): testX = r.x  
    elif (c.x > r.x+r.width): testX = r.x+r.width
    if (c.y < r.y): testY = r.y 
    elif (c.y > r.y+r.length): testY = r.y+r.length 
  
    return (sqrt( ( (c.x-testX) * (c.x-testX) ) + ( (c.y-testY) *(c.y-testY) ) )  <= c.radius)
    
def CircleCollide(c1,c2):
    c1 = circle.initList(None,c1)
    c2 = circle.initList(None,c2)
    distanceBetweenCircles = sqrt(
	    (cir2.x - cir.x) * (cir2.x - cir.x) + 
        (cir2.y - cir.y) * (cir2.y - cir.y))
    if (distanceBetweenCircles > cir.radius + cir2.radius): 
        return 0 
    return 1
def RectCollidePoint(r, p):
    r = rect.initList(None,r)
    p = point.initList(None,p)
    if (p.x >= r.x and  p.x <= r.x + r.width and p.y >= r.y and p.y <= r.y + r.length): return 1
    return 0
def RectCollideRect(r, r2):
    r1 = rect.initList(None,r1)
    r2 = rect.initList(None,r2)
    if(r.x + r.width >= r2.x and r.x <= r2.x + r2.width and r.y + r.length >= r2.y and r.y <= r2.y + r2.length): return 1
    return 0
def PointCollide(p, p2):
    p1 = point.initList(None,p1)
    p2 = point.initList(None,p2)
    if (p.x == p2.x and p.y == p2.y): return 1
    return 0

class Text:
    def __init__(self,rect,c,text,f,d=root,draw=True):
        self.rect = rect
        self.c = c
        self.text = text
        self.f = f
        self.d=d
    def initList(self,l):
        args=6
        if (type(l) != list): return l
        for i in range(args): 
            if(len(l) < i+1): l.insert(i+1,None)
        return Text(l[0],l[1],l[2],l[3],l[4],l[5])
    
def drawText(text, font, c,d=root):
    c = circle.initList(None,c)
    col = color.initList(None,col)

def drawLine(p1,p2, c,width=1):
    p1 = point.initList(None,p1)
    p2 = point.initList(None,p2)
    c = color.initList(None,c)

def drawRect(r,c,fill=True,d=root):
    if (d == None and root != None): d=root
    r = rect.initList(None,r)
    c = color.initList(None,c)
    gc = d.d.create_gc(foreground =RSGLRGBTOHEX(c.r,c.g,c.b))
    if (fill):
        d.d.fill_rectangle(gc,r.x,r.y,r.width,r.length)
        d.display.flush()
    else:
        drawLine([r.x,r.y],[r.x,r.y+r.length],c)
        drawLine([r.x+r.width,r.y],[r.x+r.width,r.y+r.length],c)
        drawLine([r.x,r.x],[r.x+r.width,r.y],c)
        drawLine([r.x,r.y+r.length],[r.x+r.width,r.y+r.length],c)
     
def drawPoint( p,  c, win=root):
    p = point.initList(None,p)
    c = color.initList(None,c)
    RSGL.drawRect(RSGL.rect(p.x,p.y,1,1),RSGL.color(c.r,c.g,c.b),False)

def drawCircle(c,col,fill=True, win=root):
    if (win == None and root != None): win=root
    c = circle.initList(None,c)
    col = color.initList(None,col)
    gc = win.d.create_gc(foreground =RSGLRGBTOHEX(col.r,col.g,col.b))
    if (fill):
        # gc, x, y, width, height, angle1, angle2
        win.d.fill_arc(gc,int(c.x-(30/2)),int(c.y-(30/2)), int(c.radius), int(c.radius), 0, 360*64)
        d.display.flush()
    else:
        win.d.arc(gc,int(c.x-(30/2)),int(c.y-(30/2)), int(c.radius), int(c.radius), 0, 360*64)
        d.display.flush()

def drawImage(fileName, r, resize=True, d=root):
    r = rect.initList(None,r)
    im = Image.open(fileName)
    for y in range(im.height):
        for x in range(im.width):
            drawRect([r.x+x,r.y+y,1,1],[im.__array__()[y][x][0],im.__array__()[y][x][1],im.__array__()[y][x][2]])
    
def resizeImage(image,a):
    a = area.initList(None,a)
    
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

