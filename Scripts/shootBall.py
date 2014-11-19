import bge

cont = bge.logic.getCurrentController()
scene = bge.logic.getCurrentScene()
own = cont.owner
player = cont.owner
p_loc = player.worldPosition
sphere_cnt = 1
nm = player.name
light_name = nm + ".Spot"
light = player.children[light_name]
sphere_n = 'Sphere' + str(sphere_cnt)
new_ball = scene.addObject("Sphere", light, 1000)
new_ball.localLinearVelocity = (0, 0, -50)
sphere_cnt += 1
