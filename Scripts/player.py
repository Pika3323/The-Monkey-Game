import bge


cont = bge.logic.getCurrentController()
own = cont.owner
scene = bge.logic.getCurrentScene()
player = scene.objects['Suzanne']
player2 = scene.objects['Suzanne.001']
p2_loc = player2.worldPosition
p_loc = player.worldPosition

if p_loc.z < -5:
    player.worldPosition = (0,0,3.5712)
    player.linearVelocity = (0,0,0)
    player.orientation = ([1,0,0],[0,1,0],[0,0,1])
if p2_loc.z < -5:
    player2.worldPosition = (2.734,0,3.5712)
    player2.linearVelocity = (0,0,0)
    player2.orientation = ([1,0,0],[0,1,0],[0,0,1])