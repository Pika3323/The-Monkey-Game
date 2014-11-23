import bge
import colours

cont = bge.logic.getCurrentController()
scene = bge.logic.getCurrentScene()
own = cont.owner
xC = 1
yC = 1
x = own.worldPosition.x
y = own.worldPosition.z
print(own.worldPosition)
def main():
    global xC
    global yC
    global x
    global y
    key = cont.sensors['Keyboard'].events
    print(key)
    if key ==[[100,1]]:
        if xC < 4:
            print(xC)
            nX = x + 1.42056
            own.worldPosition.x = nX
            x = own.worldPosition.x
            xC = xC + 1
    elif key ==[[97,1]]:
        if xC > 1:
            print(xC)
            nX = x - 1.42056
            own.worldPosition.x = nX 
            x = own.worldPosition.x
            xC = xC - 1
    elif key ==[[119,1]]:
        if yC > 1:
            print(yC)
            nY = y + 1.42056
            own.worldPosition.z = nY
            y = own.worldPosition.z
            yC = yC - 1
    elif key ==[[115,1]]:
        if yC < 4:
            print(yC)
            nY = y - 1.42056
            print(nY)
            own.worldPosition.z = nY
            y = own.worldPosition.z
            print(y)
            yC = yC + 1
    else:
        pass
    