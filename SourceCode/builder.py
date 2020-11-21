import time
import random
import json
import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

pos = mc.player.getPos();

x,y,z = pos.x, pos.y-1, pos.z

#bId = mc.getBlock(x,y,z)

#mc.postToChat(bId)


class Block:
    def __init__(self, x, y, z, blockId):
        self.blockName = ''
        self.x = x
        self.y = y
        self.z = z
        self.blockId = blockId
        

json_file = open("BlockData2.json","r")
data = json.load(json_file)

for block in data["block"]:
    if int(block["blockId"])!=0:
        mc.setBlock(int(block["x"])+x,int(block["y"])+y,int(block["z"])+z,int(block["blockId"]))

    
mc.postToChat("DONE") 
