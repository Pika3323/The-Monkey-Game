import bge
import colours
import viewport
def apply():
    scene = bge.logic.getCurrentScene()
    scene.objects['Suzanne'].replaceMesh('Suzanne_' + colours.p1Colour + '.001', True, True)
    if colours.p2Active == True:
        scene.objects['Suzanne.001'].replaceMesh('Suzanne_' + colours.p2Colour + '.001', True, True)
        viewport.main()
    else:
        scene.objects['Suzanne.001'].endObject()