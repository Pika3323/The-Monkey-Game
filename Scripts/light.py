import bge

scene = bge.logic.getCurrentScene()
light = scene.objects['Spot']
if light.energy == 0.0:
    light.energy = 1.0
else:
    light.energy = 0.0