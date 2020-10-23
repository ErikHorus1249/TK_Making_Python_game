import mcpi.minecraft as minecraft
import mcpi.block as block

mc =  minecraft.Minecraft.create()

FILENAME =  "output.csv"

def print3D(fileName, originx, originy, originz):

	f = open(fileName, "r")
	
	lines =  f.readlines()
	
	coords = lines[0].split(",")

	sizex = int(coords[0])
	sizey = int(coords[1])
	sizez = int(coords[2])
	
	lineidx = 1
	
	for y in range(sizey):

		mc.postToChat("Loading . . .")
		
		lineidx += 1
		
		for x in range(sizex):

			line =  lines[lineidx]
			
			lineidx += 1
			
			data = line.split(",")
			
			for z  in range(sizez):
		    
				blocId = int(data[z])
				
				mc.setBlock(originx + x, originy + y, originz + z, blocId)
			
				
		
pos = mc.player.getTilePos()

print3D(FILENAME, pos.x+1, pos.y, pos.z+1)

mc.postToChat("DONE")
			
			
			
			
			
