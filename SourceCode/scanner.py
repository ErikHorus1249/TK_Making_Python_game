
import json #du lieu metadata
import mcpi.minecraft as minecraft # khai python cho mcpi
mc = minecraft.Minecraft.create() # cong cu xay dung

data = {} # khai bao noi chua du lieu : toa do(3) + id 
data['block'] = []   # du lieu dang list 
#dem, count = 0,0
	
def scan(pos,HEIGHT,WIDTHX,WIDTHZ):
	file = open('data.json', "w") # w - write 
	WIDTHX = WIDTHX/2
	WIDTHZ = WIDTHZ/2
	for  i in range(int(pos.x-WIDTHX),int(pos.x+WIDTHX)):
		mc.postToChat("Scanning...") # in ra thong diep dang quet
   		for  j in range(int(pos.y-1),int(pos.y+HEIGHT)):
       			for  k in range(int(pos.z-WIDTHZ),int(pos.z+WIDTHZ)):
           			bId = mc.getBlock(i,j,k)
           			if bId :
						data['block'].append({
						'x' : i-pos.x,
						'y' : j-pos.y,
						'z' : k-pos.z,
						'blockId' : bId
           				})
   	
	json.dump(data,file)
    
	# with open('BlockData2.json','w') as file:
    # 	json.dump(data,file)    
	
pos = mc.player.getPos();
scan(pos,20,50,50)


mc.postToChat("DONE") 
