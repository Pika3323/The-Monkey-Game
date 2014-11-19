######################################################
#
#    Viewports.py  Blender Game Engine
#
#    Tutorial can be found at 
#
#    www.tutorialsforblender3d.com
#
#    Released under the Creative Commons Attribution 3.0 Unported License.	
#
#    If you use this code, please include this information header.
#
######################################################


# Main program
def main():
	
	# get current controller	
	controller = bge.logic.getCurrentController()
	
	# get the size of the game screen
	gameScreen = gameWindow()

	# get player cameras
	playerCams = playerCameras()
	
	# make player 1 camera the active camera
	activeCamera(playerCams)
		
	# set viewport size
	viewportSize(gameScreen, playerCams)
	
	# use viewports
	viewPorts(playerCams)

#####################################################

# Game window
def gameWindow():
	
	# get width and height of game window
	width = bge.render.getWindowWidth()
	height = bge.render.getWindowHeight()
	
	# return game window size
	return (width, height)

#####################################################

# Player cameras
def playerCameras():
		
	# get the current scene
	scene = bge.logic.getCurrentScene()
	
	# get list in objects in scene
	objList = scene.objects
	
	# get player cameras
	player1 = objList["Cam1"]	
	player2 = objList["Cam2"]
	
	# return player cameras
	return (player1, player2)

#####################################################

# Active Camera
def activeCamera(playerCams):

	# get current scene
	scene = bge.logic.getCurrentScene()

	# get player 1 camera
	player1 = playerCams[0]
	
	# make player 1 the active camera
	scene.active_camera = player1


#####################################################

# Viewport size
def viewportSize(gameScreen, playerCams):

	# game window width & height
	width = gameScreen[0]
	height = gameScreen[1]

	# player cameras
	player1 = playerCams[0]
	player2 = playerCams[1]
	
	# Player 1 viewport: top half
	left_1 = 0; bottom_1 = height/2; right_1 = width; top_1 = height
			   
	#  Player 2 viewport: bottom half
	left_2 = 0; bottom_2 = 0; right_2 = width; top_2 = height/2
	
	# make sure they are integers
	left_1 = int(left_1)
	bottom_1 = int(bottom_1)
	right_1 = int(right_1)
	top_1 = int(top_1)
	
	left_2 = int(left_2)
	bottom_2 = int(bottom_2)
	right_2 = int(right_2)
	top_2 = int(top_2)
	
	# set player viewports
	player1.setViewport( left_1, bottom_1, right_1, top_1)
	player2.setViewport( left_2, bottom_2, right_2, top_2)

#############################################################

# enable viewports	
def viewPorts(playerCams):

	# get player cameras
	player1 = playerCams[0]
	player2 = playerCams[1]
		
	# use viewports
	player1.useViewport = True
	player2.useViewport = True 

#############################################################

#import bge
import bge

# Run Main Program
main()