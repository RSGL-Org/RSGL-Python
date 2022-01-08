import RSGL
running = True
window = RSGL.window("name",[500,500,500,500],[255,255,255])

while (running):
    window.checkEvents() 
    #window.clear()
    if (window.event.type == RSGL.quit): running=False
    RSGL.drawRect([100,100,400,400],[255,0,0])
window.close()