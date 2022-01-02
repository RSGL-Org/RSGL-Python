import RSGL
running = True
window = RSGL.window("",RSGL.rect(500,500,500,500),RSGL.color(0,0,0))

while (running):
    window.checkEvents() 
    window.clear()
    if (window.event.type == RSGL.quit): running=False
    RSGL.drawRect(RSGL.rect(100,100,400,400),RSGL.color(255,0,0),False)
window.close()