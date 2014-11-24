import bge
import colours

cont = bge.logic.getCurrentController()
scene = bge.logic.getCurrentScene()

p1 = scene.objects['Selector_1']
p2 = scene.objects['Selector_2']
xC = 1
yC = 1
x = p1.worldPosition.x
y = p1.worldPosition.z
xC2 = 1
yC2 = 1
x2 = p2.worldPosition.x
y2 = p2.worldPosition.z
dc = "Color_White"
dc2 = "Color_White"
def p1f():
    global xC
    global yC
    global x
    global y
    global dc
    key = p1.sensors['Keyboard'].events
    if key ==[[100,1]]:
        if xC < 4:
            nX = x + 1.42056
            p1.worldPosition.x = nX
            x = p1.worldPosition.x
            xC = xC + 1
    elif key ==[[97,1]]:
        if xC > 1:
            nX = x - 1.42056
            p1.worldPosition.x = nX 
            x = p1.worldPosition.x
            xC = xC - 1
    elif key ==[[119,1]]:
        if yC > 1:
            nY = y + 1.42056
            p1.worldPosition.z = nY
            y = p1.worldPosition.z
            yC = yC - 1
    elif key ==[[115,1]]:
        if yC < 4:
            nY = y - 1.42056
            p1.worldPosition.z = nY
            y = p1.worldPosition.z
            yC = yC + 1
    else:
        pass
    nc = colours.colour[xC - 1][yC - 1]
    scene.objects['Suzanne_1'].replaceMesh('Suzanne_' + nc, True, False)
    dc = nc
def p2f():
    global xC2
    global yC2
    global x2
    global y2
    global dc2
    key2 = p2.sensors['Keyboard'].events
    if key2 ==[[145,1]]:
        if xC2 < 4:
            nX2 = x2 + 1.42056
            p2.worldPosition.x = nX2
            x2 = p2.worldPosition.x
            xC2 = xC2 + 1
    elif key2 ==[[143,1]]:
        if xC2 > 1:
            nX2 = x2 - 1.42056
            p2.worldPosition.x = nX2 
            x2 = p2.worldPosition.x
            xC2 = xC2 - 1
    elif key2 ==[[146,1]]:
        if yC2 > 1:
            nY2 = y2 + 1.42056
            p2.worldPosition.z = nY2
            y2 = p2.worldPosition.z
            yC2 = yC2 - 1
    elif key2 ==[[144,1]]:
        if yC2 < 4:
            nY2 = y2 - 1.42056
            p2.worldPosition.z = nY2
            y2 = p2.worldPosition.z
            yC2 = yC2 + 1
    else:
        pass
    nc2 = colours.colour[xC2 - 1][yC2 - 1]
    scene.objects['Suzanne_2'].replaceMesh('Suzanne_' + nc2, True, False)
    dc2 = nc2
def newP():
    contr = bge.logic.getCurrentController()
    ownr = contr.owner
    scene.objects['Suzanne_2'].visible = True
    scene.objects['Selector_2'].visible = True
    ownr.visible = False
def start():
    colours.p1Colour = dc
    colours.p2Colour = dc2
    scene.objects['MainCamera'].perspective = 1
    scene.replace('Main_Scene')
def apply():
    scene = bge.logic.getCurrentScene()
    scene.objects['Suzanne'].replaceMesh('Suzanne_' + colours.p1Colour + '.001', True, True)
    scene.objects['Suzanne.001'].replaceMesh('Suzanne_' + colours.p2Colour + '.001', True, True)