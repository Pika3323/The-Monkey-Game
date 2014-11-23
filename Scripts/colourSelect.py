import bge
import colours

cont = bge.logic.getCurrentController()
scene = bge.logic.getCurrentScene()
own = cont.owner
xC = 1
yC = 1
x = own.worldPosition.x
y = own.worldPosition.z
dc = "Color_White"
print(own.worldPosition)
def main():
    global xC
    global yC
    global x
    global y
    global dc
    key = cont.sensors['Keyboard'].events
    if key ==[[100,1]]:
        if xC < 4:
            nX = x + 1.42056
            own.worldPosition.x = nX
            x = own.worldPosition.x
            xC = xC + 1
    elif key ==[[97,1]]:
        if xC > 1:
            nX = x - 1.42056
            own.worldPosition.x = nX 
            x = own.worldPosition.x
            xC = xC - 1
    elif key ==[[119,1]]:
        if yC > 1:
            nY = y + 1.42056
            own.worldPosition.z = nY
            y = own.worldPosition.z
            yC = yC - 1
    elif key ==[[115,1]]:
        if yC < 4:
            nY = y - 1.42056
            own.worldPosition.z = nY
            y = own.worldPosition.z
            yC = yC + 1
    else:
        pass
    print(colours.colour[xC - 1][yC - 1])
    print("Y: " + str(yC))
    nc = colours.colour[xC - 1][yC - 1]
    scene.objects['Suzanne_Color_White'].replaceMesh('Suzanne_' + nc, True, False)
    dc = nc