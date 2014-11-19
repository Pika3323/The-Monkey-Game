import bge

cont = bge.logic.getCurrentController()
scene = bge.logic.getCurrentScene()
own = cont.owner
player = cont.owner
nm = player.name
sens_name = nm + ".Ball"
sensor = player.sensors[sens_name]
timer = player.sensors["Timer"]

def main():
	sensor.frequency = 0
	timer.level = 1
def stop():
	sensor.frequency = 10
	timer.level = 0