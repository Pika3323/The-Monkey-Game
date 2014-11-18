import bge

cont = bge.logic.getCurrentController()
scene = bge.logic.getCurrentScene()
own = cont.owner
player = cont.owner
p_loc = player.worldPosition
spawn_loc = player.children['Spot'].worldPosition
sphere_cnt = 1
sphere_n = 'Sphere' + str(sphere_cnt)
scene.addObject("Sphere", "Spot", 0)
scene.objects["Sphere"].localAngularVelocity = [0, -5, 0]
sphere_cnt += 1
print(scene.objects)