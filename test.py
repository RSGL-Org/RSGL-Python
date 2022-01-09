import RSGL
running = True
window = RSGL.window("name",[500,500,500,500],[255,255,255])
window2 = RSGL.window("name2",[500,500,500,500],[255,255,255])
while (running):
    window.checkEvents() 
    window2.checkEvents()     
    if (window.event.type == RSGL.quit or window2.event.type == RSGL.quit): running=False
    RSGL.drawRect([200,200,200,200],[255,0,0])
    RSGL.drawRect([100,100,200,200],[0,255,0],d=window2)
window.close()