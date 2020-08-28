import time
import random
import json
import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()
pos = mc.player.getPos();
x,y,z = pos.x, pos.y-1, pos.z

data = {}
data['block'] = []  
dem, count = 0,0
  
for  i in range(int(x-20),int(x+20)):
    for  j in range(int(y-50),int(y+50)):
        for  k in range(int(z-20),int(z+20)):
            bId = mc.getBlock(i,j,k)
            if bId :
                data['block'].append({
                'x' : i-x,
                'y' : j-y,
                'z' : k-z,
                'blockId' : bId
            })
    mc.postToChat("Scanning...")
     
with open('BlockData2.json','w') as file:
    json.dump(data,file)    

mc.postToChat("DONE") 