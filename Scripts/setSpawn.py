import bge

cont = bge.logic.getCurrentController()
scene = bge.logic.getCurrentScene()
own = cont.owner
player = cont.owner
scene.objects['SpawnPoint'].worldPosition = player.worldPosition