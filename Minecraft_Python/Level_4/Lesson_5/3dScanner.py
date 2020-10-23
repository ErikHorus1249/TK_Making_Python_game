import mcpi.minecraft as minecraft
import mcpi.block as block

mc =  minecraft.Minecraft.create()

FILENAME =  "output.csv"

SIZEX = 100
SIZEY = 20
SIZEZ = 100



def scan3D(fileName, originx, originy, originz):
	mc.postToChat("Scanning . . .")
	
	f = open(fileName, "w")

	f.write(str(SIZEX)+","+str(SIZEY)+","+str(SIZEZ)+"\n")
	
	f.write("\n")

	
	for y in range(SIZEY):

		for x in range(SIZEX):
			
			for z  in range(SIZEZ):
				if z == SIZEZ-1:
					f.write(str(int(mc.getBlock(originx + x, originy + y, originz + z))))
				else :
					f.write(str(int(mc.getBlock(originx + x, originy + y, originz + z)))+",")
		    
			f.write("\n")
			
		f.write("\n")
				
		
pos = mc.player.getTilePos()

scan3D(FILENAME, pos.x, pos.y, pos.z)

mc.postToChat("DONE")
			
			
			
			
			
