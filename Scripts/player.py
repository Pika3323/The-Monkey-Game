import bge

cont = bge.logic.getCurrentController()
scene = bge.logic.getCurrentScene()
own = cont.owner
player = cont.owner
spawn = scene.objects['SpawnPoint'].worldPosition

if player.worldPosition.z < -5:
    player.worldPosition = spawn
    player.linearVelocity = (0,0,0)
    player.orientation = ([1,0,0],[0,1,0],[0,0,1])
