import bge

cont = bge.logic.getCurrentController()
scene = bge.logic.getCurrentScene()
own = cont.owner
player = cont.owner
nm = player.name
light_nm = player.name + ".Spot"
light = player.children[light_nm]
if light.energy == 0.0:
    light.energy = 10.0
else:
    light.energy = 0.0