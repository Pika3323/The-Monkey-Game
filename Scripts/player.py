import bge

cont = bge.logic.getCurrentController()
own = cont.owner
player = cont.owner
p_loc = player.worldPosition

if p_loc.z < -5:
    player.worldPosition = (0,0,3.5712)
    player.linearVelocity = (0,0,0)
    player.orientation = ([1,0,0],[0,1,0],[0,0,1])
