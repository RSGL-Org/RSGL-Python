import RSGL

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

